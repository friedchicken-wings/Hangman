#AL, CM, Hangman 3
import random
words = ["Chicken", "Maruchan", "Noodles", "Tacos", "Pasta", "Steak", "Lasagna", "Fries"]
word = random.choice(words)
max_attempts = 8
display = ""
loss = 1
if loss == 1: #all the hang mans and prints if loss condition is met
        print('''             --------
             |      |
             |
             |
             |  
             |
             --------''')
elif loss == 2:
        print(
        '''--------
   |      |
   |      O
   |
   |
   |
   --------''')
elif loss == 3:
        print('''
   --------
   |      |
   |      O
   |      |
   |
   |
   --------''')
elif loss == 4:
        print('''--------
   |      |
   |      O
   |     <|
   |     
   |
   --------''')


elif loss == 5:
        print( '''--------
   |      |
   |      O
   |      |
   |      |
   |    
   --------''')
elif loss == 6:
        print('''--------
   |      |
   |      O
   |     <| 
   |      |
   |
   --------''')
elif loss == 7:
        print('''--------
   |      |
   |      O
   |     <|>
   |      |
   |     /
   --------''')
elif loss == 8:
        print('''--------
   |      |
   |      O
   |     <|>
   |      |
   |     / \
   --------''')

def draw_hangman(attempts):
    print(display[max_attempts - attempts])
wrong = 0
curr = []
let_list = []
guess = input("Give me a letter.").lower()
for i in range(len(word)):
    curr.append("_")

if guess not in words:
    wrong += 1

while True:
    if "_" in curr:
        guess = input("Give me a letter.").lower()

        if guess not in word:
            wrong += 1
            print("Oops! You got it wrong. Try again")

            for letter in word:
                if letter in let_list:
                    display += letter
        else:
            display += "_"
    print(display)

    if display == word:
        print("You won!")
        break

for letter in word:
   if letter in word:
       curr += letter
else:
    curr += "_"