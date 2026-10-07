# Recursion basics

'''
Tail Recursion

When the job or printing or returning is done first, and then the recursive function is called

'''

count = 0

def func():
    if count == 5:
        return
    print(count)
    count += 1
    func()

'''

Head Recursion

When the recursive function is called first, and then the job is done of printing or returning
'''

def func():
    if count == 5:
        return
    count+= 1
    func()
    print(count)