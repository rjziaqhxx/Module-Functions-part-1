def palindrome(a):
    astr = str(a)
    if astr == astr[::-1]:
        return True
    else:
        return False
    
print(palindrome(1221))
print(palindrome(12345))