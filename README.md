# 🧠 AI Feedback Summarizer & Sentiment Analyzer

This project provides a simple Python script to **summarize feedback from a text file** and **analyze the sentiment** (positive, negative, neutral) of each line. It's ideal for educational purposes, internships, or basic product feedback analytics.

## 🚀 Features

- 📄 Summarizes large feedback files using **LSA Summarization (Sumy)**
- 😊 Analyzes sentiment using **TextBlob**
- 📊 Counts positive, negative, and neutral feedback entries
- 💬 Accepts plain `.txt` files as input

---

## 🛠️ Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt

import nltk
nltk.download('punkt')

📌 Usage
Edit the file path in summarizer_sentiment.py:
file_path = "path/to/your/sample_feedback.txt"

Then run:
python summarizer_sentiment.py


Output includes:

A concise summary of all feedback
A count of positive, negative, and neutral sentiments
