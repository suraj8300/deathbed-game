# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random

def check_life():
    if lives == 6:
        live_art = life6
    elif lives == 5:
        live_art = life5
    elif lives == 4:
        live_art = life4
    elif lives == 3:
        live_art = life3
    elif lives == 2:
        live_art = life2
    elif lives == 1:
        live_art = life1
    elif lives == 0:
        live_art = display_death_message(user_name, birth_date)
    return live_art

print("""
    _            _   _     _              _ 
    | |          | | | |   | |            | |
  __| | ___  __ _| |_| |__ | |__   ___  __| |
 / _` |/ _ \/ _` | __| '_ \| '_ \ / _ \/ _` |
| (_| |  __/ (_| | |_| | | | |_) |  __/ (_| |
 \__,_|\___|\__,_|\__|_| |_|_.__/ \___|\__,_|
                                             
                                             
""")

life6 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
"""
print(life6)

life5 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
"""
life4 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""
life3 = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""
life2 = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""
life1 = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""

from datetime import datetime

def display_death_message(user_name, birth_date):
    # Set the current date
    current_date = datetime.now().strftime("%d/%m/%Y")
    
    # Prepare the ASCII art with placeholders
    death_message = f'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
         /"""""/""""""""""""".
        /     /               \             __
       /     /                 \            ||
      /____ /                   \           ||
     |     |       In Loving     |          ||
     |     |        Memory       |          ||
     |     |  {user_name.center(17)}  |          ||
     |     |{birth_date[0]}{birth_date[1]}/{birth_date[2]}{birth_date[3]}/{birth_date[4]}{birth_date[5]}{birth_date[6]}{birth_date[7]}-{current_date}|          ||
     |     |       * *   * *     |         _||_
     |     |       *\/* *\/*     |        | TT |
     |     |       *_\_  /    ..."""""""""| || |.""...."""""""".""
     |     |           \/.."""""..."""""""\ || /.""".......""""...
     |     |......"""""""........""""""""""^^^^"......."""""""".."
     |......"""""""""""""""""........"""""...."""""..""""""""""...

    '''
    return death_message

# Usage example
display_death_message("John Doe", "01/01/2000")

    

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lives = 6

computer_list = []
for i in range(5):
    computer_word = random.choice(alphabet)
    computer_list.append(computer_word)
    
print(computer_list)
guess = ['_','_','_','_','_']

user_name = input("Enter your name: ")
birth_date = (input("Enter your date of birth in dd/mm/yyyy format: "))
while lives > 0:
    
    
    
    print(f"Word to guess: {guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}")
    user_guess = input("Guess a letter: ")
    
    if user_guess in computer_list:
        
        for i in range(5):
            if user_guess == computer_list[i]:
                guess[i] = user_guess
                
        print(f"{guess[0]} {guess[1]} {guess[2]} {guess[3]} {guess[4]}")
        
        if "_" not in guess:
            print(f"********** YOU WON SCORE: {lives} **********")
        
        print(check_life())
        print(f"********** {lives}/6 Lives Left **********")
        
    else:
        
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(check_life())
    if lives == 0:
        print("********** GAME OVER: YOU'RE DEAD **********")