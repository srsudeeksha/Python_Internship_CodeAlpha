# 🎮 Hangman Game - CodeAlpha Task 1

A classic text-based word guessing game with ASCII art hangman drawings.

## 🎯 Project Overview
This project was developed as part of the **CodeAlpha Python Programming Internship - Task 1**.

## ✨ Features
- 5 predefined words for guessing
- Visual ASCII art hangman progression
- 6 maximum wrong guesses
- Input validation and error handling
- Play again functionality
- Clear game state display
- Instructions for new players

## 🔧 Key Concepts Used
- **random** - Random word selection
- **while loops** - Game loop logic
- **if-else statements** - Conditional logic
- **strings** - Word manipulation
- **lists** - Word storage and guessed letters
- **Object-oriented programming** - Game class structure

## 🚀 How to Run
```bash
python hangman_game.py
```

## 🎮 How to Play
1. A random word is selected from the predefined list
2. Guess one letter at a time
3. Correct guesses reveal letters in the word
4. Wrong guesses add parts to the hangman drawing
5. Win by guessing all letters before the drawing completes
6. You have 6 wrong guesses before losing

## 📋 Game Features
- **Word Progress Display**: Shows guessed letters and remaining blanks
- **Available Letters**: Shows which letters haven't been guessed
- **Visual Hangman**: ASCII art shows game progress
- **Input Validation**: Prevents invalid inputs
- **Game Statistics**: Shows number of guesses when winning

## 🎨 Sample Gameplay
```
🎮 HANGMAN GAME - CodeAlpha Task 1
==================================================
Word: P _ T H O N
Letters guessed: P, O, H, T
Wrong guesses: 1/6
Available letters: A,B,C,D,E,F,G,I,J,K,L,M,N,Q,R,S,U,V,W,X,Y,Z

Enter a letter: Y
✅ Good guess! 'Y' is in the word!
```

## 🎯 Technical Implementation
- **Object-oriented design** with comprehensive HangmanGame class
- **Input validation** prevents invalid characters and repeated guesses
- **Screen clearing** for clean interface updates
- **Random word selection** from predefined list
- **Game state management** tracks progress and win/loss conditions

## 📁 Files
- `CodeAlpha_HangmanGame.py` - Main game implementation
- `Readme.md` - Project documentation

## 🏆 CodeAlpha Requirements Met
✅ Simple text-based game  
✅ Player guesses word one letter at a time  
✅ 5 predefined words used  
✅ Limited to 6 incorrect guesses  
✅ Basic console input/output  
✅ Uses random, while loop, if-else, strings, lists  

## 👨‍💻 Author
**CodeAlpha Python Programming Intern**

## 📧 Contact
- GitHub: https://github.com/srsudeeksha/Python_Internship_CodeAlpha/tree/main/CodeAlpha_Task1
- LinkedIn: www.linkedin.com/in/ranga-sudeeksha

---
*This project is part of the CodeAlpha Python Programming Internship program.*
