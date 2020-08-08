import random
user_sco = 0
comp_scp = 0
option = ["snake","water","gun"]
n =0

while n<5:
    n +=1
    com_turn = random.choice(option)
    user = input("Enter from choice \n1:Snake \n2:Water \n3:gun \n")
    if user == "snake" or user== "SNAKE" or user== "Snake":
        if com_turn == "gun":
            print("You Lost")
            comp_scp +=1
            print("computer has : ",com_turn)
        elif com_turn == "water":
            print("You winn round")
            print("computer has : ", com_turn)
            user_sco +=1
        else:
            print("Its a tie")
            print("computer has : ", com_turn)
    elif user == "gun" or user == "GUN" or user == "Gun":
        if com_turn == "snake":
            user_sco +=1
            print("You Winn this round")
            print("computer has : ", com_turn)
        elif com_turn == "water":
            comp_scp +=1
            print("You lost")
            print("computer has : ", com_turn)
        else:
            print("its a tie")
            print("computer has : ", com_turn)
    elif user == "water" or user == "Water" or user == "WATER":
        if com_turn == "snake":
            com_turn+=1
            print("You lost")
            print("computer has : ", com_turn)
        elif com_turn == "gun":
            user_sco +=1
            print("You winn this round")
            print("computer has : ", com_turn)
        else:
            print("Its a tie")
            print("computer has : ", com_turn)
    else:
        print("Invalid input choose from below options")
print("*" * 40)
if (comp_scp> user_sco):
    print("Losser")
    a = f"You Scored {user_sco} \nComputer Scored {comp_scp}"
    print(a)
elif(user_sco>comp_scp):
    print("WINNER")
    a = f"You Scored {user_sco} \nComputer Scored {comp_scp}"
    print(a)
else:
    print("Shocked its a tie")