from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from graph import graph
from memory import load_memory, save_memory
from stream_chat import StreamChat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allowed domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def add_docstring(obj, doc):
    obj.__doc__ = doc
    return obj

@app.post("/webhook")
@add_docstring
async def webhook(request: Request):
    """
    FastAPI endpoint that receives a chat payload, loads and updates user long-term memory, calls the agent graph, and returns the assistant's response.
    Expects a JSON with 'user_id', 'message', and 'history'.
    """
    data = await request.json()
    user_id = data.get("user_id", "default")
    # Load user's long-term memory
    long_memory = load_memory(user_id)
    # Merge long-term memory with request history
    history = long_memory + data.get("history", [])
    # Add the latest user message explicitly if not present
    if data.get("message"):
        if not history or history[-1].get("content") != data["message"] or history[-1].get("role") != "user":
            history.append({"role": "user", "content": data["message"]})
    state = {"history": history}
    try:
        result = await graph.ainvoke(state)
        # Save updated long-term memory (all or last N, if you want to limit)
        save_memory(user_id, result["history"])
        # Extract the last assistant response
        last_message = next((m for m in reversed(result["history"]) if m["role"] == "assistant"), None)
        response_text = last_message["content"] if last_message else ""
        return {
            "history": result["history"],
            "response": response_text
        }
    except Exception as e:
        print(f"[ERROR webhook] {e}")
        error_msg = "Sorry, I reached the model usage limit or an error occurred. Please try again later."
        history.append({"role": "assistant", "content": error_msg})
        return {
            "history": history,
            "response": error_msg
        }

@app.post("/stream-token")
@add_docstring
async def get_stream_token(request: Request):
    """
    FastAPI endpoint to generate a StreamChat token for a given user_id.
    """
    data = await request.json()
    user_id = data.get("user_id")
    chat = StreamChat(api_key="xxxxxxx", api_secret="xxxxxxxxx")
    token = chat.create_token(user_id)
    return {"token": token}