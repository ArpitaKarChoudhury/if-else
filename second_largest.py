# Accept three nos from the user and display the second largest no

num_1= int(input("enter number: "))
num_2= int(input("enter next number: "))
num_3= int(input("enter next number: "))
if num_1>num_2 and num_2>num_3:
    print(num_2,"is the second largest number")
elif num_1>num_3 and num_3>num_2:
    print(num_3,"is the second largest number")
elif num_2>num_1 and num_1>num_3:
    print(num_1,"is the second largest number")
elif num_2>num_3 and num_3>num_1:
    print(num_3,"is the second largest number")
elif num_3>num_1 and num_1>num_2:
    print(num_1,"is the second largest number")
elif num_3>num_2 and num_2>num_1:
    print(num_2,"is the second largest number")
else:
    print("No second largest number")