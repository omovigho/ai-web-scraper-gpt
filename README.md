# 🌐 AI Web Scraper GPT

An AI-powered web scraping tool that extracts and summarizes content from any public URL using OpenAI's GPT model and a clean Streamlit interface.

---

## 🚀 Features

- 🌍 Scrape webpage content using `requests` and `BeautifulSoup`
- 🧠 Summarize with OpenAI GPT (custom instructions allowed)
- 💻 Easy-to-use Streamlit web interface
- 📁 Save results automatically to `ai_summary.txt`

---

## 🔧 Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
````

---

## 🔑 Setup OpenAI API Key

Export your OpenAI API key before running:

```bash
export OPENAI_API_KEY=your-api-key-here
```

Or on Windows:

```cmd
set OPENAI_API_KEY=your-api-key-here
```

---

## 💡 How to Run

### ✅ CLI Version (Basic):

```bash
python ai_web_scraper.py
```

### ✅ Streamlit Web App:

```bash
streamlit run ai_web_scraper.py
```

---

## ✍️ Example Prompts

* "Summarize this article in bullet points."
* "Explain the page like I'm a beginner."
* "Extract product features mentioned on this page."

---

## 📂 Output

Summaries are saved in a file:

```
ai_summary.txt
```

---

## 🧩 Future Ideas

* 🔁 Batch scraping from a list of URLs
* 📊 Export summaries to CSV/JSON
* 🗃️ Archive scraped content
* 🧪 Add keyword extraction or sentiment analysis

---

## 📜 License

MIT License

---

## 🤝 Contributing

PRs welcome! For major changes, open an issue first to discuss.

---

## 👨‍💻 Built With

* Python
* BeautifulSoup4
* OpenAI GPT
* Streamlit

```