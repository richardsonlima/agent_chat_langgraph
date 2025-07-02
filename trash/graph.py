from langgraph.graph import StateGraph, END
from state import AgentState, Message
from openrouter_llm import call_openrouter

# Node to generate a response using OpenRouter
async def generate_response(state):
    """
    Asynchronously generates a response based on the conversation history.

    Args:
        state (dict): A dictionary containing the conversation state, 
            specifically the "history" key which is a list of message dictionaries.

    Returns:
        dict: An updated state dictionary with the assistant's reply appended to the "history".

    Raises:
        Any exceptions raised by the call_openrouter function.
    """
    messages = state["history"]
    reply = await call_openrouter(messages)
    messages.append({"role":"assistant", "content": reply})
    return {"history": messages}

# Graph definition with a single node for generating responses
builder = StateGraph(dict)
builder.add_node("Responder",generate_response)
builder.set_entry_point("Responder")
builder.set_finish_point("Responder")
graph = builder.compile()

