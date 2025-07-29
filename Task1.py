
# Build a simple Python script to manage a grocery store inventory.
# The system should allow the store manage the add , remove, update and search products in inventory using list methods 
 
# You can use list and dictionary methods to build a program 

print("###### Welcome grocery_store_inventory#######")
print('\n')
print(" 1 . list our item..")
print(" 2 . add our item..")
print(" 3 . remove our item..")
print(" 4 . update our item..")
print(" 5 . search our item..")
print(" 6 . Exit our store..")

print("choose your number >>> ")
grocery_store_inventory=['Milk','Apples','Bread','Chips','Coffee','Shampoo']

usr_input=int(input("Enter your number : "))
match usr_input:
    case 1:
        print(grocery_store_inventory)
    case 2:
        item=input("Enter your item : ")
        grocery_store_inventory.append(item)
        print(f"{item} is add our store sucessfully")
        print("Updated store :", grocery_store_inventory)
    case 3:
        remove_item=input("enter you will remove item : ")
        if remove_item in grocery_store_inventory:
            grocery_store_inventory.remove(remove_item)
            print(f"{remove_item} is sucessfully remove our store ..")
            print("Updated store :", grocery_store_inventory)
        else:
            print(f"{remove_item} is not found in this store ...")
    case 4:
        old_item=input("Enter your item you will change : ")
        if old_item in grocery_store_inventory:
            new_item=input("Enter new item name : ")
            index=grocery_store_inventory.index(old_item)
            grocery_store_inventory[index]=new_item
            print(f"{old_item} updated to {new_item}")
            print("Updated store :", grocery_store_inventory)
        else:
            print(f"{old_item} is not found our  store..")
    case 5:
        srch_item=input("Enter your item will be search: ")
        if srch_item in grocery_store_inventory:
            print(f"{srch_item} can be here...")
        else:
            print(f"{srch_item}is not found our store...")
            
    case 6:
        print("Thanks to visit our store!!!...") 
    case _:
        print("invalid input..try again")

        
 
        
    
        
        
        






























# #add items to the store 

# add_item=input("Enter a item name : ")
# add_item.append()
# grocery_store_inventory.append("soda")

# print(f"soda is add on the store ")
# print("grocery items add item",grocery_store_inventory)
# print('\n')


#  #remove item form store 
# grocery_store_inventory.remove("Chips")
# print("chips is remove from store ")
# print("remove item after store details!!!",grocery_store_inventory)
# print('\n')



# print("items can be updatd ")

# grocery_store_inventory[1]='cherry'

# print('cheryy is update in store ')
# print(grocery_store_inventory)
# print('\n')


# #searching items for stors.....

# print("searching profucts our store ")


# if 'Milk' in grocery_store_inventory:
#     print("milk is here in store ")
# else:
#     print("itme is not available")


# print("thank you for visiting our store ####")


 
