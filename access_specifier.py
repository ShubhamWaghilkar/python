class Employee:
    _no_of_leaves = 8
    __bcs = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f" Employee name is {self.name} their Salary is {self.salary} and their Role is {self.role} \n " \
               f"leave allownce {Employee.no_of_leaves}"

emp = Employee("shubham",50000,"devops")

print(emp._Employee__bcs)
