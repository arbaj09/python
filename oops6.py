class Employe:
    no_of_leave=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetail(self):
        return f"the name is {self.name} salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leave=newleaves
    @classmethod
    def form_das(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("this is good "+string)



harry=Employe("harry",255,"instructor")
rohan=Employe("rohan",455,"student")
arbaz=Employe.form_das("arbaz-452-student")
print(arbaz.salary)
harry.change_leaves(45)
print(arbaz.printgood("shaikh")) 