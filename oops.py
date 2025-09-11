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
# Book Class (Encapsulation)





class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
    
    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False
    
    def return_book(self):
        self.copies += 1

class Person:
    def __init__(self, name):
        self.name = name
    
    def show_details(self):
        print(f"Person: {self.name}")

class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.borrowed = []
    
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} not available")
    
    def return_book(self, book):
        if book in self.borrowed:
            book.return_book()
            self.borrowed.remove(book)
            print(f"{self.name} returned {book.title}")
    
    # Polymorphism → override show_details()
    def show_details(self):
        print(f"Member: {self.name}, Borrowed: {[b.title for b in self.borrowed]}")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_member(self, member):
        self.members.append(member)



lib = Library()

# Add Books
b1 = Book("Python", "Guido", "101", 2)
b2 = Book("AI", "Andrew", "102", 1)
lib.add_book(b1)
lib.add_book(b2)

# Add Members
m1 = Member("Alice", "M01")
m2 = Member("Bob", "M02")
lib.register_member(m1)
lib.register_member(m2)

# Borrow/Return
m1.borrow_book(b1)
m2.borrow_book(b1)
m1.return_book(b1)

# Show Members
m1.show_details()
m2.show_details()
