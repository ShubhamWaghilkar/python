# def func_name_print(a,b,c,d):
#     print (a,b,c,d)
# func_name_print("harry","shubham","jon","stark")

def runar(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
    for key , value in kwargs.items():
        print(f"{key} and the value is {value}")


a = ["harry","shubham","jon","stark","hello"]

cm = "This is aa normal argument"

ca = {"shubham":"programmer","web":"developer"}
runar(cm,*a,**ca)