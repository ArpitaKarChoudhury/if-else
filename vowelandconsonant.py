# Write a python program to input any alphabet and check whether it is vowel or consonant.
chr=input("enter character: ")
if chr=="a" or chr=="A" or chr=="e" or chr=="E" or chr=="i" or chr=="I" or chr=="o" or chr=="O" or chr=="u" or chr=="U":
    print(chr,"is a vowel")
elif chr>="A" and chr<="Z" or chr>="a" and chr<="z":
    print(chr,"is a Consonant")
else:
    print(chr,"is not a alphabate")