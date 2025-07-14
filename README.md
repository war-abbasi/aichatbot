# 🤖 Rule-Based FAQ Chatbot

A simple chatbot built in Python to answer frequently asked questions (FAQs) for a **university** or **company**, using rule-based logic and natural language processing techniques.

---

## 📌 Overview

This chatbot uses a combination of **pattern matching**, **intent mapping**, and **basic NLP** to understand user queries and respond with pre-defined answers. It can handle common questions like admission process, office hours, contact details, etc., and responds with fallback messages when the query doesn't match known patterns.

---

## ✨ Features

* 🧠 Rule-based question answering system
* 📚 Intents and responses defined in JSON/dictionary
* 🧾 Regex-based pattern matching for flexibility
* 🛠️ Built in Python using **NLTK** for basic NLP
* ❓ Fallback response for unrecognized questions

---

## 🛠 Tech Stack

* Python 3.x
* [NLTK](https://www.nltk.org/) (for tokenization, stopwords, etc.)
* JSON (for storing intents & responses)
* Regex (for pattern-based matching)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/war-abbasi/aichatbot.git
cd aichatbot
```

---

### 2. Install Dependencies

```bash
pip install nltk
```

Run the following to download NLTK data (first time only):

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

### 3. Run the Chatbot

```bash
python chatbot.py
```

You'll see:

```
Welcome to the University FAQ Chatbot! Ask me anything.
Type 'exit' to quit.
You: 
```

---

## 📄 Example Intents (in `intents.json`)

```json
{
  "intents": [
    {
      "tag": "admissions",
      "patterns": ["how to apply", "admission process", "apply for admission"],
      "responses": ["You can apply through our online portal at admissions.university.edu."]
    },
    {
      "tag": "office_hours",
      "patterns": ["when is the office open", "office hours", "what are the timings"],
      "responses": ["Our office is open Monday to Friday, 9am to 5pm."]
    }
  ]
}
```

---

## 🤖 Logic Flow

1. Preprocess the input (tokenize, lowercasing, remove stopwords)
2. Match the query with intent patterns using regex
3. Return a matching response or fallback reply like:

> "I'm sorry, I didn't understand that. Please contact our support for more help."

---

## 📂 Project Structure

```
.
├── chatbot.py            # Main chatbot script
├── intents.json          # Defined intents and responses
├── README.md             # Project documentation
└── requirements.txt      # (optional) List of dependencies
```

---

## 📌 Example Interaction

```
You: How to apply?
Bot: You can apply through our online portal at admissions.university.edu.

You: What are your office hours?
Bot: Our office is open Monday to Friday, 9am to 5pm.

You: Tell me about scholarships.
Bot: I'm sorry, I didn't understand that. Please contact our support for more help.
```

---

## 📜 License

MIT License — Feel free to use and improve.

---

## 👩‍💻 Author

**Wardah Zia Abbasi**
🔗 [GitHub: @war-abbasi](https://github.com/war-abbasi)

