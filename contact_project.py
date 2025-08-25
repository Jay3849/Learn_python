       
contact = {}

while True:
    print("\nContact Book App---")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit the app")
    
    choice = input("Enter your choice : ")
    
    if choice == '1':
        name = input("ENTER YOUR NAME : ")
        
        if name in contact:
            print("Contact name already exists")
        else:
            age = input("Enter age : ")
            email = input("Enter email : ")
            mobile = input("Enter mobile : ")
            contact[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"{name} has been created successfully")
    
    elif choice == '2':
        name = input("Enter a name to view : ")
        if name in contact:
            details = contact[name]
            print(f"name: {name}, age: {details['age']}, email: {details['email']}, mobile: {details['mobile']}")
        else:
            print("Contact name not found!")
    
    elif choice == '3':
        name = input("Enter a name you want to update : ")
        if name in contact:
            age = input("Enter updated age : ")
            email = input("Enter updated email : ")
            mobile = input("Enter updated mobile : ")
            contact[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f"{name} has been successfully updated")
        else: 
            print("Contact not found!!")
        
    elif choice == "4":
        name = input("Enter a name you want to delete : ")
        if name in contact:
            del contact[name]
            print(f"{name} has been successfully deleted")
        else:
            print("Contact not found!!")
            
    elif choice == "5":
        search_name = input("Enter a name to search : ").lower()
        found = False
        for key, details in contact.items():
            if search_name in key.lower():
                print(f"Found → name: {key}, age: {details['age']}, email: {details['email']}, mobile: {details['mobile']}")
                found = True
        if not found:
            print("Contact not found!!")
                
    elif choice == "6":
        if len(contact) == 0:
            print("No contacts available")
        else:
            print("Your total contacts are : ", len(contact))
            
    elif choice == "7":
        print("Thanks for using our app, have a nice day!!")
        break
    
    else:
        print("Invalid input")

        
          
            
            