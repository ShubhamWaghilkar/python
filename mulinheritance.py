class employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f" Employee name is {self.name} their Salary is {self.salary} and their Role is {self.role} \n " \
               f"leave allownce {employee.no_of_leaves}"

class player:
    no_of_games = 4
    def  __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetail(self):
        return f"The name is {self.name} and game is {self.game}"

class coolProgrammer(player,employee):
    language = "JAVA"
    def prlanguage(self):
        print(self.language)


shubham = player("shubham",["cricket","football"])

jon = coolProgrammer("jon","scoccer")
print(jon.printdetail())
print(jon.prlanguage())

# class personal(employee):
#     def pr(self,language):
#         return f"Employee langauge {language}"
#
# shubham = personal("Shubham",50000,"programmer")
#
# print(shubham.pr("python"))
# print(shubham.printDetails())