arr = [1, 2, 3, 4, 5, 6, 7]
k = int(input("Enter number of rotations: "))

k = k % len(arr)  # In case k is greater than array length

rotated_arr = arr[k:] + arr[:k]
print(rotated_arr)