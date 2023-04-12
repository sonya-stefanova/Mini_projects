import hangman_art
import random
import hangman_words
from hangman_stages import stages

#We accept it is not the end of the game
print("Welcome To The Hangman Challenger!!!")
logo = hangman_art.logo
print(logo)
end_of_game = False
#We create a list of all possible words which are fruits in this case
fruits = hangman_words.list_of_fruits
#This is the code for a random choose of a fruit
chosen_fruit = random.choice(fruits)

word_length = len(chosen_fruit)

#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Create blanks or underscores that will be replaced with the letters at a later stage in a list
# so we can easily iterate through it and replace the blanks

displayed_word = []
for _ in range(word_length):#fill it with as many _ as the letters are
    displayed_word += "_"

#guess letters until the game end
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check if each letter in the word is equal to the guess when iterating through the chosen fruit:
    for i in range(len(chosen_fruit)):
        if chosen_fruit[i] == guess:
            displayed_word[i] = chosen_fruit[i]

    #If guess is not a letter in the chosen_fruit,
    #Then reduce 'lives' by 1.
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_fruit:
        print(f"What a pity! You guessed {guess} which is not in the word.You've just losen a life! ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(displayed_word)}")

    #Check if user has got all letters.
    if "_" not in displayed_word:
        end_of_game = True
        print("You win.")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])