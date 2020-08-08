import random

user_score = 0
comp_score = 0
play_count = 0
print("LET'S PLAY STONE PAPER SICSSORS")
opt = ["s","p","r"]

for i in range(4):
    play_count +=1
    computer_turn = random.choice(opt)
    user_turn = input("Choose your options :\n s-Stone \n p=Paper \n r-sicssor \n")
    if user_turn == 's' or user_turn == 'S':
        if computer_turn == "p":
            print("Computer Outcome \n", computer_turn)
            comp_score +=1
            print("Ahh you loose")
        elif computer_turn == "r":
            print("Computer Outcome \n",computer_turn)
            user_score +=1
            print("You winn this time")
        else:
            print("Computer Outcome \n",computer_turn)
            print("woah its tie")
    elif user_turn == "r" or user_turn== "R":
        if computer_turn == "p":
            user_score += 1
            print("Computer Outcome \n", computer_turn)
            print("You winn this time")
        elif computer_turn == "s":
            comp_score +=1
            print("Computer Outcome \n", computer_turn)
            print("Ahh you loose")
        else:
            print("Computer Outcome \n", computer_turn)
            print("woah its tie")
    elif user_turn == "p" or user_turn == "p":
        if computer_turn == "s":
            user_score +=1
            print("Computer Outcome \n", computer_turn)
            print("you win this time")
        elif computer_turn == "r":
            comp_score += 1
            print("Computer Outcome \n", computer_turn)
            print("Ahh You loose")
        else:
            print("Computer Outcome \n", computer_turn)
            print("woah its tie")
    else:
        print("Invalid input choose from above")

print("*" * 30)
if(comp_score > user_score):
    print("Loser")
    a = f"Computer score : {comp_score} \nYour Score : {user_score}"
    print(a)
elif(user_score > comp_score):
    print("Winner")
    a = f"Computer score : {comp_score} \nYour Score : {user_score}"
    print(a)
      # print("Your score : ", user_score )
    # print("Computer score : ", comp_score)
else:
    print("SHOCKED, IT'S TIE")