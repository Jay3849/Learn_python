# nums=[1,-2,3,-4,-5,3,4,4,4]
# positive=0

# for num in nums:
#     if num>0:
#         positive+=1
# print("positivr numbrt ",positive)


# num =int(input("enter your number : "))

# for i in range(1,11):
#     if i==5:
#         continue
#     print(num,'X',i,'=',num*i)
    

# num =int(input("enter your number : "))
# fact = 1
# while num >0:
#     fact = fact * num
#     num = num-1
# print(fact)
    
# while True:

#     num = int(input("enter your num 1 to 10 : "))
    
#     # if num!=str:
#     #     print("valid value try agiun")
        
#     #     exit()
#     if 1<=num <=10:
#         print("thanks ")
#         break
    
#     else :
#         print("try again valid enter number ")



# for i in range (1,6):
#     print(i,end=" ")


# for i in range (1,6):
#     print(i**2,end=" ")

# for i in range (1,11):
#     if(i%2==0):
#         print(i,end=" ")

    # total = 0


    # for i in range (1,11):
    #         total+=i
    # print(total)
    
    
# str = 'jay'

# for i in range(len(str)-1,-1,-1):
#     print(str[i],end=" ")


# vowles = 'aeiou'
# word = 'jayparmar'
# count=0

# for char in word:
#     if char in vowles:
#         count+=1
# print(f'your vowels {word} in total {count}')


# n=5
# facat=1

# for i in range(1,n+1):
#     facat*=i
# print(facat)

# is_prime = True
# n=10
# for i in range(2,int(n**0.5)+1):
#     if n%i==0:
#      is_prime=False
#      break
# if is_prime and n>1:
#     print(n ,'is a prime number ')
# else :
#     print(n,'num is not a prime ')


# while loop 
# num = 10

# while num<=15 :
#     print(num,end=" ")
#     num+=1

# num=1


# while num<=5:
#     print(num ** 3,end=" ")
#     num+=1
   
# n=1

# while n<=10:
#     if n%2!=0:
#         print(n,end=" ")
#     n+=1 
# pnum=1
# num=1

# while num<=5:
#     pnum*=num
#     num+=1
#     print(pnum)


# str=input("enter a str: ")

# words=str.split()

# for word in words:
#     i=len(word)-1
#     while i>=0:
        
#      print(word[i],end="")
#      i-=1
#     print(end=" ")

# str='jay'

# for k in str:
#     i=len(str)-1
#     while i>=0:
#         print(str[i],end="")
    
#         i-=1

# str=input("enter a string: ")

# vowels='aeiou'
# count=0
# index=0

# while index<len(str):
#     if str[index].lower() not in vowels and str[index].isalpha():
#         count+=1
#     index+=1
# print(  "num is consistance : ",count)


# num=1
# mul=3

# while num<=5:
#     num*=mul
#     print(num,end=" ")
#     num+=1
    
    
# num = 1
# while num <= 5:
#     print(num * 3 ,end=" ")
#     num += 1

# basevalue=int(input("enter a base value : "))
# expoenentval=int(input("enter a expoenent value : "))
# count=0
# result=1

# while count<expoenentval:
#     result=result*basevalue
#     count+=1
# print(result)


# num=int(input("enter your test number : "))
# i=1
# is_perfect_sqr=False

# while i*i<=num:
#     if i*i==num:
        
#         is_perfect_sqr=True 
#         break
#     i+=1
# if is_perfect_sqr:
#     print(f"{num} is perfcet sqr")
# else :
#     print("not a perfcet --sqr")


# str=input("enter a string : ")
# char_count=input("Enter a charecter you will count : ")

# count=0
# index=0

# while index<len(str):
#     if str[index]==char_count:
#         count+=1
#     index+=1
# print(f"{char_count} is {count} time ")