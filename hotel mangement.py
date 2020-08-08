class Hotel:
    def __init__(self,menu,hname):
        self.menu = menu
        self.hname = hname
        self.cart = {}.__str__()

    def display(self):
        for i,j in self.menu.items():
            print(f"{i} Rs {j}")

    def order(self,menu):
        self.menu = menu
        for i,j in self.menu.items():
            print(f"{i} Rs {j}")
        self.dish = (input("Enter dish name to order"))
       # self.qty  = int(input("Select Quantity"))
        if self.dish in self.menu:
            a = self.menu.pop(self.dish)
            self.cart = a
            #self.bill = self.qty * int(j)
            print(f"You Order {i} Rs {j} ")
            print(f"Cart {self.cart}")
        else:
            print(f"Dish not found")
            #print(self.menu.pop(self.dish))
        # if dish in menu:
        #   print(menu)
        # else:
        #     print("wrong dish entered")
    def DelOrder(self):
        self.d = input("Enter dish that you want to remove")
        if self.d in self.cart is not None:
            self.cart =""
            print(f"Your cart is empty now...")
        else:
            print(f"The item you entered is not present in cart")



def main():
    menu = {"Maharashtra thali":1200,"Chinese":50,"Continental":1500}
    Hotel_Name = "Shubham"

    Shubham = Hotel(menu,Hotel_Name)
    print(f"Welocme to {Hotel_Name} Hotel Order your Favourite food")
    print("1: Order \n 2: Cancel Order \n 3: To View Menu")

    Logout = False
    while (Logout is not True):
       user = input("options :")
       print("\n")
       if user == "3":
           Shubham.display()
       elif user == "1":

           Shubham.order(menu)
       elif user == "5":
           Shubham.DelOrder()



if __name__ == '__main__':
     main()
