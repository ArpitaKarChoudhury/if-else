# 15. Write a python program to input all sides of a triangle and
#  check whether the triangle is valid or not.
side1=int(input("enter number"))
side2=int(input("enter number"))
side3=int(input("enter number"))
if (side1+side2)>side3:
    print("the triangle is valid")
elif (side1+side3)>side2:
    print("the triangle is valid")
elif (side3+side2)>side1:
    print("the triangle is valid")
else:
    print("the triangle is invalid")