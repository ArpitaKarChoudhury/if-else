# A shop will give a discount of 10% if the cost of the
# purchased quantity is more than 1000. Ask the user for 
# quantity, Suppose, one unit will cost 100. Judge and print
# total cost for user
item=int(input("enter quantity"))
cost=item*100
if cost>=1000:
    total_cost=cost-10/100
    print("total cost is with discount",total_cost)
else:
    print("total cost=",cost)