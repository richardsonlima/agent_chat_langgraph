# Agent Chat LangGraph

A FastAPI-based conversational AI agent with long-term memory, streaming chat support, and modular architecture. This project leverages LangGraph for conversation flow, OpenRouter for LLM responses, and StreamChat for real-time chat token generation.

## Table of Contents
- [Key Features](#key-features)
- [Built With](#built-with)
- [Future Implementation Features](#future-implementation-features)
- [Use Cases](#use-cases)
- [Project Structure](#project-structure)
- [Get Started](#get-started)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)

## Key Features
- **Conversational AI Agent**: Handles user messages, maintains context, and generates intelligent responses.
- **Long-Term Memory**: Stores and retrieves user chat history for personalized interactions.
- **Streaming Chat Support**: Integrates with StreamChat for real-time messaging.
- **REST API**: Exposes endpoints for chat and token generation.
- **CORS Enabled**: Ready for integration with web frontends.
- **Streamlit Frontend**: Quick testing interface for development and demos.

## Built With
- [LangGraph](https://github.com/langchain-ai/langgraph): Enables sophisticated, stateful agent workflows
- [FastAPI](https://fastapi.tiangolo.com/): Provides the webhook endpoint and API infrastructure
- [OpenRouter](https://openrouter.ai/): LLM provider
- [StreamChat](https://getstream.io/chat/): Real-time chat API
- [Streamlit](https://streamlit.io/): Rapid prototyping frontend
- Python 3.9+

## Future Implementation Features
- **PostgreSQL**: Will manage conversation states and history for scalability and reliability
- **WPPConnect**: Will handle WhatsApp integration for multi-channel support
- **Groq**: Will power the language model for natural conversations and transcribe voice messages to text
- **gTTS**: Will convert text responses to speech for voice-enabled interactions
- [**Mem0**](https://github.com/mem0ai/mem0): Will provide advanced, scalable, and semantic memory for the agent, enabling richer context and long-term knowledge retention

## Use Cases
- Personal AI assistant with persistent memory
- Prototyping and testing conversational agents
- Integrating advanced LLMs into web or mobile apps
- Research and experimentation with memory architectures

## Project Structure
```
agent_chat_langgraph/
├── agent.py           # FastAPI app with endpoints for chat and token
├── graph.py           # Conversation flow logic using LangGraph
├── memory.py          # Long-term memory management (JSON-based)
├── openrouter_llm.py  # LLM integration (OpenRouter)
├── prompts.py         # System prompt and instructions
├── state.py           # State and message models
├── stream_chat.py     # StreamChat integration
├── streamlit_chat.py  # Streamlit frontend for quick tests
└── frontend/          # (Optional) Web frontend (see README inside)
```

## Get Started
### Backend
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the FastAPI server**:
   ```bash
   uvicorn agent_chat_langgraph.agent:app --reload
   ```
3. **Send requests** using your preferred HTTP client (e.g., Postman, curl, or a frontend app).

### Streamlit Frontend (Quick Test)
```bash
streamlit run agent_chat_langgraph/streamlit_chat.py
```

### Web Frontend (Optional)
See `frontend/README.md` for setup and usage instructions if you wish to use or build a full web interface.

## Development Notes
- The current memory implementation (`memory.py`) is functional but illustrative. An advanced version using Mem0 will be released soon.
- Prompts and agent behavior can be customized in `prompts.py`.
- LLM provider and API keys are set in `openrouter_llm.py`.
- For production, consider replacing JSON memory with a database or scalable store.

## Troubleshooting
- **CORS Issues**: Ensure `allow_origins` in `CORSMiddleware` is set appropriately for your frontend.
- **Backend Not Responding**: Check FastAPI logs and ensure the server is running on the expected port.
- **Streamlit Errors**: Make sure all dependencies are installed and the backend is accessible at the configured URL.
- **Memory Not Persisting**: Verify file permissions for `agent_memory.json` or set `AGENT_MEMORY_FILE` env variable.
- **Model Usage Limit**: If you see usage limit errors, check your OpenRouter API quota or try again later.

---

*Created by Richardson Lima with ❤️ for advanced conversational AI applications.*


