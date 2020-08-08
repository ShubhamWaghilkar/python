n = 18

nog = 1;
print("The 9 guess can be used while playing")

while (nog<=9):
    nog = nog + 1
    print("Enter the number")
    guess = int(input())

    if guess>18:
        print("Value to large take smaller number")

    elif guess == 15:
        print("You are close to the number")
        continue

    elif guess<18:
        print("Value is to Small take larger number")



    elif guess == 18:
        print("Congrats you guess the correct number")

        break

print("Number of guess you took ", nog )

if(nog>9):
    print(nog, "guess have been used \n game over")