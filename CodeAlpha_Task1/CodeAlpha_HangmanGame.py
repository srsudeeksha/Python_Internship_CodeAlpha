"""
Hangman Game - CodeAlpha Task 1
A text-based word guessing game where players have 6 attempts to guess a secret word.

Author: [Your Name]
Project: CodeAlpha Python Programming Internship
Task: Task 1 - Hangman Game
"""

import random
import os
import sys

class HangmanGame:
    """A complete Hangman game implementation"""
    
    def __init__(self):
        """Initialize the game with predefined words and hangman drawings"""
        
        # Predefined list of 5 words (as per requirements)
        self.words = [
            "PYTHON",
            "CODING",
            "COMPUTER",
            "HANGMAN",
            "PROGRAMMING"
        ]
        
        # Hangman drawings for each wrong guess (0-6)
        self.hangman_drawings = [
            # 0 wrong guesses
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            # 1 wrong guess
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            # 2 wrong guesses
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            # 3 wrong guesses
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            # 4 wrong guesses
            """
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            =========
            """,
            # 5 wrong guesses
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            =========
            """,
            # 6 wrong guesses (game over)
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            =========
            """
        ]
        
        # Game state variables
        self.secret_word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        self.game_over = False
        self.won = False
    
    def clear_screen(self):
        """Clear the console screen for better display"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def choose_word(self):
        """Randomly select a word from the predefined list"""
        self.secret_word = random.choice(self.words).upper()
        return self.secret_word
    
    def display_word(self):
        """Display the current state of the word with guessed letters"""
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()
    
    def display_game_state(self):
        """Display the complete game state"""
        self.clear_screen()
        
        print("🎮 HANGMAN GAME - CodeAlpha Task 1")
        print("=" * 50)
        
        # Display hangman drawing
        print(self.hangman_drawings[self.wrong_guesses])
        
        # Display word progress
        print(f"Word: {self.display_word()}")
        print(f"Letters guessed: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print(f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong_guesses}")
        
        # Display remaining letters
        remaining_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - self.guessed_letters
        print(f"Available letters: {', '.join(sorted(remaining_letters))}")
        print("-" * 50)
    
    def get_user_guess(self):
        """Get and validate user input"""
        while True:
            guess = input("Enter a letter (or 'quit' to exit): ").upper().strip()
            
            # Check for quit command
            if guess.lower() == 'quit':
                return 'QUIT'
            
            # Validate input
            if len(guess) != 1:
                print("❌ Please enter only one letter!")
                continue
            
            if not guess.isalpha():
                print("❌ Please enter only letters!")
                continue
            
            if guess in self.guessed_letters:
                print(f"❌ You already guessed '{guess}'. Try another letter!")
                continue
            
            return guess
    
    def make_guess(self, letter):
        """Process a letter guess"""
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            print(f"✅ Good guess! '{letter}' is in the word!")
            
            # Check if word is complete
            if all(letter in self.guessed_letters for letter in self.secret_word):
                self.won = True
                self.game_over = True
        else:
            print(f"❌ Sorry! '{letter}' is not in the word.")
            self.wrong_guesses += 1
            
            # Check if game is over
            if self.wrong_guesses >= self.max_wrong_guesses:
                self.game_over = True
        
        input("\nPress Enter to continue...")
    
    def display_game_over(self):
        """Display game over screen"""
        self.clear_screen()
        
        print("🎮 HANGMAN GAME - GAME OVER")
        print("=" * 50)
        
        # Final hangman drawing
        print(self.hangman_drawings[self.wrong_guesses])
        
        if self.won:
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"You guessed the word: {self.secret_word}")
            print(f"It took you {len(self.guessed_letters)} guesses!")
        else:
            print("💀 GAME OVER! YOU LOST! 💀")
            print(f"The word was: {self.secret_word}")
            print("Better luck next time!")
        
        print("=" * 50)
    
    def play_again(self):
        """Ask if player wants to play again"""
        while True:
            choice = input("Do you want to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
    
    def reset_game(self):
        """Reset game state for a new round"""
        self.secret_word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False
    
    def display_instructions(self):
        """Display game instructions"""
        self.clear_screen()
        print("🎮 HANGMAN GAME - INSTRUCTIONS")
        print("=" * 50)
        print("📝 How to Play:")
        print("• A secret word will be chosen randomly")
        print("• Guess one letter at a time")
        print("• You have 6 wrong guesses before losing")
        print("• Win by guessing all letters in the word")
        print("• Type 'quit' anytime to exit the game")
        print("\n💡 Tips:")
        print("• Start with common vowels (A, E, I, O, U)")
        print("• Try common consonants (R, S, T, L, N)")
        print("• Pay attention to word length and patterns")
        print("=" * 50)
        input("Press Enter to start the game...")
    
    def play(self):
        """Main game loop"""
        print("🎮 Welcome to Hangman Game!")
        print("CodeAlpha Task 1 - Python Programming")
        
        # Show instructions
        show_instructions = input("\nWould you like to see instructions? (y/n): ").lower().strip()
        if show_instructions in ['y', 'yes']:
            self.display_instructions()
        
        while True:
            # Reset game state
            self.reset_game()
            
            # Choose a random word
            self.choose_word()
            
            print(f"\n🎯 A new word has been chosen! ({len(self.secret_word)} letters)")
            input("Press Enter to start guessing...")
            
            # Main game loop
            while not self.game_over:
                # Display current game state
                self.display_game_state()
                
                # Get user guess
                guess = self.get_user_guess()
                
                # Check for quit
                if guess == 'QUIT':
                    print("\n👋 Thanks for playing! Goodbye!")
                    return
                
                # Process the guess
                self.make_guess(guess)
            
            # Display game over screen
            self.display_game_over()
            
            # Ask to play again
            if not self.play_again():
                print("\n👋 Thanks for playing Hangman! Goodbye!")
                break

def display_game_info():
    """Display project information"""
    print("\n" + "=" * 60)
    print("PROJECT INFORMATION")
    print("=" * 60)
    print("Project: Hangman Game")
    print("Task: CodeAlpha Task 1")
    print("Description: Text-based word guessing game")
    print("Features:")
    print("• 5 predefined words")
    print("• 6 maximum wrong guesses")
    print("• ASCII art hangman drawings")
    print("• Input validation and error handling")
    print("• Play again functionality")
    print("• Clear game state display")
    print("Key Concepts: random, while loop, if-else, strings, lists")
    print("=" * 60)

def main():
    """Main function to start the hangman game"""
    try:
        # Display project info
        display_game_info()
        
        # Create and start game
        game = HangmanGame()
        game.play()
        
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted! Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the game.")

if __name__ == "__main__":
    main()