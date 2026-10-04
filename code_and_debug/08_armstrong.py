# Armstrong number

num = 153
num1 = num
count = 0
arm = 0

# while num > 0:
#     n = num%10
#     count+= 1
#     num = num //10
    
# num = num1

nod = len(str(num))

while num > 0:
    n = num%10
    arm = arm + n ** nod
    num = num // 10

print(arm == num1)