import time
class Library:

    def __init__(self,list_of_books,library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend_data ={}

        for books in self.list_of_books:
            self.lend_data[books] = None

    def displayBooks(self):

        for index,books in enumerate(self.list_of_books):
            print(f"{index}) {books}")

    def Add(self,book):
        self.list_of_books.append(book)

    def lend(self,book,author):

        if book in self.list_of_books:
          if self.lend_data[book] is None:
              self.lend_data[book] = author
          else:
            print(f"Sorry this book is lend by {self.lend_data[book]}")
        else:
            print(f"You have written wrong book name")
    def return_book(self,book,author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
                self.lend_data[book] = author
                print(f"this books is return back by {self.lend_data[book]}")
            else:
                print(f"this book is not lend")
        else:
            print(f"You have written wrong book")
    def dele(self,book):
        if book in self.list_of_books:
            print("Deleting the book...")
            time.sleep(3)
            self.list_of_books.remove(book)
            self.lend_data.pop(book)
            print("Deleted Successfully")
        else:
            print(f"Book not found")











def main():
    list_books = ["Story books" , "Novels" , "RD SHARMA", "CHETAN BHAGAT", "NCERT"]
    Library_Name = 'Shubham'
    secret_key = "abc"

    Shubham = Library(list_books,Library_Name)

    print(f"Welcome To {Library_Name} Library \n 1: To Display \n 2:To Add books \n 3: Lend Book")
    Exit = False
    while(Exit is not True):
        user = input("options: ")
        print("\n")


        if user == "1":
            Shubham.displayBooks()
        elif user == "Exit":
            Exit = True
        elif user == "2":
            add = input("Enter Book Name : \n")
            Shubham.Add(add)
        elif user == "3":
            u1 = input("Enter your Name")
            u2 = input("Enter Book Name")
            Shubham.lend(u2,u1)
        elif user == "4":
            u1 = input("Enter your name")
            u2 = input("Enter Book name")
            Shubham.return_book(u2,u1)
        elif user == "5":
            u1 = input("Enter Secret key to delete The book from library")
            if u1 == secret_key:
                a1 = input("Enter Book Name")
                Shubham.dele(a1)
            else:
                print(f"You Entered wrong key \n Try Again...")




if __name__ == '__main__':
        main()