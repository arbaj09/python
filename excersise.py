def add(num1,num2):
    return num1+num2
def substract(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def devide (num1,num2):
    return num1/num2
print("select the opreation-\n" \
      
    "1.+\n"\
    "2.-\n"\
    "3.*\n"\
    "4./\n")

select=int(input("please select opreation :"))
number_1=int(input("enter the first number:"))
number_2=int(input("enter the second number:"))

if select==1:
    print(number_1,"+",number_2,"=",
    add(number_1,number_2))

elif select==2:
    print(number_1,"-",number_2,"=",
    substract(number_1,number_2))
elif select==3:
    print(number_1,"*",number_2,"=",
    multiplication(number_1,number_2))
elif select==4:
    print(number_1,"/",number_2,"=",
    devide(number_1,number_2))
else:
    print("please choose the operator!")





