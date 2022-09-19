# 5. Write a python program to create a function to find the Min of three numbers.

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))

smallest = 0
if a<b and b<c:
    smallest=a
elif b<c:
    smallest=b
else:
    smallest=c
print(smallest,"is the smallest of three number")