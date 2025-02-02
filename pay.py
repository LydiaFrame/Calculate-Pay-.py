#!/usr/bin/env python3 

"""Write a program to calculate the amount of an employees paycheck"""

__author__="Lydia Frame"
__date__="02/02/2025"

#prompt for hourly pay
pay_rate = float(input("Hourly pay rate? "))
print()

#prompt user for hourly or salary?
pay_type = input("Hourly/salary (H/S)? ").strip().lower()
print()

#Calculate salary pay or hourly pay 
if pay_type == "s":
    weekly_pay = round(pay_rate * 40, 2)
elif pay_type == "h":
    num_hours = float(input("Num hours? "))
    print()
    holiday = input("Holiday (Y/N)? ").strip().lower() 
    print()

    if holiday == "y":
        weekly_pay = round(pay_rate * num_hours * 2, 2) 
    else:
        if num_hours <= 40:
            weekly_pay = round(pay_rate * num_hours, 2)
        else:
            reg_hours = 40
            overtime = num_hours - 40
            weekly_pay = round((reg_hours * pay_rate) + (overtime * pay_rate * 1.5), 2)

#print weekly pay
print("Your weekly pay $" + str(weekly_pay))