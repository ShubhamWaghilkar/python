import time

initial = time.time()

k=0
while (k<45):
    k +=1
    print("shubham waghilkar")
print(" Time taken for while : ",time.time() - initial,"seconds")

initial2 = time.time()
for i in range(30):
    print("shubham s waghilkar")
print("Time taken forloop : ", time.time() - initial2,"seconds")