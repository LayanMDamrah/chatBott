import streamlit as st
import random

def get_response(text):
    text_lower = text.lower().strip()

    greetings = ["hi", "hello", "hey" ,"nice to meet you"]
    goodbays = ["bye", "goodbye",  "see you later"]
    how_are_you = ["how are you","whats up", "how do you do"]
    thanks = ["thanks", "thank you", "thx",  "welcom"]
    name_q = ["your name", "who are you", "what are you", "what's your name", "whats your name"]
    help_q = ["help", "help me", "i need help", "can you help"]
    topics_q = ["what can you talk about", "what do you know", "talk to me", "tell me something", "what topics", "what can we talk about", "suggest something", "what can you do"]

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

    if any(w in text_lower for w in topics_q):
        return random.choice([
            "sure i can talk about a few things - palestinian cities like tulkarm nablus jenin gaza jerusalem hebron ramallah and jericho, science questions, or just normal chat stuff like how you're doing what's on your mind and so on",
            "glad you asked - you can ask me about palestinian cities and what they're known for, throw some science questions my way, or we can just talk casually whatever you feel like",
            "we can talk about palestinian cities and their history, science related stuff, or just have a normal conversation - your call"
        ])

    if "tulkarm" in text_lower:
        return "tulkarm is a city in the northern west bank known for its agricultural land especially citrus fruits it also has a strong history of resistance and is home to many refugee camps like nur shams and tulkarm camp"

    if "nablus" in text_lower:
        return "nablus is famous for its old city its traditional soap made from olive oil and of course knafeh nablus is considered the home of knafeh and it's known as the mountain of fire for its long history of resistance"

    if "jenin" in text_lower:
        return "jenin is known for its refugee camp which became a symbol of resistance it also has a famous freedom theatre and fertile agricultural lands in the jenin valley"

    if "ramallah" in text_lower:
        return "ramallah is the administrative center of palestine it has a lively cultural scene with cafes theatres and art galleries it's also where the muqata the presidential compound is located"

    if "jerusalem" in text_lower or "al quds" in text_lower:
        return "jerusalem or al quds is the heart of palestine it's home to the al aqsa mosque the dome of the rock the church of the holy sepulchre and one of the oldest old cities in the world it holds deep meaning for muslims christians and jews"

    if "gaza" in text_lower:
        return "gaza is one of the oldest cities in the world it's known for its resilience and resistance its people have faced decades of siege but the city has a rich history of trade culture and crafts like pottery and weaving"

    if "hebron" in text_lower or "khalil" in text_lower:
        return "hebron known in arabic as al khalil is famous for its glassblowing tradition its old market and the ibrahimi mosque it's also known for producing grapes and its strong crafts industry"

    if "jericho" in text_lower:
        return "jericho is considered one of the oldest cities in the world it sits below sea level near the dead sea and is known for its warm climate its dates and bananas and ancient archaeological sites"

    science_q = ["what is", "how does", "why does", "what are", "explain", "define", "science", "physics", "chemistry", "biology", "space", "planet", "atom", "gravity", "evolution", "dna", "cell", "energy", "light", "sound"]
    if any(w in text_lower for w in science_q):
        return random.choice([
            "that's a science question i find those really interesting honestly i just don't have the full answer right now",
            "oh good one i know a bit about that but not enough to give you a proper answer",
            "science questions are my weakness but i respect you for asking",
            "hmm i think i learned something about that once but it's not coming to me right now",
            "you should look that up properly i'd hate to give you wrong info on something like that"
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
