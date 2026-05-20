print("enter marks of 5 subjects")
markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())
tot = markone+marktwo+markthree+markfour+markfive
avg = int(tot/5)
validrange = range(0, 101)
if avg not in validrange:
    print("invalid input!")
elif avg in range(91,101):
    print("your grade is a1")
elif avg in range(81,91):
    print("your grade is a2")
elif avg in range(71,81):
    print("ypur grade is b1")


