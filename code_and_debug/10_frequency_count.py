# Frequency counter

arr = [1,2,5,6,3,4,6,2,4,5,7,3,4,5]
d = {}

# for i in range(0, len(arr)):
#     if arr[i] in d:
#         d[arr[i]] += 1
#     else:
#         d[arr[i]] = 1

# print(d)

for i in arr:
    d[i] = d.get(i, 0) + 1
    
print(d)