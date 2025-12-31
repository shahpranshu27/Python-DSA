'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC12

(, ), [, ], {, }
'''

s = input().strip()

stack = []

for i in range(len(s)):
    ch = s[i]
    
    if ch== "(" or ch == "{" or ch == "[":
        stack.append(ch)
        
    else:
        if not stack:
            print(i+1)
            exit()
        
        top = stack.pop()
        
        if (ch == ")" and top != "(") or (ch == "]" and top != "[") or (ch == "}" and top != "{"):
            print(i+1)
            exit()
    
if stack:
    print(len(s))
else:
    print(0)