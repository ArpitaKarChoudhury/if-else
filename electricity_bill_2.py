# Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :Unit Price First 100 units no charge ,Next 100 units
# Rs 5 per unit ,After 200 units Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

unit= int(input("enter unit: "))
if unit>=1 and unit<=100:
    print("no charge")
elif unit>100 and unit<=200:
    print("total bill=",(unit-100)*5)
elif unit>200:
    print("total bill=",((unit-200)*5)+100*10)
else:
    print("unavailable")