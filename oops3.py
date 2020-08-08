class Employee:

    no_of_leaves = 8
    @staticmethod
    def pri():
        print( f"hello world")

    @classmethod
    def dup(cls,leaves):
        cls.no_of_leaves = leaves
    @classmethod
    def frt(cls,string):
        params = string.split("*")
        return cls(params[0],params[1],params[2])



    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f" Employee name is {self.name} their Salary is {self.salary} and their Role is {self.role} \n " \
               f"leave allownce {Employee.no_of_leaves}"


shubham = Employee("shubham",80000,"developer")
print(shubham.salary)
jon = Employee("JON",70000,"tester")
print(jon.salary)
shubham.pri()
shubham.dup(34)
print(shubham.no_of_leaves)
print(Employee.no_of_leaves)
arya = Employee.frt("arya*490*Analyst")
print(arya.name)

# shubham.name = "shubham"
# shubham.salary ="80000"
# shubham.role="developer"
#
#
# jon.name ="jon"
# jon.salary ="60000"
# jon.role="tester"
# #
# print(jon.printDetails())
# print(shubham.printDetails())

