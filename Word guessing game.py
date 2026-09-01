import random

words = ['rainbow', 'computer', 'science', 'python', 'player']
word = random.choice(words)

guesses = set()
turns = 12

print("Guess the word!")

while turns > 0:
    display = [c if c in guesses else "_" for c in word]
    print(" ".join(display))

    if "_" not in display:
        print("You Win! The word was:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guesses:
        print("Already guessed!")
        continue

    guesses.add(guess)

    if guess not in word:
        turns -= 1
        print("Wrong! Turns left:", turns)

        if turns == 0:
            print("You Lose! The word was:", word)
