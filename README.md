# 🤖 FAQ Chatbot

A simple AI-powered FAQ chatbot built with Python, Streamlit, and Natural Language Processing techniques.

## ✨ Features

- Interactive chatbot interface
- FAQ-based question answering
- TF-IDF text vectorization
- Cosine similarity matching
- Handles different ways of asking the same question
- Rejects unrelated questions
- Maintains conversation history

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLTK
- TF-IDF
- Cosine Similarity

## 🧠 How It Works

1. The user enters a question.
2. The question is converted into a TF-IDF vector.
3. The chatbot compares it with the stored FAQ questions.
4. Cosine similarity identifies the closest FAQ.
5. If the similarity score is high enough, the corresponding answer is displayed.
6. Otherwise, the chatbot informs the user that it doesn't have a relevant answer.

## 🚀 How to Run

Install the required libraries:

```bash
pip install -r requirements.txt