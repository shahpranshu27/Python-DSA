'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC02
'''

def isPali(num):
    return str(num) == str(num)[::-1]

def reverse_num(num):
    return int(str(num)[::-1])

def find_palindrome(num):
    iterations = 0
    while not isPali(num) and iterations < 1000:
        num = num + reverse_num(num)
        iterations+=1
    return num

num = int(input("enter num: "))
print(find_palindrome(num))