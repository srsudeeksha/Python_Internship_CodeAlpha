# 🤖 Basic Chatbot - CodeAlpha Task 4

A rule-based conversational chatbot with intelligent pattern matching and varied responses.

## 🎯 Project Overview
This project was developed as part of the **CodeAlpha Python Programming Internship - Task 4**.

## ✨ Features
- **Intelligent Pattern Matching** - Recognizes various greeting patterns
- **Multiple Response Variations** - Random selection for natural conversations
- **Input Preprocessing** - Handles different cases and punctuation
- **Conversation Categories** - Greetings, questions, thanks, help, and farewells
- **Graceful Exit Handling** - Polite goodbye messages
- **Demo Mode** - Test responses without interactive chat
- **Error Recovery** - Handles unexpected inputs gracefully

## 🔧 Key Concepts Used
- **if-elif statements** - Conditional response logic
- **Functions** - Modular code organization
- **Loops** - Conversation flow control
- **Input/Output** - User interaction
- **Object-oriented programming** - Chatbot class structure
- **Regular expressions** - Text preprocessing
- **Random selection** - Response variation

## 🚀 How to Run
```bash
python basic_chatbot.py
```

## 💬 Conversation Categories

### 🙋‍♂️ Greetings
**Patterns:** hello, hi, hey, good morning, good afternoon, good evening
**Sample Responses:**
- "Hello! How can I help you today?"
- "Hi there! Nice to meet you!"
- "Hey! What's on your mind?"

### 🤔 How Are You
**Patterns:** how are you, how do you do, what's up
**Sample Responses:**
- "I'm doing great! Thanks for asking. How about you?"
- "I'm fine, thanks! How are you doing?"
- "All good here! How's your day going?"

### 👋 Farewells
**Patterns:** bye, goodbye, see you, farewell, take care, exit, quit
**Sample Responses:**
- "Goodbye! Have a wonderful day!"
- "See you later! Take care!"
- "Bye! It was nice chatting with you!"

### 🏷️ Identity Questions
**Patterns:** what is your name, who are you
**Sample Responses:**
- "I'm a basic chatbot created for the CodeAlpha internship!"
- "You can call me ChatBot! I'm here to help."

### 🙏 Thanks
**Patterns:** thank you, thanks, appreciate
**Sample Responses:**
- "You're welcome! Happy to help!"
- "No problem at all!"
- "Glad I could help!"

### ❓ Help
**Patterns:** help, what can you do, commands
**Sample Responses:**
- "I can chat with you! Try saying hello, asking how I am, or saying goodbye."
- "I'm a simple chatbot. I can respond to greetings, questions about myself, and farewells!"

## 🎮 Sample Conversation
```
🤖 Basic Chatbot - CodeAlpha Task 4
========================================
Hello! I'm a simple chatbot. Type 'bye' or 'quit' to exit.
Try saying: hello, how are you, what's your name, help, thanks, or goodbye
----------------------------------------

You: Hello there!
Bot: Hi there! Nice to meet you!

You: How are you doing today?
Bot: I'm doing great! Thanks for asking. How about you?

You: What's your name?
Bot: I'm a basic chatbot created for the CodeAlpha internship!

You: Thanks for chatting!
Bot: You're welcome! Happy to help!

You: Goodbye
Bot: Goodbye! Have a wonderful day!
```

## 🧪 Demo Mode
The chatbot includes a demo mode that shows sample responses for testing:

```
🧪 DEMO MODE - Testing Chatbot Responses
=============================================
Input: Hello
Response: Hello! How can I help you today?
------------------------------
Input: How are you?
Response: I'm fine, thanks! How are you doing?
------------------------------
Input: What's your name?
Response: I'm a basic chatbot created for the CodeAlpha internship!
```

## 🛡️ Input Handling
- **Case insensitive** - Works with any capitalization
- **Punctuation removal** - Handles various punctuation marks
- **Empty input validation** - Prompts for valid input
- **Exit command recognition** - Multiple ways to quit
- **Unknown input handling** - Graceful responses to unrecognized patterns

## 🔄 Response Variation
The chatbot uses random selection from multiple response options to make conversations feel more natural and engaging.

## 🏆 CodeAlpha Requirements Met
✅ Rule-based chatbot implementation  
✅ Responds to "hello", "how are you", "bye"  
✅ Predefined replies for each input type  
✅ Uses if-elif, functions, loops, input/output  

## 🎯 Technical Implementation
- **Object-oriented design** with comprehensive BasicChatbot class
- **Pattern matching system** using string operations
- **Response categorization** for organized reply management
- **Input preprocessing** for robust text handling
- **Conversation flow control** with proper exit handling

## 📁 Files
- `basic_chatbot.py` - Main chatbot implementation
- `README.md` - Project documentation

## 👨‍💻 Author
**CodeAlpha Python Programming Intern**

## 📧 Contact
- GitHub: https://github.com/srsudeeksha/Python_Internship_CodeAlpha/tree/main/CodeAlpha_Task4
- LinkedIn: www.linkedin.com/in/ranga-sudeeksha

---
*This project is part of the CodeAlpha Python Programming Internship program.*
