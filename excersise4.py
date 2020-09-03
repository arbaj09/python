#pattern printing
#input=integer n

#boolean =true of false
#*
#**
#***
#****


#n=5
#print("*\n","**\n",
            #"***\n",
           # "****\n")

#
# print("enter the value :")
# n=int(input())
# if n==5:
#     print("*\n","**\n","***\n","****\n")
# elif n==10:
#     print("****\n","***\n","**\n","*\n",)
#
# else:
#     print("invalid key")



print("how many row you want to print")
one=int(input())
print("type 1 or 0 ")
two=int (input())
new=bool(two)
if new==True:
    for i in range(0,one+1):
        for j in range(1,i+1):
            print("*",end="")
        print()

if new == False:
    for i in range(one,0,  -1):
        for i in range(1, i + 1):
            print("*", end="")

        print()















