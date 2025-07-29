student_grades={
    
}

def add_student(name,grade):
    student_grades[name]=grade
    print(f"added {name} with a grade {grade}")
    
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"   {name}with marks are updated{grade}")
        
    else:
        print(f"{name} is not found!!")
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been succesfully deleted..")
    else:
        print(f"{name} is not found!!")
def view_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no student found!!!")
        
def main():
    print("\n Welcome to our student-Management-system...")
    
    while True:
   
        print("1.Add student\n2.Update student\n3.Delete student\n4.View student\n5.Exit")
        print("Enter your input to operate the system:- ")
    
        
        choice=int(input("enter here : "))
        print("\n")
        if choice==1:
            name=input("enter your student name : ")
            grade=input("enter your student grade : ")
            add_student(name,grade)
        elif choice==2:
            name=input("enter your student name : ")
            grade=input("enter your student grade : ")
            update_student(name,grade)
            
        elif choice==3:
            name=input("enter a name you will be delete : ")   
            delete_student(name)
            
        elif choice==4:
            view_students()
        
        elif choice==5:
            print("closing the system...")
            
            break
   
main()