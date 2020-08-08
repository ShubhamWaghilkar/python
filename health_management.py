import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input(" SHUBHAM SCHEDULE \n Enter 1 for exercise and 2 for food \n"))
        if(c==1):
            value = input("Type here \n")
            with open ("shubhamexercise.txt","a") as s:
                s.write(str([str(gettime())])+":" +value+ "\n")
                print("successfully written")
        elif(c==2):
            value = input("type here \n")
            with open("shubhamfood.txt","a") as s:
                s.write(str([str(gettime())])+":" +value+ "\n")
                print("successfully written")
    elif k==2:
        c = int(input(" VAISHNAVI SCHEDULE \n Enter 1 for exercise and 2 for food"))
        if(c==1):
            value = input("Type here \n")
            with open("vaishnaviexercise.txt","a") as s:
                 s.write(str([str(gettime())])+":" +value+ "\n")
                 print("successfull written")
        elif(c==2):
            value = input("Type here \n")
            with open("vaishnavifood.txt","a") as s:
                s.write(str([str(gettime())])+":" +value+ "\n")
                print("Successfully written")
    else:
        print("invalid input entered")

def ret(k):
    if k==1:
        c = int(input(" SHUBHAM SCHEDULE \n Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("shubhamexercise.txt") as s:
                for i in s:
                    print(i,end="")
        elif(c==2):
            with open("shubhamfood.txt") as s:
                for i in s:
                    print(i,end="")
    elif k==2:
        c = int(input(" VAISHNAVI SCHEDULE \n Enter 1 for exercise and 2 for food"))
        if (c == 1):
            with open("vaishnaviexercise.txt.txt") as s:
                for i in s:
                    print(i, end="")
        elif (c == 2):
            with open("vaishnavifood.txt") as s:
                for i in s:
                    print(i, end="")
    else:
        print("Invalid input entered")

print("HEALTH MANAGEMENT SYSTEM")

a= int(input("press 1 for log the value and 2 for retreive the value \n "))

if a == 1:
    b = int(input("Enter 1(shubham), Enter 2(vaishnavi) \n"))
    take(b)
else:
    b = int(input("Enter 1(shubham) , Enter 2(vaishnavi) \n"))
    ret(b)