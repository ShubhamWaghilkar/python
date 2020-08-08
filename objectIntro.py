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

skill = Employee("dill","Bill")
print(skill.printEmail)
print(type(skill))
print(id("shubham"))
