# 4. Write a python program to create a function that checks whether a passed string is
# palindrome or not.

def isPalindrom(string):
    left_pos=0
    right_pos=len(string)-1
    
    while right_pos>=right_pos:
        if not string[left_pos] == string [right_pos]:
            return False
        left_pos +=1
        right_pos -=1
    return True
print(isPalindrom('aza'))