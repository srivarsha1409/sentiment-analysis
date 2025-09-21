import streamlit as st
import pickle
import re
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("sentiment_bilstm.keras")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


max_len = 100


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text


sentiment_map = {
    0: ("Negative", "😡", "#ff4b4b"),
    1: ("Negative", "😕", "#ff6f61"),
    2: ("Neutral",  "😐", "#f7b32b"),
    3: ("Positive", "🙂", "#4caf50"),
    4: ("Positive", "🤩", "#2e7d32")
}


st.set_page_config(page_title="Sentiment Analysis", page_icon="⭐", layout="wide")


st.markdown("""
<style>
body {
    background: linear-gradient(to right, #a8edea, #fed6e3);
}
.stButton>button {
    background-color: #0a9396;
    color:white;
    font-weight:bold;
    border-radius:10px;
    height:40px;
    width:150px;
}
.stTextArea textarea {
    border-radius: 10px;
    border: 2px solid #0a9396;
    padding: 10px;
}
.card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    margin-top: 20px;
    transition: transform 0.2s;
}
.card:hover {
    transform: scale(1.02);
}
.emoji {
    font-size: 60px;
    text-align: center;
}
.prob-bar {
    height: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


st.markdown('<h1 style="text-align:center; color:#0a9396;">⭐ Sentiment Analysis App ⭐</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; font-size:18px;">Enter a product review to see its predicted sentiment.</p>', unsafe_allow_html=True)


user_input = st.text_area("✍️ Type your review here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a review!")
    else:
       
        cleaned = clean_text(user_input)
        seq = tokenizer.texts_to_sequences([cleaned])
        pad = pad_sequences(seq, maxlen=max_len, padding='post')

       
        pred = model.predict(pad)
        label = int(np.argmax(pred))
        sentiment, emoji, color = sentiment_map[label]

        
        st.markdown(f"""
        <div class="card" style="border-left:8px solid {color};">
            <div class="emoji">{emoji}</div>
            <h2 style="color:{color}; text-align:center;">{sentiment}</h2>
            <p style="text-align:center; font-weight:bold;">Confidence Scores for 1-5 Stars:</p>
        </div>
        """, unsafe_allow_html=True)

        
        for i, score in enumerate(pred[0]):
            st.markdown(f"""
            <p>⭐ {i+1} Star</p>
            <div class="prob-bar" style="background: linear-gradient(to right, {color}, #ffffff); width:{score*100}%;"></div>
            """, unsafe_allow_html=True)
