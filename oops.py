# # class and obj example --------------


# class Car:
    
#     total_car=0
#     def __init__(self,car,model):
#         self.car = car
#         self.model = model
#         Car.total_car+=1
        
        
        
#     def full_name(self):
#         return f"this is my {self.car} and this model {self.model}"
    
#     def fuel_type(self):
#         return "petrol or desele"
    
    
        
     
     
# class Electric_car(Car):
            
#           def __init__(self,car,model,betry):
#               super().__init__(car,model)
#               self.betry=betry
#           def fuel_type(self):
#                return "electric charge "
          
        

# my_car=Electric_car("tesla","204","250kg")

# print(my_car.fuel_type())
# my_car1 = Car("lambo",2024)



# print(my_car1.fuel_type())
# print(Car.total_car)

# # print(my_car.car,my_car.model)
        
# # car2=Car("safari","2020")

# # print(car2.car,car2.model)      

# class Studnet:
    
#     clg_name="sarvajnik clg.."      
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

# s1=Studnet("jay",89)
# print(s1.clg_name)
# print(f"srtudent name: {s1.name}\nmamrks: {s1.marks}")




# constructor oops conecpts  
# class Student:
    

        
        
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#             avg=sum/3
#         print(f"{self.name} your avg score is : {avg}")
                  
# s1=Student("jajaj",[99,98   ,97])


# s1.get_avg()


# staticmthod like decorators in python 

# class demo:
    
#     @staticmethod #decorators 
#     def hello():
        
#         print("good morning guyss...")

# demo1=demo()
# demo1.hello()


# abstraction methos ,,,,,


# class car:
    
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch =False
#     def car_start(self):
#         self.clutch=True
#         self.acc=True
#         print("your car is start now...")
        
# car1=car()
# car1.car_start()


#example with prectice to understand oops conecpts 


# class Account:
    
#     def __init__(self,name,balance,acc):
#         self.nameholder=name
#         self.balance=balance
#         self.acc_no=acc
#         print(f"accountholder name:{self.nameholder}")
#         print(f"account number is:{self.acc_no}")
#         print(f"accunt balance is :{self.balance}")
        
#     def debit(self,amount):
#         self.balance-=amount
#         print(f"{amount} was debited your account ")
#         print(f"total balance is : {self.balance}")
    
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"{amount} form your account")
#         print(f"total balance is : {self.balance}")
        
        
        
# user1=Account("jay",1000,1234567)

# print(user1.nameholder,user1.acc_no,user1.balance)
# user1.credit(500)


# calculate area and circle 
# class Circle:
    
#     def __init__(self,redius):
#         self.radius=redius
        
#     def area(self):
#         return (22/7)*self.radius**2
#     def parameter(self):
#         return 2*(22/7)*self.radius
    
# c1=Circle(  21)
# print(c1.area())
# print(c1.parameter())


# class Emp:
#     def __init__(self,dept,role,salary):
#         self.dept=dept
#         self.role=role
#         self.salary=salary
#     def Show_details(self):
#         print("department : ",self.dept)
#         print("Role : ",self.role)
#         print("salary is : ",self.salary)
        
# class Engineer(Emp):
#     def __init__(self,name,age):
        
#         self.name=name
#         self.age=age
#         super().__init__("acc", "emp", 33000)
    
        
# emp1=Engineer("jay","22")
# emp1.Show_details()


class Order:
    
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ord2):
        return self.price>ordr2.price
    
ordr1=Order("packets",35)
ordr2=Order("sugar",20)

print(ordr1>ordr2)




