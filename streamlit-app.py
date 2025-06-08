import streamlit as st
from gemini_bot import get_gemini_response

st.set_page_config(page_title="📚 GenAI Support Bot", page_icon="🤖")
st.title("📚 Online Bookstore Customer Support")

# Chat state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 Ask me something about your order, returns, etc.")

if user_input:
    with st.spinner("🤖 Thinking..."):
        response = get_gemini_response(st.session_state.chat_history, user_input)
    st.session_state.chat_history.append({"user": user_input, "bot": response})

# Show chat
for msg in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**Bot:** {msg['bot']}")

if st.button("🔄 Reset Conversation"):
    st.session_state.chat_history = []
