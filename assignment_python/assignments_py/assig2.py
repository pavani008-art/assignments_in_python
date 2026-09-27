mark1 = int(input("Enter first marks: "))
mark2 = int(input("Enter second marks: "))
mark3 = int(input("Enter third marks: "))

if mark1 > mark2 and mark1 > mark3:
    print("Top marks:", mark1)
elif mark2 > mark1 and mark2 > mark3:
    print("Top marks:", mark2)
else:
    print("Top marks:", mark3)