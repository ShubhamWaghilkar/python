print("Enter Number 1")
num1 = (input())
print("Enter Number 2")
num2 = (input())

try:
    print(int(num1) + int(num2))
except Exception as e:
    print(e)


print("This is important")
