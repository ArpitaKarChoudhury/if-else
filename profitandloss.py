# 17. Write a python program to calculate profit or loss.
_mrp=int(input("enter market amount"))
_slp=int(input("enter seling ammount"))
if _mrp<_slp:
    print("profit")
elif _slp<_mrp:
    print("loss")
else:
    print("thank you")