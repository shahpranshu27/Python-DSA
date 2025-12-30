arr = [1, 2, 3, 4, 2, 3, 5, 1, 3, 4, 5, 6]
# arr = [1, 1, 2]
count = 0
arr.sort()
for i in range(len(arr)-1, 0, -1):
    if arr[i] == arr[i-1]:
        count += 1
        arr.pop(i)

print("len(arr) ------ ", len(arr))