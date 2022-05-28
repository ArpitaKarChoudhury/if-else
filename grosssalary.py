# Write a python program to input basic salary of an employee and
#  calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
b_s=int(input("enter amount"))
if b_s<=10000:
    HRA=b_s//20*100
    DA=b_s//80*100
    g_s=b_s+HRA+DA
    print(g_s,"is gross salary")
elif b_s<=20000:
    HRA=b_s//25*100
    DA=b_s//90*100
    g_s=b_s+HRA+DA
    print(g_s,"is gross salary")
elif b_s>20000:
    HRA=b_s//30*100
    DA=b_s//95*100
    g_s=b_s+HRA+DA
    print(g_s,"is gross salary")
else:
    print("unavailable")