# 14. Write a python program to input angles of a triangle 
# and check whether triangle is valid or not.
_angel1=int(input("enter number"))
_angle2=int(input("enter number"))
_angle3=int(input("enter number"))
if (_angel1+_angle2+_angle3)==180:
    print("its a triangle")
else:
    print("it's not a triangle")