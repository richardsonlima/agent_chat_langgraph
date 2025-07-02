import React, { useState } from "react";
import { MessageList, Input, Button } from "react-chat-elements";
import "react-chat-elements/dist/main.css";

const API_URL = "http://localhost:8000/webhook";

function stripMarkdown(text) {
  return text
    .replace(/(\*\*|__)(.*?)\1/g, '$2') // bold
    .replace(/(\*|_)(.*?)\1/g, '$2') // italic
    .replace(/`([^`]+)`/g, '$1') // inline code
    .replace(/!\[.*?\]\(.*?\)/g, '') // images
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // links
    .replace(/^#+\s/gm, '') // headings
    .replace(/^\s*[-*+]\s+/gm, '') // unordered lists
    .replace(/^\s*\d+\.\s+/gm, '') // ordered lists
    .replace(/>\s?/g, '') // blockquotes
    .replace(/\\([\\`*_{}[\]()#+\-.!])/g, '$1') // escaped chars
    .replace(/\n{2,}/g, '\n') // multiple newlines
    .trim();
}

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = {
      position: "right",
      type: "text",
      text: input,
      date: new Date(),
    };
    setMessages((msgs) => [...msgs, userMsg]);
    setInput("");
    setLoading(true);

    // Monta o histórico para o backend
    const history = [
      ...messages
        .filter((m) => m.type === "text")
        .map((m) => ({
          role: m.position === "right" ? "user" : "assistant",
          content: m.text,
        })),
      { role: "user", content: input },
    ];

    try {
      const resp = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: "frontend",
          message: input,
          history,
        }),
      });
      const data = await resp.json();
      setMessages((msgs) => [
        ...msgs,
        {
          position: "left",
          type: "text",
          text: stripMarkdown(data.response),
          date: new Date(),
        },
      ]);
    } catch (e) {
      setMessages((msgs) => [
        ...msgs,
        {
          position: "left",
          type: "text",
          text: "Erro ao conectar ao backend.",
          date: new Date(),
        },
      ]);
    }
    setLoading(false);
  };

  return (
    <div style={{
      maxWidth: 600,
      margin: "40px auto",
      padding: 16,
      boxSizing: "border-box",
      width: "100%",
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      background: "#f9f9f9"
    }}>
      <h2 style={{ textAlign: "center", fontSize: 24, marginBottom: 16 }}>Chatbot</h2>
      <div style={{ flex: 1, minHeight: 0 }}>
        <MessageList
          className="message-list"
          lockable={true}
          toBottomHeight={"100%"}
          dataSource={messages}
          style={{ maxHeight: "60vh", overflowY: "auto", background: "#fff", borderRadius: 8, boxShadow: "0 1px 4px #0001", padding: 8 }}
        />
      </div>
      <div style={{ display: "flex", marginTop: 10, gap: 8 }}>
        <Input
          placeholder="Digite sua mensagem..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          disabled={loading}
          style={{ flex: 1, minWidth: 0 }}
          inputStyle={{ fontSize: 16 }}
        />
        <Button
          text="Enviar"
          onClick={sendMessage}
          disabled={loading}
          style={{ minWidth: 90, fontSize: 16 }}
        />
      </div>
      <style>{`
        @media (max-width: 700px) {
          div[style*='max-width: 600px'] {
            max-width: 100vw !important;
            margin: 0 !important;
            padding: 8px !important;
          }
          .message-list {
            font-size: 15px !important;
          }
        }
        @media (max-width: 480px) {
          div[style*='max-width: 600px'] {
            padding: 2px !important;
          }
          .message-list {
            font-size: 13px !important;
          }
        }
      `}</style>
    </div>
  );
}

export default App;