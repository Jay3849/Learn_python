def Task():
    
    Tasks=[]
    
    print("-----Wlcome to our Task Managemnet System...####")
   
    Total_task=int(input("Enter how many taks you wan't to add : "))
    i=1
    while i<=Total_task:
          task_name=input(f"enter {i} task name:- ")
          if task_name in Tasks:
            print(f"{task_name} already add.. try other add taks..")
            continue
          else:
            Tasks.append(task_name)
            i+=1
        
    print(f"Today's your Tasks: {Tasks}")
        
  
    
    
    while True:
        operation=int(input(" \n1-add\n2-Update\n3-Delete\n4-View\n5-Exit \nEnter your input to operation:"))
        if operation==1:
            
            add_task=input("enter add your task : ")
            if add_task in Tasks:
                print(f"your {add_task} is already here ")
            else:
              Tasks.append(add_task)
              print(f"{add_task} is successfully add ....")
        
        elif operation==2:
            old_task=input("enter your task you will change : ")
            if old_task in Tasks:
                up_val=input("enter new Task : ")
                index=Tasks.index(old_task)
                Tasks[index]=up_val
                print(f"{up_val} is updated your Tasks ")
            else:
                print(f"your task in not not available plz enter valid task ")
        elif operation==3:
            del_val=input("enter your Task you will be delete : ")
            if del_val in Tasks:
                index=Tasks.index(del_val)
                del Tasks[index]
                print(f"{del_val} is successfully remove ... ")
            else:
                print(f"your task in not not available plz enter valid task ")
        elif operation==4:
            print(f"your tasks is {Tasks}")
        elif operation==5:
            print("closing the taks mangement... ")
            break
        else:
            print("invalid input try again...")
    
Task()