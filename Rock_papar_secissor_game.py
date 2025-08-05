import random

items=["Rock","Paper","Scissor"]
user_choice=input("Enter you choice :- Rock,Paper,Scissor : ")
computer_choice=random.choice(items)

print(f"user choice is {user_choice}, computer choice is {computer_choice}")


if user_choice==computer_choice:
    print("Both choose same = match Tie" )
elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper cover Rock : Computer is win !!")
    else :
        print("Rock smashes Scissor : You win ")
elif user_choice=="Paper":
    if computer_choice=="Rock":
        print("Paper cover Rock : You  win !!")
    else :
        print("Scissor cut Paper : computer is Win")
elif user_choice=="Scissor":
    if computer_choice=="Rock":
        print("Rock smashes Scissor : computer is  win ")
    else:
        print("Scissor cut Paper : You  Win")
else :
    print("invalid input try again !!!!")
        
        
        
        
    
