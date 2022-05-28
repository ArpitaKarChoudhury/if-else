# 12. Write a python program to input the month number and
#  print the number of days in that month.
_month=int(input("enter number"))
if _month==1 or _month==3 or _month==5 or _month==7 or _month==8 or _month==10 or _month==12:
    print("31 days")
elif _month==4 or _month==6 or _month==9 or _month==11:
    print("30days")
elif _month==2:
    print("28days")
else:
    print("invalid month")