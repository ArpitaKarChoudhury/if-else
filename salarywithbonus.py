# A company decided to give a bonus of 5% to an employee if
# his/her year of service is more than 5years. Ask users for 
# their salary and year of service and print the net bonus
# amount.
salary=int(input("enter amount"))
year=int(input("enter year"))
if year>=5:
    bonus=salary*5//100
    net_bonus=bonus+salary
    print("net bonus=",net_bonus)
else:
    print("total salary=",salary)