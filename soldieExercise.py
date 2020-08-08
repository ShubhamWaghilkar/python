import os


def format(path,file,form):
    path = path
    file = file
    form = form
    print(os.listdir(path))
    f = open(file)
    file4 = f.read()
    file4.split("\n")
    print(file4)
    count = 0
    for f in os.listdir():
        fnam,fxt = os.path.splitext(f)
        if fxt == f".{form}":
           print(f)
           new_name = f"str{count}.{form}"
           count = +1
           os.rename(f,new_name)
           pass

        # new_name,form2 = f.split(f)
        # if f == f".{form}":
        #     print("yess")
        # else:
        #     print("no")




if __name__ == '__main__':
    user1 = input("Enter file path ")
    user2 = input("Enter the file name ")
    user3 = input("Enter the file format like .txt,.jpg")
    format(user1,user2,user3)
