# AI-Powered Web Scraper with Natural Language Extraction using OpenAI

import requests
from bs4 import BeautifulSoup
import openai
import os
import streamlit as st

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching webpage: {e}"


def extract_clean_text(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Extract text
    text = soup.get_text(separator=" ", strip=True)
    return text[:5000]  # Limit input size for GPT


def summarize_with_ai(text, instructions="Summarize the main points of this webpage"):
    prompt = f"{instructions}:\n\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful summarizer of web content."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


# --- Streamlit UI ---
st.set_page_config(page_title="AI Web Scraper", layout="centered")
st.title("🌐 AI-Powered Web Scraper")

url = st.text_input("Enter the URL to scrape")
instructions = st.text_input("Summarization Prompt", value="Summarize the main points of this webpage")

if st.button("Scrape and Summarize"):
    if url:
        html = fetch_webpage(url)

        if html.startswith("Error"):
            st.error(html)
        else:
            with st.spinner("Extracting and summarizing content..."):
                raw_text = extract_clean_text(html)
                summary = summarize_with_ai(raw_text, instructions)

            st.subheader("🔍 AI Summary")
            st.write(summary)

            with open("ai_summary.txt", "w") as f:
                f.write(summary)

            st.success("✅ Summary saved to ai_summary.txt")
    else:
        st.warning("Please enter a valid URL.")
