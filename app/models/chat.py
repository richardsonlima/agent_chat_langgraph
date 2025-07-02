from typing import List

# chat message and agent state models

class Message:
    """
    Represents a message exchanged in a chat, containing the sender's role and the message content.
    """
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class AgentState:
    """
    Represents the state of the agent, including the chat history.
    """
    def __init__(self, history: List[Message]):
        self.history = history
