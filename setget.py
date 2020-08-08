class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def printEmail(self):
        if self.fname == None or self.lname == None:
            return "Email Does not exists"

        return f"{self.fname}.{self.lname}@ooyaa.com"

    @printEmail.setter
    def printEmail(self,string):
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @printEmail.deleter
    def printEmail(self):
        self.fname = None
        self.lname = None

#supp = Employee("shubham","waghilkar")
# tupp = Employee("jon","snow")


# supp.fname = "vaishnavi"
# print(supp.printEmail)
# supp.printEmail = "jack.lon"
# print(supp.printEmail)
#
a = input("Enter Details for your fname \n")
b = input("Enter last name \n")
supp = (Employee(a,b))



supp.fname = "shubham"

print(supp.printEmail)
# del supp.printEmail
# print(supp.printEmail)