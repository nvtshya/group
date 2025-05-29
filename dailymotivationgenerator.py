import streamlit as st
import random
from datetime import date

# Page config
st.set_page_config(page_title="Daily Motivation Generator", layout="wide")

# Custom styles
st.markdown(
     """
    <style>
    .stApp {
        background-color: #ffe4ec;
        color: #a4005a;
    }

    .stButton>button {
        background-color: #f8c1d1;
        color: #a4005a;
        border-radius: 10px;
        font-weight: bold;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .stButton>button:hover {
        background-color: #f6a5c0;
        box-shadow: 0 0 10px #ffc1e3, 0 0 20px #ffc1e3;
    }

    .stButton>button:hover::after {
        content: '✨';
        position: absolute;
        top: 50%;
        right: 10px;
        transform: translateY(-50%);
        animation: sparkle 1s infinite;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: translateY(-50%) scale(1); }
        50% { opacity: 1; transform: translateY(-50%) scale(1.3); }
    }

    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #a4005a !important;
    }

    input, .stTextInput > div > div > input {
        color: #a4005a !important;
    }

    .motivation {
        color: #a4005a;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout columns
col1, col2 = st.columns([2, 1])

# Column 1: Main content
with col1:
    st.markdown("<h1 style='text-align:center;'>✨ Daily Motivation Generator ✨</h1>", unsafe_allow_html=True)

    # Quotes
    quotes = [
        "🌟 Believe in yourself and all that you are.",
        "💪 You are stronger than you think.",
        "🌈 Every day is a second chance.",
        "🔥 Stay positive. Work hard. Make it happen.",
        "🚀 Don’t watch the clock; do what it does. Keep going."
    ]

    # Quote of the Day
    index = date.today().day % len(quotes)
    st.markdown(f"💖 *Quote of the Day:* <span class='motivation'>{quotes[index]}</span>", unsafe_allow_html=True)

    # Button for random quote
    if st.button("🎁 Give me more sparkle!"):
        st.markdown(f"✨ <span class='motivation'>{random.choice(quotes)}</span>", unsafe_allow_html=True)
        st.balloons()

    # Motivation game
    st.markdown("---")
    st.markdown("<h3>🎮 Motivation Word Guessing Game</h3>", unsafe_allow_html=True)

    words = {
        "dream": "It's something you hope for while asleep or awake.",
        "hustle": "It means to work hard, often in a busy or energetic way.",
        "focus": "It helps you avoid distractions.",
        "growth": "Something plants and people both experience.",
        "courage": "It's what you need to face your fears."
    }

    word, hint = random.choice(list(words.items()))
    hidden = "_ " * len(word)
    st.markdown(f"Hint: *{hint}*")
    st.write(f"Word: {hidden.strip()}")
    guess = st.text_input("Type your guess here", key="game").lower()

    if guess:
        if guess == word:
            st.success("🎉 Correct! You're a true motivator!")
        else:
            st.error("❌ Oops! Try again!")

# Column 2: Image
with col2:
    st.image("download.jpg", width=300, caption="😺 You got this!")