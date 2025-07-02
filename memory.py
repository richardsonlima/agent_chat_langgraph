# memory.py
import json
import os
from typing import Any, Dict, List

MEMORY_FILE = os.getenv("AGENT_MEMORY_FILE", "agent_memory.json")

def load_memory(user_id: str) -> List[Dict[str, Any]]:
    """Loads the user's long-term memory from a JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, ValueError):
        data = {}
    return data.get(user_id, [])

def save_memory(user_id: str, history: List[Dict[str, Any]]):
    """
    Saves the user's long-term memory (chat history) to a JSON file.

    Args:
        user_id (str): The unique identifier for the user.
        history (List[Dict[str, Any]]): The chat history to be saved for the user.

    Notes:
        - If the memory file exists, it loads the existing data; otherwise, it creates a new one.
        - Handles JSON decoding errors gracefully by resetting the data.
        - Overwrites the memory file with the updated data for the given user.
    """
    data = {}
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, ValueError):
            data = {}
    data[user_id] = history
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
