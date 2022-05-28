# Write a python program to input electricity unit charges and
# calculate total electricity bill according to the given 
# condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
unit=int(input("enter unit"))
if 0<unit and unit<=50:
    _Rs=unit*0.50+20/100
    print("total bill=",_Rs)
elif 50<unit and unit<=150:
    _Rs=unit*0.75+20/100
    print("total bill=",_Rs)
elif 150<unit and unit<=250:
    _Rs=unit*1.20+20/100
    print("total bill=",_Rs)
elif 250<unit:
    _Rs=unit*1.50+20/100
    print("total bill=",_Rs)
else:
    print("not available")