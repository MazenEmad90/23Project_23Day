import random

current = 0
print("Welcome to 21 Number Game!")
print("Rules: You can say 1, 2, or 3 numbers in sequence. Whoever says 21 loses.")

while current < 21:
    move = int(input("How many numbers will you say (1, 2, or 3)? "))

    if move not in [1, 2, 3]:
        print("Invalid choice, try again.")
        continue

    for i in range(move):
        num = int(input("Enter your next number: "))

        if num != current + 1:
            print("You must enter the next number in sequence!")
            raise SystemExit

        current = num

        print("You:", current)
        if current == 21:
            print("You said 21. You lose!")
            raise SystemExit

    comp_move = random.randint(1, 3)
    print("Computer will say", comp_move, "numbers")
  
    for i in range(comp_move):
        current += 1
        print("Computer:", current)

        if current == 21:
            print("Computer said 21. Computer loses! You win!")
            raise SystemExit
