import random
from hangman_words import word_list


lives = 6


from hangman_art import stages
chosen_word = random.choice(word_list)



word_length = len(chosen_word)
placeholder="_"*len(chosen_word)

print("Word to guess: " + placeholder)

game_over = False

guess_words = []
display = list(placeholder)
while not game_over:
   print(f"****************************<???>{lives}/6 LIVES LEFT****************************")
   guess = input("Guess a letter: ").lower()
   life_exists = False
   if guess in guess_words:
       print(f"You have already guessed the letter {guess}")
       print("".join(display))
       life_exists = True
   else:
     for index,letter in enumerate(chosen_word):


       if  letter == guess:
           guess_words.append(letter)
           display[index] = letter
           life_exists=True
     print("".join(display))

   if not life_exists:
       if lives==0:
           game_over = True
           print(stages[0])
           print(f"***********************YOU LOSE**********************")
       else:
           print("The letter you guessed is not in the word.You lose a life")
           print(stages[lives])
           lives=lives-1
           print("".join(display))



   if "_" not in display:
       game_over = True

       print("****************************YOU WIN****************************")



