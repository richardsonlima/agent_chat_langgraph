from typing import Dict, List

class Message:
    """
    Represents a message exchanged in a chat, containing the sender's role and the message content.

    Attributes:
        role (str): The role of the sender (e.g., 'user', 'assistant').
        content (str): The textual content of the message.

    Args:
        role (str): The role of the sender.
        content (str): The content of the message.
    """
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
        
class AgentState:
    """
    Represents the state of the agent, including the chat history.

    Attributes:
        history (List[Message]): The list of messages exchanged in the chat.

    Args:
        history (List[Message]): The chat history.
    """
    def __init__(self, history: List[Message]):
        self.history = history