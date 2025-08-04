# We are running a shop in which we have day off during Sundays. So, from date 1 to 30 every Sunday we are off. 30 can be 31 or 28 or 27
# as per days of months. Every day we need to calculate total sales amount which is in multiplication of 15 with current day. We need 
# a to know average sales of month at the end of month from everyday sales. So, we need a technical solution in which we provide the 
# month number (1 for January and so on) it will give us average sales of January month. Again we will pass our choice of month and 
# we will get average sales of that month. We will also give the year. So, 2 things year and month we need average sales of that month
# calculated based in every day sales.





import calendar
from datetime import date


def avg_sales(year,month):
    
    day_in_month=calendar.monthrange(year,month)[1]
    total=0
    day_count=0
    
    for day in range(1,day_in_month+1):
        today=date(year,month,day)
        
        if today.weekday()!=6:
            sale=day*15
            total+=sale
            day_count+=1
    if day_count==0:
        return 0
    return total/day_count

year=int(input("Enter year : "))
month=int(input("Enter month : "))

result = avg_sales(year,month)
print("avrage sales in ",calendar.month_name[month],year,"is",round(result, 2))
