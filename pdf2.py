# Write a python program to find a maximum between three numbers.
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("Enter number"))
if a>b and a>c:
    print(a,"is maximum number")
elif b>a and b>c:
    print(b,"is maximum number")
else:
    print(c,"is maximum number")