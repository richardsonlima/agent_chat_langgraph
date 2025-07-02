from openai import OpenAI
import os
from prompts import AGENT_SYSTEM_PROMPT

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-r1-0528-qwen3-8b:free")
REFERER = os.getenv("OPENROUTER_REFERER", "http://localhost")
TITLE = os.getenv("OPENROUTER_TITLE", "Local App")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

async def call_openrouter(messages, model=MODEL, max_fallbacks=4):
    """
    Asynchronously sends a list of chat messages to the OpenRouter API using a specified model, 
    with automatic fallback to alternative models if the request fails.

    Args:
        messages (list): A non-empty list of message dictionaries, each containing at least a "role" and "content" key.
        model (str, optional): The primary model to use for completion. Defaults to MODEL.
        max_fallbacks (int, optional): The maximum number of fallback models to try if the primary model fails. Defaults to 4.

    Raises:
        ValueError: If 'messages' is not a non-empty list.
        RuntimeError: If all model attempts fail, with details of the errors encountered.

    Returns:
        str: The content of the assistant's reply from the first successful model.
    """
    # Ensure messages is a non-empty list
    if not messages or not isinstance(messages, list):
        raise ValueError("The 'messages' field must be a non-empty list of messages.")
    # Ensure the system prompt is present as the first message
    if not (messages and messages[0].get("role") == "system"):
        messages = [{"role": "system", "content": AGENT_SYSTEM_PROMPT}] + messages
    # The openai package is not async, so run in thread pool
    import asyncio
    loop = asyncio.get_event_loop()
    # List of fallback models in order
    fallback_models = [
        MODEL,
        "microsoft/mai-ds-r1:free",
        "minimax/minimax-m1:extended",
        "mistralai/mistral-small-3.2-24b-instruct:free",
        "google/gemma-3n-e4b-it:free"
    ]
    tried = []
    for i, m in enumerate(fallback_models[:max_fallbacks+1]):
        def sync_call():
            try:
                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": REFERER,
                        "X-Title": TITLE,
                    },
                    model=m,
                    messages=messages,
                    max_tokens=1024
                )
                return completion.choices[0].message.content
            except Exception as e:
                tried.append((m, str(e)))
                return None
        reply = await loop.run_in_executor(None, sync_call)
        if reply:
            return reply
    # If all models fail, return detailed error
    raise RuntimeError(f"All models failed: {tried}")
