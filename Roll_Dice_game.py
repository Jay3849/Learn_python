import random

print("Welcome to the Roll_Dice_Game---")


while True:
   
    choice=input("Enter your choice [yes/no] : ").lower()
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    
    total=0
    if choice=="yes":
        print(f"{die1} , {die2}")
        total+=1
        print("total= ",total)
    elif choice=="no":
        print("thanks...")
        break
    else:
        print("invalid input try again ...")
    
    
    
    