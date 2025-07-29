# define restourant menu list 

menu={
     "Pizza":500,
     "Pepsi":100,
     "Burger":150,
     "Salad":50,
     "Pasta":130
  
}

print("Welcome to our Python Restorant")

print("\n")

print("this is our Menu :- ")


for x,y in menu.items():
    print(x,":",y)
  
total_order=0    


item1=input("Enter your order accorading to menu : ")
if item1 in menu:
    total_order+=menu[item1]
    print(f"your{item1} is add to your oder..")
else:
    
    print(f"your {item1}is not available in this menu ")
    
    
another_order=input("Do want to another item can be order (YES/NO): ")
if another_order=="YES":
    item2=input("enter your   second itme : ")
    if item2 in menu:
        total_order+=menu[item2]
        print(f"ypur order can be adds on your order ...")
    else:
       
        print(f"your {item2}is not available in this menu ")
else:
   
    
     print("Thanks for ordering again visit out store ...!!")     
print(f"your total amount is to pay : {total_order}")
print("Thanks for ordering again visit out store ...!!")     
