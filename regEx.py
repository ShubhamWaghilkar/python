import re

str = """

HEllo my name is shubham my email is Waghilkarshubham@gmail.com
HEllo my name is shubham my email is Waghilkarshubham1@gmail.com
HEllo my name is shubham my email is Waghilkarshubham2@gmail.com
HEllo my name is shubham my email is Waghilkarshubham4@gmail.com




"""
str1 = """
My name is shubham my no. is 9967970409
My name is shubham my no. is 9967970401
My name is shubham my no. is 9967970402
My name is shubham my no. is 9967970403
My name is shubham my no. is 9967970404

"""

list2 = re.findall(r'\w+\d[10]+\w',str1)
op1 = open("number.txt","a")
k = 0
for i in list2:
    op1.write(f"Numbers are:  {k}: {i} \n")
    k = k+1
op1.close()
print(f"Number are : {list2}")

list1 = re.findall(r'\w+@\S+\w',str)

op = open("email.txt","a")

j =0
for i in list1:
    op.write(f"Email: {j}{i}\n ")
    j = j+1
op.close()

print(f"Emails are :{list1}")
print(f"Total Emails are: {j}")