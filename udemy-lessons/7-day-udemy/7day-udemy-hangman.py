import random
import os
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

lives = 6

display = []

for _ in chosen_word:
    display.append("_")

end_of_game = False

print(logo)
print(f"Your word: {' '.join(display)}")

while not end_of_game:
    guess = str.lower(input("Guess a letter: "))

    os.system('cls') #notīra termināli

    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, it's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])