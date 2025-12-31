'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC10?tab=statement
'''

# num = "5624381275"
num = "99999999"

sq_num = []

for i in range(len(num)):
    if i%2 == 1:
        sq_num.append(int(num[i])**2)

print(''.join(str(item) for item in sq_num)[:4])

# print(sq_num)