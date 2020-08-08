#overriding

class Aoss:
    classvar1 = "Iam in classs variable class A"

    def __int__(self):
        self.var1 = "Iam inside class A constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "hello"




class Boss(Aoss):

    classvar1 = "Iam in classs variable class B"

    def __int__(self):

        self.var1 = "Iam inside class b constructor"
        self.classvar1 = "Instance var in class b"
        super().__init__()

a = Aoss()
b = Boss()

print(print(b.special))