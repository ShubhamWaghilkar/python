# numbers =["34","55","345","100"]
#
# fum = int(numbers)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# numbers[2] = numbers[2]+1
# print(numbers[2])


def sq(a):
    return a*a

def cube(a):
    return a*a*a


def four(a):
    return a*a*a*a




num1 = [2,34,545,3,32,2]


a = list(map(sq,num1))
print(a)


b = list(map (lambda x:x*x*x,num1))
print(b)

print("*" * 50)

funt = [sq,cube,four]

for i in range(5):
     val = list(map(lambda x:x(i),funt))
     print(val)

print("*"*40)
#################  FILTER #################################

list1 = [1,2,3,4,5,6,7,8,9]

def isgret(num):
    return num>5

great = list(filter(isgret,list1))
print(f"for filter {great}")
############################  REDUCE #################################
from functools import reduce

list3 = [3,4,56,34]
# num = 0
# for i in list3:
#     num = num + i
# print(f"The Reduce function works in  {num} ")

num = reduce(lambda x,y:x+y, list3)
print(f" Reduce function {num}")

sli = "shubham"
print(sli[0:5])


