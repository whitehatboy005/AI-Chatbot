# AI Chatbot
This Python application creates a chatbot interface using Streamlit, allowing users to interact with an AI model powered by the google.generativeai library. The chatbot responds to various commands and queries, providing conversational responses based on the input.

## Features
- **Chat Input**: Users can enter messages or commands in the chat interface.
- **Bot Responses**: Based on the input, the chatbot responds with predefined messages or generates content using the AI model.
- **Session Management**: Maintains a history of conversations within the session using Streamlit's session state.
- **Personalization**: Displays a personalized greeting and identifies itself as an AI assistant.
- **Dynamic Content Generation**: Uses the AI model to generate text content for user queries beyond predefined responses.

## Model Output

![Screenshot 2024-07-11 173855](https://github.com/whitehatboy005/Ai/assets/147156726/042b5ad2-286e-4743-a921-bbe0e7b06203)
## API KEY OBTAIN

To get GEMINI_API_KEY in this link https://aistudio.google.com/app/apikey

## Installation
## Clone the Repository
```bash
git clone https://github.com/whitehatboy005/AI-Chatbot
```
## Move the file
```bash
cd AI-Chatbot
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Config Your API Key
```bash
notepad config.env
```
## Run the Program
```bash
streamlit run Ai.py
```

