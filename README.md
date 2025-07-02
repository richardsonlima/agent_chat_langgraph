# Agent Chat LangGraph

A FastAPI-based conversational AI agent with long-term memory, streaming chat support, and modular architecture. This project leverages LangGraph for conversation flow, OpenRouter for LLM responses, and StreamChat for real-time chat token generation.

## Features
- **Conversational AI Agent**: Handles user messages, maintains context, and generates intelligent responses.
- **Long-Term Memory**: Stores and retrieves user chat history for personalized interactions.
- **Streaming Chat Support**: Integrates with StreamChat for real-time messaging.
- **REST API**: Exposes endpoints for chat and token generation.
- **CORS Enabled**: Ready for integration with web frontends.

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
└── frontend/          # Frontend web application (see below)
```

## Frontend
A modern frontend web application is included for interacting with the agent backend. It provides a real-time chat interface and supports streaming responses.

### Features
- Real-time chat with the AI agent
- Streaming responses as the assistant types
- User identification for personalized memory
- Easy integration with the backend API
- Customizable UI/UX

### Project Structure (example)
```
frontend/
├── public/           # Static assets (favicon, images, etc.)
├── src/
│   ├── components/   # UI components (Chat, Message, etc.)
│   ├── pages/        # Main pages (Home, Chat, etc.)
│   ├── hooks/        # API and state management
│   ├── styles/       # CSS or Tailwind files
│   └── ...
├── package.json      # Project metadata and dependencies
├── README.md         # Frontend documentation
└── ...
```

### Getting Started
1. **Install dependencies**:
   ```bash
   npm install
   # or
   yarn install
   ```
2. **Configure API URL**:
   - Set the backend API URL (e.g., in `.env` or config file) to point to your FastAPI server.
3. **Run the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```
4. **Open your browser** at `http://localhost:3000` (or the port shown in your terminal).

### Environment Variables
- `VITE_API_URL` or `NEXT_PUBLIC_API_URL`: URL of the backend FastAPI server.

### Example API Usage
```js
// Example: Sending a message to the agent
fetch(`${process.env.VITE_API_URL}/webhook`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ user_id: 'user123', message: 'Hello!', history: [] })
})
  .then(res => res.json())
  .then(data => console.log(data.response));
```

## API Endpoints
### `POST /webhook`
- **Description**: Receives a chat payload, updates user memory, invokes the agent, and returns the assistant's response.
- **Request Body**:
  - `user_id` (string): Unique user identifier
  - `message` (string): Latest user message
  - `history` (list): (Optional) Recent chat history
- **Response**:
  - `history`: Updated chat history
  - `response`: Assistant's latest reply

### `POST /stream-token`
- **Description**: Generates a StreamChat token for a given user.
- **Request Body**:
  - `user_id` (string): Unique user identifier
- **Response**:
  - `token`: StreamChat token

## Setup & Usage (Backend)
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the FastAPI server**:
   ```bash
   uvicorn agent_chat_langgraph.agent:app --reload
   ```
3. **Send requests** using your preferred HTTP client (e.g., Postman, curl, or a frontend app).

## Environment Variables (Backend)
- `AGENT_MEMORY_FILE`: (Optional) Path to the JSON file for storing user memory. Defaults to `agent_memory.json`.

## Customization
- **Prompts**: Edit `prompts.py` to change the agent's system prompt and behavior.
- **LLM Provider**: Update `openrouter_llm.py` to use a different LLM or API key.
- **Memory Logic**: Adjust `memory.py` for alternative storage (e.g., database).
- **Frontend UI/UX**: Edit components and styles in `frontend/src/` to match your branding.

## License
MIT License

---

## Additional: Streamlit Frontend for Quick Testing
A simple Streamlit-based frontend (`streamlit_chat.py`) is included in this repository. You can use it for quick local tests and prototyping with the agent backend. To run it:

```bash
streamlit run agent_chat_langgraph/streamlit_chat.py
```

This will launch a web interface for chatting with the agent, ideal for development and debugging purposes.

---

## Note on Memory Implementation
The current memory implementation (`memory.py`) is fully functional but intended as a simple illustrative example. A more advanced version leveraging the capabilities of Mem0 will be released soon, providing enhanced memory features and scalability.

---

*Created by Richardson Lima with ❤️ for advanced conversational AI applications.*


