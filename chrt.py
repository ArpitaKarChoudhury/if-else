a=input("enter text")
if a>=chr(65) and a<=chr(122):
    print(a)
elif int(a)>=0 and int(a)<=10:
    print("digit")
else:
    print("special charecter")