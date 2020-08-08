dict1 = {i:f"item{i}" for i in range(5)}
print(dict1)

#genrator
#special kinds of iterator
evens = (i for i in range(100) if i%2==0)
print(evens)
for item in evens:
    print(item)

user = (input("Enter number of items"))
u2 = input("which coprehension you want \n "
           "1:set \n 2:list \n 3:dict")





if u2 == "set":
    set = {i for i in range(user)}
    print(set)
elif u2 == "dict":
    i = 1
    set = {i:f"Your Number{i}" for i in range(1,user)}
    print(set)
elif u2 == "list":
    set = [i for i in range(user)]
    print(set)