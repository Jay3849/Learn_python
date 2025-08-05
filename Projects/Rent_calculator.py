rent=int(input("Enter your room/hostel rent: "))
food=int(input("Enter total food bill: "))
electricity_spend=int(input("Enter you spend : "))
charge_per_unit=int(input("Enter the charge par unit : "))
total_persons=int(input("Enter number of person living in room/hostel : "))


total_bill=electricity_spend*charge_per_unit
output=(rent+food+total_bill)//total_persons

print(" one person bill is : ",output)