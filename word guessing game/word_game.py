# Hello. This is the first script I've ever written without any help from YouTube or anywhere else. It's a word guessing game. The computer guesses a word from the list in words.py and the game gives you the length of the word. Then it wants you to pick a letter and then it tells you if that letter is in the word; then adds that letter to another list and tells you the letters you've used.
# The game counts your tries. You get a clue every three tries but if you don't take clues, your tries gets subtracted by three. If you hit 12 tries, game is over.
# Please try to enter letters or words all lowercase.

import random
from words import words

play = input("Do you want to play or quit (y or q)? ").lower()
if play == "y":
    pass
elif play == "q":
    quit()

computer_word = random.choice(words)
print(f"The length of the word is {len(computer_word)}")
guess = ""
tries = 0
letters_used = []

while guess != computer_word:
    guess = input("Please enter a character or '-': ").lower()
    word_list = list(computer_word)

# Adds 1 to your tries and appends the letter you guessed to another list and shows them
    if guess in word_list:
        print(f"Yes, {guess} is in the word {word_list.count(guess)} times.")
        tries += 1
        letters_used.append(guess)
        print(f"You've used this letters: {letters_used}")
    else:
        print(f"No, {guess} is not in the word.")
        tries += 1  
        letters_used.append(guess)
        print(f"You've used this letters: {letters_used}")

    guess_the_word = input("Do you want to guess the word? ").lower()
    if guess_the_word == "yes":
        answer = input("What is your guess? ")
        if answer == computer_word:
            print("You've got it!")
            break
        elif answer != computer_word:
            print("No, the answer is not right.")
    elif guess_the_word == "no":
        pass

# The first clue gives you the first letter of the word that the computer chose 
    if tries == 3:
        clue = input("Do you want to have a clue? ")
        if clue.lower() == "yes":
            print(f"The first character is {word_list[0]}")
        elif clue.lower() == "no":
            tries -= 3
            pass 
    
    if tries == 6:
        clue = input("Do you want to have another clue? ")
        if clue.lower() == "yes":
            print(f"The second character is {word_list[1]}")
        elif clue.lower() == "no":
            tries -= 3
            pass 
    
    if tries == 9:
        clue = input("Do you want to have a final clue? ")
        if clue.lower() == "yes":
            print(f"The third character is {word_list[2]}")
        elif clue.lower() == "no":
            tries -= 3
            pass

# 15 tries, game over
    if tries == 15:
        print(f"You could not get the word correct. The word was {computer_word}")
        quit()
