# Assignment 1 :- 
# If number is divided by 2 and result is zero we should show sign (by 2)
# if($i/2 == 0)
 
# - If number is in between 39 to 67 then show sign (between)   	
# if($i>39 && $I<67)	
 
# - If number is minus then and between -25 to -78 show sign (negative range)   
# if($i < 0 && ($i < -25 && $i > -78))
 
# - If number is subtract by 7 and answer is between 89 to 145 show sign (in subtract range)   
# $a = $i - 7;
# if($a > 89 && $a < 145)


def Num_check(n):

    if n % 2 == 0:
        print("by 2")
        
    if n > 39 and n < 67:
        print("between")

    if n < 0 and n < -25 and n > -78:
        print("negative range")
    
    a = n - 7
    if a > 89 and a < 145:
        print("in subtract range")
 
num = int(input("Enter your number: "))
Num_check(num)


# Assignment 2 :- 
# If number is grater then (range 2 - range 1) we should show sign (is grater)
# if($i > ($range_2 - $range_1))
 
# - If number is in between 57 to 203 then show sign (between)   	
# if($i > 57 && $I < 203)
 
# - If number is minus then and between -305 to -780 show sign (negative range)   
# if($i < 0 && ($i < -305 && $i > -780))
 
# - If number is subtract by 70 and answer is between 100 to 300 show sign (in subtract range)   
# $a = $i - 70;
# if($a > 100 && $a < 300 )

def Check_num(i,rang1,rang2):
    if i >(rang2-rang1):
        print("is grater ")
        
    if (i >57 )and (i<203):
        print("between")
        
    if i<0 and (i<-305 and i>-780):
        print("nagative range ")
        
    x=i-70
    if (x>100 and x<300):
        print("in subtract range ")
        
number=int(input("enter number : "))
rang1=int(input("Enter range 1 "))
rang2=int(input("enter range 2 : "))

Check_num(number,rang1,rang2)


 