def searcher():
    import time
    f = open("co.txt", "rt")
    time.sleep(3)
    f1 = f.read()

    while True:
        text = (yield)
        if text in f1:
            print("Your text found ")
        else:
            print("your text not found")
search = searcher()
next(search)

while True:
    user = input("Enter the letter you want to search")
    search.send(user)
    if user == "0":
        print("Search ended")
        break
