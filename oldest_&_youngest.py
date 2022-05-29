# Take the age of 3 people by user and determine oldest and youngest among them.

age_1= int(input("enter age: "))
age_2= int(input("enter next age: "))
age_3= int(input("enter next age: "))
if age_1>age_2 and age_1>age_3 and age_2<age_3:
    print(age_1,"is oldest and",age_2,"is youngest")
elif age_1>age_2 and age_1>age_3 and age_3<age_2:
    print(age_1,"is oldest and",age_3,"is youngest")
elif age_2>age_1 and age_2>age_3 and age_1<age_3:
    print(age_2,"is oldest and",age_1,"is youngest")
elif age_2>age_1 and age_2>age_3 and age_3<age_1:
    print(age_2,"is oldest and",age_3,"is youngest")
elif age_3>age_1 and age_3>age_2 and age_1<age_2:
    print(age_3,"is oldest and",age_1,"is youngest")
elif age_3>age_1 and age_3>age_2 and age_2<age_1:
    print(age_3,"is oldest and",age_2,"is youngest")
else:
    print("put different age")