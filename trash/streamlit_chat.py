import streamlit as st
"""
Streamlit chat application for "Baku - Personal AI Consultant".

Features:
- Initializes Streamlit page with custom title and icon.
- Configures logging to both file and console for debugging and monitoring.
- Manages user session with unique user ID and chat history.
- Displays chat messages in a WhatsApp-like interface, distinguishing between user and assistant roles.
- Highlights specific assistant error messages in red for better user feedback.
- Provides a chat input field for user interaction.
- Sends the latest 5 chat messages to a backend webhook for processing.
- Handles backend responses, updates chat history, and manages error states.
- Displays warnings when usage limits are reached or backend errors occur.

Dependencies:
- streamlit
- requests
- uuid
- logging
- os
"""
import requests
import uuid
import logging
import os

st.set_page_config(page_title="Baku - Personal AI Consultant", page_icon="🤖", layout="centered")
st.title("🤖 Baku - Personal AI Consultant")

# Configure logging to file and console
log_path = os.path.abspath('baku_streamlit.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler(log_path, mode='a'),
        logging.StreamHandler()
    ]
)
logging.info(f"[START] Streamlit started. Log at: {log_path}")

if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat in WhatsApp style
for msg in st.session_state.history:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        # Highlight friendly error message in red
        if "Sorry, I reached the model usage limit" in msg["content"]:
            with st.chat_message("assistant"):
                st.markdown(f"<b>Baku:</b> <span style='color:red'>{msg['content']}</span>", unsafe_allow_html=True)
        else:
            with st.chat_message("assistant"):
                st.markdown(f"<b>Baku:</b> {msg['content']}", unsafe_allow_html=True)

# Input field at the bottom
if prompt := st.chat_input("Type your message and press Enter..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    logging.info(f"User sent: {prompt}")
    with st.spinner("Baku is thinking..."):
        try:
            response = requests.post(
                "http://localhost:8000/webhook",
                json={
                    "user_id": st.session_state.user_id,
                    "history": st.session_state.history[-5:]  # send only the last 5 user messages
                },
                timeout=60
            )
            logging.info(f"Backend HTTP status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                logging.info(f"Backend response: {data}")
                assistant_msgs = [m for m in data["history"] if m["role"] == "assistant"]
                if assistant_msgs:
                    # Always add the last assistant response to history
                    st.session_state.history.append(assistant_msgs[-1])
                    # If it's a friendly error message, activate alert
                    if "Sorry, I reached the model usage limit" in assistant_msgs[-1]["content"]:
                        st.session_state["show_error"] = True
                    else:
                        st.session_state["show_error"] = False
            else:
                st.error("Error communicating with the agent.")
                logging.error(f"HTTP error communicating with backend: {response.status_code}")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
            logging.error(f"Exception calling backend: {e}")
    st.rerun()

# After the chat, display alert if necessary
if st.session_state.get("show_error"):
    st.warning("Model usage limit reached. Please wait or add credits to continue using Baku.")
