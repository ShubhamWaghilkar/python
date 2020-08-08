class Employee:
    no_of_leaves = 8
    pass

shubham = Employee()
jon = Employee()

shubham.name = "shubham"
shubham.salary ="80000"
shubham.role="developer"
jon.name ="jon"
jon.salary ="60000"
jon.role="tester"

print(shubham.no_of_leaves)
print(shubham.__dict__)


print(f"before no. of leaves {Employee.no_of_leaves}")
Employee.no_of_leaves = 9
print(f"After changing the leaves {Employee.no_of_leaves}")
