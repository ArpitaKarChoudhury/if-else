# 13. Write a python program to count the total number of 
# notes in a given amount.
_amt=int(input("enter number"))
if _amt!=0:
    a=_amt//2000
    b=_amt%2000
    c=b//500
    d=b%500
    e=d//200
    f=d%200
    g=f//100
    h=f%100
    i=h//50
    j=h%50
    k=j//20
    l=j%20
    m=l//10
    n=l%10
    print("2000 notes=",a,"500 notes=",c,"200 notes=",e,"100 notes=",g,"50 notes =",i,"20 note=",k,"10 notes=",m,"coin=",n)