import json
import re
import nltk

# Download the tokenizer if not already done
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

# Load intents from JSON
with open("intents.json", "r") as file:
    intents = json.load(file)

# Function to find matching intent
def get_intent_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):
                return intent["response"]

    return intents["fallback"]

# Main chatbot loop
def chatbot():
    print("University FAQ Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye! 👋")
            break
        response = get_intent_response(user_input)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
# chatbot.py - A simple FAQ chatbot for a university
# It uses intents defined in a JSON file to respond to user queries.