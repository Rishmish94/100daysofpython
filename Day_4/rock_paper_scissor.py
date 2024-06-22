import random
RPS = ["Rock", "Paper", "Scissor"]
user_input = input("Enter you choice out of Rock , Paper, Scissor : -  ")
random_choice = RPS[random.randint(0,2)]
print(f"You entered {user_input} and computer entered  {random_choice}")

if user_input == random_choice :
    print("Game is Draw")
else :
    if (user_input == "Rock" and random_choice == "Paper") or (user_input == "Scissor" and random_choice == "Rock") or (user_input == "Paper" and random_choice == "Scissor") :
        print("Computer wins the game")
    else :
        if (user_input == "Paper" and random_choice == "Rock") or (user_input == "Rock" and random_choice == "Scissor") or (user_input == "Scissor" and random_choice == "Paper") :
            print("You win the Game")
        else :
            print("You have entered a wrong choice")