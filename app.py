import streamlit as st
from transformers import pipeline

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="☕ Sentiment Analysis - Coffee Mood",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------- Coffee Theme CSS --------------------
coffee_style = """
<style>
body {
    background-color: #f5ebe0;
    color: #3e2723;
    font-family: 'Cairo', sans-serif;
}
div.stButton > button:first-child {
    background-color: #795548;
    color: white;
    border-radius: 12px;
    padding: 0.6em 1.5em;
    border: none;
    font-weight: bold;
}
div.stButton > button:first-child:hover {
    background-color: #5d4037;
    color: #f5ebe0;
}
textarea {
    background-color: #efebe9 !important;
    color: #3e2723 !important;
}
footer {visibility: hidden;}
</style>
"""
st.markdown(coffee_style, unsafe_allow_html=True)

# -------------------- Page Title --------------------
st.markdown("<h1 style='text-align:center; color:#3e2723;'>☕ Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center; color:#6d4c41;'>Analyze the emotion behind your words</h4>", unsafe_allow_html=True)
st.write("---")

# -------------------- Load Model --------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_analyzer = load_model()

# -------------------- User Input --------------------
user_input = st.text_area("Type your sentence below 👇", height=150, placeholder="Example: I love drinking coffee in the morning.")

# -------------------- Analyze Button --------------------
if st.button("☕ Analyze Sentiment"):
    if user_input.strip() != "":
        with st.spinner("Analyzing sentiment..."):
            result = sentiment_analyzer(user_input)[0]
            label = result['label']
            score = round(result['score'], 2)

            st.write("---")
            if label == "POSITIVE":
                st.success(f"😄 Positive sentiment — Confidence: {score}")
            elif label == "NEGATIVE":
                st.error(f"😠 Negative sentiment — Confidence: {score}")
            else:
                st.info(f"😐 Neutral sentiment — Confidence: {score}")
    else:
        st.warning("Please enter a sentence first 😅")

# -------------------- Footer --------------------
st.write("---")
st.markdown("<p style='text-align:center; color:#6d4c41;'>Made with ❤️ and ☕ by Dina</p>", unsafe_allow_html=True)
