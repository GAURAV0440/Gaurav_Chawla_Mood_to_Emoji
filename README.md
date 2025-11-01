## Mood2Emoji – Kid-Safe Text Mood Detector
Made by: Gaurav Chawla
For: Codingal Curriculum Developer (AI & Coding) Internship

## 🎯 Project Goal
To build a simple AI web app that reads a short sentence and shows a kid-friendly emoji (😀 😐 😞) with a one-line explanation — suitable for students aged 12–16.

## What This App Does:
1. Takes a short text input from the user.
2. Detects the mood or emotion in that text.
3. Shows an emoji and a short message (like “Sounds happy!”).
4. Filters out bad or inappropriate words to make it safe for kids.
5. Includes a Teacher Mode that explains how the app works.

## Tech Stack Used:
1. Python 3.9+ – used because it’s simple, widely used and easy for students to understand.
2. Streamlit – used to create the web app; it gives instant results with a clean and interactive interface.
3. NLTK (VADER) – used for analyzing the emotion in sentences. It’s a rule-based tool that understands sentences with negations like “I don’t love this” correctly.
4. Better Profanity – used to filter out bad or inappropriate words and make the app completely safe for kids.

## Why Not TextBlob?
I first tried using TextBlob because it is simple and gives a quick sentiment score.
But TextBlob does not handle negations properly — for example, it marks “I don’t hate this” as sad and “I don’t love this” as happy.
To fix this, I switched to VADER (from NLTK).
VADER understands such sentences correctly and still works on simple rule-based logic (not a heavy machine learning model).
It fits the assignment requirement and gives more accurate and meaningful results.

## Project Structure:
<img width="358" height="212" alt="image" src="https://github.com/user-attachments/assets/452915f2-032f-4b6e-b234-0f524d86eb8f" />

## How to Run This Project??

1. Clone or Download the Repo:
git clone https://github.com/GAURAV0440/Gaurav_Chawla_Mood_to_Emoji.git
cd Gaurav_Chawla_Mood_to_Emoji

2. Create Virtual Environment:
python3 -m venv .venv
source .venv/bin/activate

3. Install Requirements:
pip install -r requirements.txt
python -m nltk.downloader vader_lexicon

4. Run the App:
streamlit run app.py

## How Kids Learn From It (Simple 60-Minute Plan)
# Time	Activity:
0–10 mins	Introduction to moods and emojis. Discuss how computers can understand text.
10–20 mins	Explain how words can show happiness or sadness. (e.g., “love”, “hate”)
20–40 mins	Walk students through the Streamlit code and logic step-by-step. Let them try different sentences.
40–50 mins	Enable “Teacher Mode” and explain the app workflow visually.
50–60 mins	Students test their own sentences and observe results. Discuss which phrases change the mood and why.

# Known Limitations:
Works best for short, simple English sentences.
May not understand sarcasm or very complex grammar.
Emoji choice limited to 3 moods (😀 😐 😞) to keep it simple for learning.
Doesn’t store data — just live feedback for safety and privacy.

# Safety Notes:
All text inputs are filtered through better_profanity.
No data is stored or shared.
All outputs are age-appropriate.

# Example Tests:
Input	Output
I love coding!	😀 Sounds happy!
I don’t love this	😞 Sounds a bit sad!
I am eating lunch.	😐 Feels neutral!
You are stupid	😐 Let's use nice words only!

# Conclusion:
Mood2Emoji is a fun, safe and educational AI project that helps students understand how computers can read human emotions using text.
It’s simple, accurate and encourages kids to learn AI with creativity.
