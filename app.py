import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page configuration
st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

# FAQ data
faqs = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level programming language known for its simple syntax and wide range of applications."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a branch of AI that allows computers to learn patterns from data and make predictions."
    },
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial intelligence is the field of creating systems that can perform tasks that normally require human intelligence."
    },
    {
        "question": "What is NLP?",
        "answer": "NLP stands for Natural Language Processing. It helps computers understand and process human language."
    },
    {
        "question": "What is Streamlit?",
        "answer": "Streamlit is a Python framework used to quickly build interactive web applications for data and machine learning projects."
    },
    {
        "question": "What is GitHub?",
        "answer": "GitHub is a platform used to store, manage, and collaborate on software projects using Git."
    }
]

# Prepare FAQ questions
faq_questions = [faq["question"] for faq in faqs]

# TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

faq_vectors = vectorizer.fit_transform(faq_questions)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 FAQ Chatbot")
st.write("Ask me questions about AI, Python, or technology.")

# Display previous messages
for message in st.session_state.messages:

    if message["role"] == "user":
        st.chat_message("user").write(message["content"])

    else:
        st.chat_message("assistant").write(message["content"])

# Chat input
user_question = st.chat_input("Ask your question...")

if user_question:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    # Convert question into TF-IDF vector
    user_vector = vectorizer.transform([user_question])

    # Calculate similarity
    similarities = cosine_similarity(
        user_vector,
        faq_vectors
    )

    # Find best match
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    # Generate response
    if best_score >= 0.6:
        answer = faqs[best_match_index]["answer"]
    else:
        answer = (
            "Sorry, I couldn't find a relevant answer to your question."
        )

    # Add chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Refresh the page
    st.rerun()