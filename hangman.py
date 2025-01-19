# Import the random module to randomly select a word
import random 

# Define different stages of the hangman game based on the number of lives remaining
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Display the logo of the game
logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                      
                   |___/    
'''

# List of words for the game
word_list = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 
    'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar',
    'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb',
    # Add other words...
]

# Initial number of lives
lives = 6

# Display the logo when the game starts
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # For debugging (to see the chosen word)

# Initialize the placeholder for displaying the word as underscores
placeholder = ""
word_length = len(chosen_word)

# Create an underscore placeholder for each letter in the word
for position in range(word_length):
    placeholder += "_"

# Print the placeholder (the word to guess)
print("Word to guess: " + placeholder)

# Initialize game variables
game_over = False
correct_letters = []  # List to store letters that have been correctly guessed

# Main game loop
while not game_over:
    # Display remaining lives and ask for user input
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()  # Convert guess to lowercase

    # Check if the user has already guessed the letter
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    display = ""  # Placeholder for the current word being guessed

    # Build the word display by checking the guessed letters
    for letter in chosen_word:
        if letter == guess:
            display += letter  # If the letter matches, display it
            correct_letters.append(guess)  # Add the guessed letter to correct_letters
        elif letter in correct_letters:
            display += letter  # If the letter has already been guessed, display it
        else:
            display += "_"  # Display an underscore for unguessed letters

    # Show the current state of the word
    print("Word to guess: " + display)

    # If the guess is incorrect, decrease lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        # If no lives are left, game over
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # If all letters have been guessed, the player wins
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display the current hangman stage based on the number of lives remaining
    print(stages[lives])
