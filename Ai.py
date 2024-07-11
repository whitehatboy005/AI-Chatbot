import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv('config.env')

#API KEY Environment
GEMINI_API = os.getenv("GEMINI_API")
NAME = os.getenv("NAME")

genai.configure(api_key="GEMINI_API")

def ai(txt):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(txt)
    return response.text



# Streamlit interface
st.title(f"Welcome to {NAME} AI")

command = st.chat_input("How can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])

if command:

    with st.chat_message("user"):
        st.write(command)
        st.session_state.message.append({"role": "user", "message": command})

    if "hello" in command or "Hello" in command:
        with st.chat_message("bot"):
            st.write("Hi How can i help you.")
            st.session_state.message.append({"role": "bot", "message": "Hi How can i help you."})


    elif "Who are you" in command or "who are you" in command:
        with st.chat_message("bot"):
            st.write(f"I'm {NAME} ai assistant")
            st.session_state.message.append({"role": "bot", "message": f"I'm {NAME} assistant"})


    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role": "BOT", "message": data})

# Print session state for debugging
print(st.session_state.message)



