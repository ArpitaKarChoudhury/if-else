# Write a program to check whether the last digit of a number is divisible by 3 or not.

num= int(input("enter number: "))
last_digit= num%10
if last_digit%3==0:
    print("last digit of",num,"is divisible by 3")
else:
    print("last digit of", num,"is not divisible by 3")