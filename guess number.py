n=18
number_of_gesses=1
print("number of guesses is limited to only 9 times:")
while (number_of_gesses<=9):
    guess_number= int(input("guess the number:\n"))
    if guess_number<18:
        print("you enter less number please enter greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input les number.\n")
    else:
        print("you win.\n")
        print(number_of_gesses,"number of gusses he took to finish")
        break

        print(9-number_of_guesses,"no. of guesse left")
        number_of_gesses=number_of_gusses+1

if(number_of_gesses>9):
            print("game over")