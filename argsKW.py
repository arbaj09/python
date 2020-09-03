# def funargs(Nornal,*args,**kwargs):
#      print(Nornal)
#
#      for item in args:
#
#         print(item)
#      print("\nNow i would like to introduce some of heros : ")
#      for key,value in kwargs.item():
#          print(f"(key) is a {value}")
#
# har=["harry", "rohan","skillf","hammad","the programmer"]
# normal="i am a normal argument and the student are:"
# kw=["rohan","monitor"]
# funargs(normal,*har,**kw)


def funargs(nornal, *args, **kwargs):
    print(nornal)
    for item in args:
        print(item)
    print("now i would like to introduce some heros")
    for key, value in kwargs.item():

        print(f"(key) is a {value}")


har = ["rohan", "harry", "skillf", "hammad", "shivam", "the programmer"]
normal = "i am a normal argument and the student are :"
kw = {"rohan:monitor", "harry:fitness instructor", "the programmer:cordinator"}
funargs(normal, *har, **kw)
