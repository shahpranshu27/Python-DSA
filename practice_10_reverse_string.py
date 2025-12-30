name = "Geek"

# slicing operator
# name = name[::-1]
# print(name)


# backward traversal
# res = []
# for i in range(len(name)-1, -1, -1):
#     res.append(name[i])

# print(''.join(res))


# two pointer
left = 0
right = len(name) - 1

s = list(name)

while left < right:
    s[left], s[right] = s[right], s[left]
    left+=1
    right-=1

print(''.join(s))