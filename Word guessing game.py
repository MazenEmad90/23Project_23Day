import random

words = ["apple","banana","mango","orange","grapes","papaya"]
word = random.choice(words)
guessed, wrong, max_attempts = set(), 0, 6

hangman = [
"-----\n|   |\n    |\n    |\n    |\n=========",
"-----\n|   |\n O  |\n    |\n    |\n=========",
"-----\n|   |\n O  |\n|   |\n    |\n=========",
"-----\n|   |\n O  |\n/|\\ |\n    |\n=========",
"-----\n|   |\n O  |\n/|\\ |\n/   |\n=========",
"-----\n|   |\n O  |\n/|\\ |\n/ \\ |\n========="
]

print("Welcome to Hangman!\nHint: The word is a fruit.")

while wrong < max_attempts:
    display = ' '.join(c if c in guessed else '_' for c in word)
    print(hangman[wrong], "\nWord:", display)

    if '_' not in display: print("You Win!\nThe word was:", word); break
    g = input("Guess a letter: ").lower()

    if len(g)!=1 or not g.isalpha() or g in guessed: print("Invalid/duplicate"); continue
    guessed.add(g)

    if g in word: print("Correct!")
    else: wrong+=1; print("Wrong!")
else:
    print("Game Over!\nThe word was:", word)
