import random

targate=random.randint(1,100)


while True:
    userChoice=input("Guess the Targate or Quite game : ")
    if (userChoice=="Q"):
        break

    userChoice=int(userChoice)
    
    if(userChoice==targate):
        print("success : Correct guess ")
        break
    elif(userChoice<targate):
        print("your num was small plz enter big number ")
    else:
        print("your num is big plx enter small number ")
        
print("----Game--Over---")