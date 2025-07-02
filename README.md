# Agent Chat LangGraph

A FastAPI-based conversational AI agent with long-term memory and modular architecture. This project leverages LangGraph for conversation flow and OpenRouter for LLM responses.

## Table of Contents
- [Key Features](#key-features)
- [Built With](#built-with)
- [Future Implementation Features](#future-implementation-features)
- [Use Cases](#use-cases)
- [Project Structure](#project-structure)
- [Agent Implementation](#agent-implementation)
- [Streamlit Quick Chat](#streamlit-quick-chat)
- [Frontend ReactJS](#frontend-reactjs)
- [Get Started](#get-started)
- [Development Notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Step-by-Step: Building and Running a LangGraph Agent](#step-by-step-building-and-running-a-langgraph-agent)

## Key Features
- **Conversational AI Agent**: Handles user messages, maintains context, and generates intelligent responses.
- **Long-Term Memory**: Stores and retrieves user chat history for personalized interactions.
- **REST API**: Exposes endpoints for chat.
- **CORS Enabled**: Ready for integration with web frontends.

## Built With
- [LangGraph](https://github.com/langchain-ai/langgraph): Enables sophisticated, stateful agent workflows
- [FastAPI](https://fastapi.tiangolo.com/): Provides the webhook endpoint and API infrastructure
- [OpenRouter](https://openrouter.ai/): LLM provider
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
├── app/
│   ├── main.py              # FastAPI app with webhook endpoint
│   ├── core/
│   │   └── memory.py        # Long-term memory management (JSON-based)
│   ├── models/
│   │   └── chat.py          # State and message models
│   ├── prompts/
│   │   └── system.py        # System prompt and instructions
│   ├── services/
│   │   └── llm.py           # LLM integration (OpenRouter)
│   ├── workflows/
│   │   └── graph.py         # Conversation flow logic using LangGraph (main agent logic)
│   ├── utils/               # (Optional) Utility functions
│   ├── scripts/             # (Optional) Helper scripts
│   └── tests/               # (Optional) Unit and integration tests
├── frontend/                # ReactJS frontend (see its own README.md)
├── streamlit_chat.py        # Streamlit quick chat interface for rapid validation
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
├── trash/                   # (Backup) Old files for reference
```

## Agent Implementation
The core agent logic is implemented in a modular way:
- **`app/workflows/graph.py`**: Main orchestrator for the agent's reasoning, conversation flow, and response generation using LangGraph.
- **`app/services/llm.py`**: Handles integration with the LLM (OpenRouter) for generating responses.
- **`app/core/memory.py`**: Manages long-term memory for storing and retrieving user chat history.
- **`app/models/chat.py`**: Defines data models for messages and agent state.

The FastAPI endpoint in `app/main.py` acts as the entry point, but the actual agent logic is in `workflows/graph.py` and the supporting modules above.

## Streamlit Quick Chat
For rapid validation and testing of the agent backend, you can use the included Streamlit chat interface. This allows you to interact with the agent without needing to run the full ReactJS frontend in `frontend/`.

**How to use:**

1. Install the required dependencies (if not already installed):
   ```bash
   pip install streamlit requests
   ```
2. Run the chat:
   ```bash
   streamlit run streamlit_chat.py
   ```
3. The chat will open in your browser and connect to the FastAPI backend at `http://localhost:8000/webhook`.

> The file is located at `streamlit_chat.py` in the project root.

## Frontend ReactJS
The project includes a modern ReactJS frontend located in the `frontend/` folder. This frontend provides a more complete and customizable chat interface for interacting with the agent.

**How to use:**

1. Go to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install the dependencies (using npm, yarn, or pnpm):
   ```bash
   npm install
   # or
   yarn
   # or
   pnpm install
   ```
3. Run the frontend:
   ```bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   ```
4. The frontend will be available at `http://localhost:3000` (or the configured port).

> For more details, see the `README.md` file inside the `frontend/` folder.

## Get Started
### Backend
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```
3. **Send requests** using your preferred HTTP client (e.g., Postman, curl, or a frontend app).

## Development Notes
- The current memory implementation (`core/memory.py`) is functional but illustrative. An advanced version using Mem0 will be released soon.
- Prompts and agent behavior can be customized in `prompts/system.py`.
- LLM provider and API keys are set in `services/llm.py`.
- For production, consider replacing JSON memory with a database or scalable store.

## Troubleshooting
- **CORS Issues**: Ensure `allow_origins` in `CORSMiddleware` is set appropriately for your frontend.
- **Backend Not Responding**: Check FastAPI logs and ensure the server is running on the expected port.
- **Memory Not Persisting**: Verify file permissions for your memory file or set the appropriate environment variable.
- **Model Usage Limit**: If you see usage limit errors, check your OpenRouter API quota or try again later.

## Step-by-Step: Building and Running a LangGraph Agent
This project follows a modular, professional approach to building a LangGraph-based conversational agent. Here is a high-level step-by-step guide inspired by the referenced Medium article:

1. **Define Message and State Models**
   - Implement message and state data structures in `app/models/chat.py`.
   - These models represent the conversation history and agent state.

2. **Create System Prompts**
   - Store and manage system prompts and instructions in `app/prompts/system.py`.
   - Prompts guide the agent's behavior and responses.

3. **Integrate the LLM**
   - Use `app/services/llm.py` to connect to your LLM provider (e.g., OpenRouter).
   - This module handles all LLM API calls and abstracts provider details.

4. **Implement Long-Term Memory**
   - Manage user memory and chat history in `app/core/memory.py`.
   - This enables persistent, personalized conversations.

5. **Design the Conversation Flow with LangGraph**
   - Orchestrate the agent's reasoning and workflow in `app/workflows/graph.py` using LangGraph.
   - Define how the agent processes input, updates state, and generates output.

6. **Expose the Agent via FastAPI**
   - The main FastAPI app in `app/main.py` provides a `/webhook` endpoint.
   - This endpoint receives chat payloads, manages memory, invokes the LangGraph agent, and returns responses.

7. **Test and Interact**
   - Use the included Streamlit chat (`streamlit_chat.py`) for rapid backend validation.
   - Or use the full ReactJS frontend in `frontend/` for a richer user experience.

8. **Customize and Extend**
   - Add new features, memory providers, or integrations by extending the modular components.
   - Update prompts, state logic, or LLM provider as needed.

> For a detailed, conceptual walkthrough, see the [Medium article](https://medium.com/@kts.ramamoorthy07/building-a-chat-agent-with-langgraph-a-step-by-step-guide-e3d3bbe640f0).

---

*Created by Richardson Lima with ❤️ for advanced conversational AI applications.*


