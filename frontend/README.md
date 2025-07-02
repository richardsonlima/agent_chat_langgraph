# Agent Chat LangGraph Frontend

A modern frontend for interacting with the Agent Chat LangGraph backend. This project provides a user-friendly web interface for real-time chat with the AI agent, supporting streaming responses and persistent conversation history.

## Features
- **Real-Time Chat**: Communicate with the AI agent using a responsive chat interface.
- **Streaming Responses**: See the assistant's replies as they are generated.
- **User Authentication**: (Optional) Identify users for personalized memory and chat history.
- **API Integration**: Connects seamlessly to the FastAPI backend endpoints.
- **Customizable UI**: Easily adapt the look and feel to your needs.

## Project Structure
```
frontend/
├── public/           # Static assets (favicon, images, etc.)
├── src/
│   ├── components/   # React/Vue/Svelte components (Chat, Message, etc.)
│   ├── pages/        # Main pages (Home, Chat, etc.)
│   ├── hooks/        # Custom hooks for API and state
│   ├── styles/       # CSS or Tailwind files
│   └── ...
├── package.json      # Project metadata and dependencies
├── README.md         # This file
└── ...
```

## Getting Started
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

## Environment Variables
- `VITE_API_URL` or `NEXT_PUBLIC_API_URL`: URL of the backend FastAPI server.

## Customization
- **UI/UX**: Edit components and styles in `src/` to match your branding.
- **API Logic**: Update API calls in hooks/components as needed.
- **Authentication**: Integrate with your auth provider if required.

## Example API Usage
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

## License
MIT License

---

*Created by Richardson Lima with ❤️ for advanced conversational AI experiences.*
