import streamlit as st
from better_profanity import profanity
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Ensure VADER is available (auto-download if missing)
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

# --- Setup ---
st.set_page_config(page_title="Mood2Emoji", page_icon="😀", layout="centered")
st.title("🧠 Mood2Emoji – Kid-Safe Text Mood Detector")

profanity.load_censor_words()
analyzer = SentimentIntensityAnalyzer()

# --- Mood detection ---
def analyze_mood(text: str):
    if not text.strip():
        return "😐", "Please type something first!"
    if profanity.contains_profanity(text):
        return "😐", "Let's use nice words only!"

    score = analyzer.polarity_scores(text)["compound"]

    if score > 0.2:
        return "😀", "Sounds happy!"
    elif score < -0.2:
        return "😞", "Sounds a bit sad!"
    else:
        return "😐", "Feels neutral!"

# --- Input + Output ---
user_text = st.text_input("Enter a short sentence:")
if user_text:
    emoji, explanation = analyze_mood(user_text)
    st.markdown(f"### {emoji}  {explanation}")

# --- Teacher Mode ---
with st.expander("👩‍🏫 Teacher Mode – How it works"):
    st.markdown(
        """
        Step 1 → Student enters a sentence  
        Step 2 → Bad words are filtered  
        Step 3 → VADER computes a sentiment score  
        Step 4 → Score is mapped to 😀 😐 😞  
        Step 5 → Kid-safe emoji + short message shown
        """
    )
st.markdown("---")
st.caption("Made for Codingal | Gaurav Chawla | Mood2Emoji App")