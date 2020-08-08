class Employee:
    no_of_leaves = 9
    def __init__(self,salary,role):
        self.salary = salary
        self.role = role

    def __add__(self, other):
        return self.salary + other.salary


emp1 = Employee(500,"devlop")
emp2 = Employee(8000,"prog")
print(emp1+emp2)