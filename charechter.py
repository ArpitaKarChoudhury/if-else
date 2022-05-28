# Write a python program to input any character and check whether it is alphabet, digit or special character
txt=input("enter value")
if txt>=chr(65) and txt<=chr(90) or txt>=chr(97) and txt<=chr(122):
    print(txt,"is alphabate")
elif txt>=chr(33) and txt<=chr(47) or txt<=chr(64) and txt>=chr(53):
    print(txt,"is special charechter")
elif int(txt)>=0 or int(txt)<0:
    print(txt,"is number")
else:
    print("value is incorrect")