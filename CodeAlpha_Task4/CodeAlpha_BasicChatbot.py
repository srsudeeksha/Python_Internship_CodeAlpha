"""
Basic Chatbot - CodeAlpha Task 4
A simple rule-based chatbot that responds to user inputs with predefined replies.

Author: Sannidhi Ranga Sudeeksha
Project: CodeAlpha Python Programming Internship
Task: Task 4 - Basic Chatbot
"""

import random
import re
from datetime import datetime

class BasicChatbot:
    """A simple rule-based chatbot class"""

    def __init__(self):
        """Initialize the chatbot with predefined responses"""

        self.responses = {
            'greetings': {
                'patterns': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
                'replies': [
                    "Hello! How can I help you today?",
                    "Hi there! Nice to meet you!",
                    "Hey! What's on your mind?",
                    "Hello! I'm here to chat with you!",
                    "Hi! Hope you're having a great day!"
                ]
            },
            'how_are_you': {
                'patterns': ['how are you', 'how do you do', 'how are things', 'whats up', "what's up"],
                'replies': [
                    "I'm doing great! Thanks for asking. How about you?",
                    "I'm fine, thanks! How are you doing?",
                    "All good here! How's your day going?",
                    "I'm doing well! What about yourself?",
                    "Great as always! How are you feeling today?"
                ]
            },
            'goodbye': {
                'patterns': ['bye', 'goodbye', 'see you', 'farewell', 'take care', 'exit', 'quit'],
                'replies': [
                    "Goodbye! Have a wonderful day!",
                    "See you later! Take care!",
                    "Bye! It was nice chatting with you!",
                    "Farewell! Come back anytime!",
                    "Take care! See you soon!"
                ]
            },
            'name': {
                'patterns': ['what is your name', 'whats your name', 'who are you', 'your name'],
                'replies': [
                    "I'm a basic chatbot created for the CodeAlpha internship!",
                    "You can call me ChatBot! I'm here to help.",
                    "I'm your friendly neighborhood chatbot!",
                    "I'm a simple AI assistant. Nice to meet you!"
                ]
            },
            'thanks': {
                'patterns': ['thank you', 'thanks', 'appreciate', 'grateful'],
                'replies': [
                    "You're welcome! Happy to help!",
                    "No problem at all!",
                    "Glad I could help!",
                    "Anytime! That's what I'm here for!"
                ]
            },
            'help': {
                'patterns': ['help', 'what can you do', 'commands', 'options'],
                'replies': [
                    "I can chat with you! Try saying hello, asking how I am, or saying goodbye.",
                    "I'm a simple chatbot. I can respond to greetings, questions about myself, and farewells!",
                    "I can have basic conversations. Try greeting me or asking about my name!"
                ]
            }
        }

        self.default_responses = [
            "I'm not sure I understand. Can you try rephrasing that?",
            "That's interesting! Tell me more about it.",
            "I'm still learning. Could you ask me something else?",
            "Hmm, I don't have a response for that. Try asking about something else!",
            "I'm a simple chatbot, so I might not understand everything. What else would you like to chat about?"
        ]

        self.log_file = "chat_log.txt"

    def preprocess_input(self, user_input):
        """Clean and preprocess user input"""
        processed = user_input.lower().strip()
        processed = re.sub(r'[^\w\s]', '', processed)
        return processed

    def find_response(self, user_input):
        """Find appropriate response based on user input"""
        processed_input = self.preprocess_input(user_input)
        for category, data in self.responses.items():
            for pattern in data['patterns']:
                if re.search(rf'\b{pattern}\b', processed_input):
                    return random.choice(data['replies'])
        return random.choice(self.default_responses)

    def log_chat(self, user_input, bot_response):
        """Save conversation to file"""
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"You: {user_input}\nBot: {bot_response}\n")

    def chat(self):
        """Main chat loop"""
        print("🤖 Basic Chatbot - CodeAlpha Task 4")
        print("=" * 40)
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Type 'bye', 'quit', or 'exit' to end the chat.")
        print("-" * 40)

        while True:
            user_input = input("\nYou: ").strip()
            if not user_input:
                print("Bot: Please say something! I'm here to chat.")
                continue
            if self.preprocess_input(user_input) in ['bye', 'goodbye', 'exit', 'quit']:
                response = self.find_response(user_input)
                print(f"Bot: {response}")
                self.log_chat(user_input, response)
                break
            response = self.find_response(user_input)
            print(f"Bot: {response}")
            self.log_chat(user_input, response)

def main():
    try:
        bot = BasicChatbot()
        bot.chat()
    except KeyboardInterrupt:
        print("\nBot: Goodbye! Thanks for chatting with me!")

if __name__ == "__main__":
    main()
