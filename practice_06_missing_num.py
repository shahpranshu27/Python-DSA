arr = [1, 2, 4, 5, 6, 8, 9, 7, 3]
n = len(arr) + 1

for i in range(1, n+1):
    if i not in arr:
        print("Missing number is:", i)