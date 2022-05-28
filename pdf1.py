# Write a python program to find the maximum between two numbers.
a=int(input("enter number"))
b=int(input("enter number"))
if a<b:
    print(b,"is maximum")
elif b<a:
    print(a,"is maximum")
else:
    print("both are equal")