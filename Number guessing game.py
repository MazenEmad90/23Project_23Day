number= 555
print("You have 5 attempts to guess the correct number.")
number_guessing=int(input("Guess a number: "))

attempts = 5
while number_guessing != number and attempts > 0:
    if number_guessing < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts -= 1
    if attempts > 1:
        print(f"You have {attempts} attempts left.")
    elif attempts == 1:
        print("This is your last attempt!")
    elif attempts == 0:
        print("Sorry, you've run out of attempts. The correct number was", number)
        break
    number_guessing = int(input("Guess a number: "))

if number_guessing == number:
    print("**Congratulations! You guessed the correct number.**".upper())
