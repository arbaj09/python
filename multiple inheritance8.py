class Employe:
    var=5
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

class player:
    var=7
    no_of_game=3
    def __init__(self,name, game):
        self.name=name
        self.game=game
    def printdetail(self):
         return f"the name is {self.name} and game is {self.game}"
class coolprogrammer(Employe,player):
    var = 20
    language="c++"
    def printlanguage(self):
        print(self.language())

harry=Employe("harry",255,"instructor")
rohan=Employe("rohan",455,"student")

subham=player("subham",["cricket"])
karan=coolprogrammer("karan",9999,"coolprogrammer")
# det=karan.printdetail()
# print(karan.language)
# print(det)
print(subham.var)