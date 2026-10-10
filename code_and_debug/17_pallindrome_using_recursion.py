'''
Pallindrome check using Recursion
'''

def func(s, left, right):
    if s[left] != s[right]:
        return False
    if left >= right:
        return True
    return func(s, left+1, right-1)

s = "nitin"
print(func(s, 0, len(s)-1))