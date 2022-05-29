# Write a python program to find a maximum between three numbers.

num1=int(input("enter no: "))
num2=int(input("enter no: "))
num3=int(input("enter no: "))
if num1>num2 and num1>num3:
    print(num1,"maximum no")
elif num2>num1 and num2>num3:
    print(num2,"maximum no")
elif num3>num1 and num3>num2:
    print(num3,"maximum no")
else:
    print("there is no maximum no")