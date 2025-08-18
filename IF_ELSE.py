
# odd even check 

# user_input=int(input("Enter your check number : "))

# if user_input%2==0:
#     print(f"{user_input} is even number ")
# else :
#     print(f"{user_input} is odd number ")
    
    
# prime number check 

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("not prime")
# elif num == 2 or num == 3:
#     print("prime number ")
# elif num % 2 == 0 or num % 3 == 0:
#     print("not prime")
# else:
#     print("prime number ")


def fact(n):
    result=1
    for i in range(n,0,-1):
        result*=i
    print(result)

num=int(input("enter number : "))
fact(num)
