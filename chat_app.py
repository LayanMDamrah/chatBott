import streamlit as st
import random

def get_response(text):
    text_lower = text.lower().strip()

    greetings = ["hi", "hello", "hey"]
    goodbays = ["bye", "goodbye",  "see you later"]
    how_are_you = ["how are you","whats up", "how do you do"]
    thanks = ["thanks", "thank you", "thx",  "welcom"]
    name_q = ["your name", "who are you", "what are you", "what's your name", "whats your name"]
    help_q = ["help", "help me", "i need help", "can you help"]
    if any(w in text_lower for w in greetings):
        return random.choice([
            "hey good to see you",
            "oh hey what's going on",
            "hi there how's it going",
            "hey what's up need anything",
            "hello always nice to have someone to talk to"
        ])

    if any(w in text_lower for w in goodbays):
        return random.choice([
            "take care",
            "bye come back anytime",
            "see you later hope your day goes well",
            "take care of yourself bye",
            "goodbye it was nice chatting with you"
        ])

    if any(w in text_lower for w in how_are_you):
        return random.choice([
            "i'm good thanks for asking what about you ?",
            "i'm doing well just here chatting with you",
            "not bad at all how are you ?",
            
        ])

    if any(w in text_lower for w in thanks):
        return random.choice([
            "of course anytime",
            "happy to help always",
            "no worries at all",
            "glad i could help",
       
        ])

    if any(w in text_lower for w in name_q):
        return random.choice([
            "i'm layan's chatbot nice to meet you",
            "people just call me the chat assistant ",
            "just your chatbot"
        ])

    if any(w in text_lower for w in help_q):
        return random.choice([
            "of course what do you need ?",
            "sure  tell me what's going on?",
            "i'll do my best what it is you looking for?"
        ])

    if "?" in text_lower:
        return random.choice([
            "that's actually a good question i'm not sure ",
            "i realy don't know",
            "wish i had an answer for you",
            "honestly no idea"
        ])

    if len(text_lower) < 5:
        return random.choice([
            "tell me more that was  short",
            "i'm listening go on"
        ])

    return random.choice([
        "keep going i'm listening",
        "tell me more about that",
        f"wait so you're saying \"{text}\" that's kind of interesting actually",
        "i see what you mean ?"
    ])


st.title("Layan Damrah Chat Bot ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})