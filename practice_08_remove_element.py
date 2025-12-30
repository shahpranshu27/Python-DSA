# arr = [1, 2, 3, 2, 4, 2, 5, 6, 2]
arr = [0,1,2,2,3,0,4,2]
val = 2

j = 0
for i in range(len(arr)):
    if arr[i] != val:
        arr[j] = arr[i]
        j+=1
        
print(j)
print(arr)