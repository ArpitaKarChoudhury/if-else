# Write a python program to check whether a year is leap year or not.
a=int(input("enter number"))
if a%400==0:
    print(a,"is century number and leapyear number")
elif a%4==0 and a%100!=0:
    print(a,"is leap year ")
else:
    print(a,"is normal year")