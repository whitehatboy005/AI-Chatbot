import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv('config.env')

#API KEY Environment
gemini_api = os.getenv("gemini_api")
genai.configure(api_key=st.secrets["gemini_api"])

def ai(txt):
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("I am Harish Assistant. In the purpose of learn Ethical Hacking.: "+txt)
    return response.text



# Streamlit interface
st.title("Welcome to Harish AI")

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

    if "hello" in command:
        with st.chat_message("bot"):
            st.write("Hi How can i help you.")
            st.session_state.message.append({"role": "bot", "message": "Hi How can i help you."})

    elif "Hello" in command:
        with st.chat_message("bot"):
            st.write("Hi How can i help you.")
            st.session_state.message.append({"role": "bot", "message": "Hi How can i help you."})

    elif "Who are you" in command:
        with st.chat_message("bot"):
            st.write("I'm Harish ai assistant")
            st.session_state.message.append({"role": "bot", "message": "I'm Harish assistant"})

    elif "who are you" in command:
        with st.chat_message("bot"):
            st.write("I'm Harish ai assistant")
            st.session_state.message.append({"role": "bot", "message": "I'm Harish assistant"})

    else:
        with st.chat_message("BOT"):
            data = ai(command)
            st.write(data)
            st.session_state.message.append({"role": "BOT", "message": data})

# Print session state for debugging
print(st.session_state.message)



