"""
As a creative thing
- I put color helps as well and the user input is blue
- It chooses a random word from a file
 
"""

import os, time, random

clear = ""
if os.name == "nt":
    clear = "cls"
else:
    clear = "clear"

words = []
with open("words.txt", "r") as f:
    for l in f:
        try:
            words.append(l.split()[0])
        except:
            pass
word = words[random.randint(0, len(words))]
hints = [" _ " for i in range(len(word))]
old_hints = []
is_over = False
count = 0

while not is_over:
    os.system(clear)
    print(f"Welcome to the word game\nGuesses: {count}")
    for i, h in enumerate(old_hints):
        if i % len(word) == len(word)-1 and i > 0:
            print(h)
        else:
            print(h, end="")
    
    print(f"\nlast hint is", end="")
    for h in hints:
        print(h, end="")
    print()
    hints = [" _ " for i in range(len(word))]
    guess = input("make a guess: \033[94m")
    print("\033[0m")
    count += 1
    if len(guess) != len(word):
        print(f"the guess must be have {len(word)} letters")
        time.sleep(1.5)
        continue
    
    if guess.lower() == word:
        is_over = True
    
    for i, l in enumerate(guess):        
        if l in word:
            if word[i] == guess[i]:
                hints[i] = " \033[92m"+l.upper()+"\033[0m "
            else:
                hints[i] = " \033[93m"+l.lower()+"\033[0m " 
        else:
            hints[i] = " \033[91m"+l.lower()+"\033[0m "
        old_hints.append(hints[i])
    

print(f"The word was: \033[92m{word}\033[0m good job, it took you {count} guesses ")
