# def convert(str1):
#
#     if str1[-2:]=="AM" and str1[:2]== "12":
#         return "00"+str1[2:-2]
#     elif str1[:2] < "12" and str1[-2:] != "AM":
#         return str(int(str1[:2])+12) + str1[2:8]
#     elif str1[-2:] == "PM" and str1[:2]=="12":
#         return "12"+str1[2:8]
#     elif str1[:2] < "12" and str1[-2:] == "AM":
#         return str1[:8]
#
#
#
#
#
# inte = input("Enter %HH:%MM:%SS AM/PM \n")
# print(convert(inte))
#

print("*" * 40)
import datetime
import time

netflix = ""
current_time = datetime.datetime.now()
print(current_time)
expiry = datetime.timedelta(days=30)
print(expiry)


try:
    user = input("Enter the platform you want \n 1:Netflix \n 2:Prime").lower()
    if user == "netflix":
        print("Thanks for choosing our service your subscription has been started")
        print(f"your curent subs date: {current_time} \n Expiry Date : {expiry}")



except Exception as e :
    print("something wrong")





#
# def remain():
#     pass
