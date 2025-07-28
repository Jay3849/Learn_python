# class and obj example --------------


class Car:
    
    total_car=0
    def __init__(self,car,model):
        self.car = car
        self.model = model
        Car.total_car+=1
        
        
        
    def full_name(self):
        return f"this is my {self.car} and this model {self.model}"
    
    def fuel_type(self):
        return "petrol or desele"
    
    
        
     
     
class Electric_car(Car):
            
          def __init__(self,car,model,betry):
              super().__init__(car,model)
              self.betry=betry
          def fuel_type(self):
               return "electric charge "
          
        

my_car=Electric_car("tesla","204","250kg")

print(my_car.fuel_type())
my_car1 = Car("lambo",2024)



print(my_car1.fuel_type())
print(Car.total_car)

# print(my_car.car,my_car.model)
        
# car2=Car("safari","2020")

# print(car2.car,car2.model)                      