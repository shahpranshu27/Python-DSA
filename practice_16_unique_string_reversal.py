'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC09?tab=statement
'''

name = "google"

def removeDuplicates(s):
    seen = set()
    result = []
    
    for char in s:
        if char not in seen: # chech each char if it's there in set or not
            seen.add(char) # since the char is not there, we will add that char in seen, as it's unique. It it will be there already, then we won't add it
            result.append(char)
        
    
    result.reverse() # the result is in list format, so we can reverse it
    return ''.join(result)
    
print(removeDuplicates(name))