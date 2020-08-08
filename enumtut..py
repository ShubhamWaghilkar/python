l1 = ["bhindi","aloo","chowmin","chopsticksi ","chinese"]

# i = 0
#
# for item in l1:
#     if i%2 is not 0:
#         print(f"please bring {item}")
#     i +=1


for index,item in enumerate(l1):
    if index % 2 is not 0:
        print(f"please bring {item}")