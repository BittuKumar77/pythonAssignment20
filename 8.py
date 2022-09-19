# 8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.


def stringTest(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original values:",s)
    print("No of upper_case characters:",d["UPPER_CASE"])
    print("No of Lower_case characters:",d["LOWER_CASE"])
stringTest('MySirG is a Biggest Online Education Platform')
