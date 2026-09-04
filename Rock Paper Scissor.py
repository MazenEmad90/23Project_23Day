import random

choices = ["Rock", "Paper", "Scissors"]

print("Welcome to Rock-Paper-Scissors!\n")

while True:
    try:
        choice = int(input("1-Rock  \n2-Paper  \n3-Scissors\nEnter your choice (1-3): "))
        if choice not in [1,2,3]: 
            print("Please enter 1, 2 or 3.")
            continue
    except ValueError:
        print("Invalid input, numbers only.")
        continue

    user = choices[choice-1]
    comp = random.choice(choices)

    print(f"You: {user} | Computer: {comp}")

    if user == comp:
        print("Tie!")
    elif (user=="Rock" and comp=="Scissors") or \
         (user=="Paper" and comp=="Rock") or \
         (user=="Scissors" and comp=="Paper"):
        print("You Win!")
    else:
        print("Computer Wins!")

    while True:
        ans = input("Play again? (Y/N): ").lower()
        if ans in ['y','n']:
            break
        print("Please enter Y or N.")

    if ans == 'n':
        break

print("Thanks for playing!")
