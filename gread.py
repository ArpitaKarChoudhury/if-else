# Write a python program to input marks of five subjects Physics,
# Chemistry, Biology, Mathematics and Computer. Calculate
#  percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
_phy=int(input("enter physics mark"))
_chm=int(input("enter chemistry mark"))
_bio=int(input("enter biology mark"))
_math=int(input("enter mathmatics mark"))
_com=int(input("enter computer mark"))
total=(_phy+_chm+_bio+_math+_com)
percentage=total/100*5
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=40:
    print("Grade E")
elif percentage<40:
    print("Grade F")
else:
    print("panding")