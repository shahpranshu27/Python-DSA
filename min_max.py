arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_ele = arr[0]
max_ele = arr[1]

count = 0
for i in range(2, len(arr)):
    if arr[i] > max_ele:
        max_ele = arr[i]
    if arr[i] < min_ele:
        min_ele = arr[i]
    count += 1
    
print("Minimum element is:", min_ele)
print("Maximum element is:", max_ele)
print("Number of comparisons made:", count)