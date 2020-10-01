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

class programmer (Employe):
    no_of_holiday=56
    def __init__(self,name, salary,role, language):
        self.name=name
        self.salary=salary
        self.role=role
        self.language=language
    def printprog(self):
         return f"the name is {self.name} salary is {self.salary} and role is {self.role} and the language are {self.language}"


harry=Employe("harry",255,"instructor")
rohan=Employe("rohan",455,"student")
subham=programmer("subham",555,"programmer",["python","java"])
karan=programmer("karan",777,"programmer",["python"])
print(subham.no_of_holiday)