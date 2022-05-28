# 16. Write a python program to check whether the triangle is 
# equilateral, isosceles or scalene triangle.
_angel1=int(input("enter number"))
_angle2=int(input("enter number"))
_angle3=int(input("enter number"))
if _angel1==_angle2 and _angle2==_angle3:
    print("its a equilateral")
elif _angel1==_angle2 or _angle2==_angle3 or _angel1==_angle3:
    print("isosceles")
else:
    print("scalene")