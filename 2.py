# 2. Write a python program to create a function that takes a number as a parameter and
# checks if the number is prime or not

def check_prime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
        return True
print(check_prime(13))
        