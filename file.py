# file io basic
import datetime
import time

f = open("shubham.txt", "rt")

for line in f:
    print(line)


f.close()


def wr(file,text):
    f = open(file,"a")
    f.write(text)

wr('star.txt','helloworld')