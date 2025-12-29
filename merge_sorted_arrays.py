arr1 = [1, 2, 5, 9]
arr2 = [3, 4, 5, 6, 9]
arr3 = []

# arr3 = arr1 + arr2
# arr3.sort()
# print(arr3)

i, j, k = 0, 0, 0
n1 = len(arr1)
n2 = len(arr2)

while(i < n1 and j < n2):
    if(arr1[i] < arr2[j]):
        arr3[k] = arr1[i]
        i+=1
        k+=1
    else:
        arr3[k] = arr1[j]
        j+=1
        k+=1
        
while(i < n1):
    arr3[k] = arr1[i]
    k+=1
    i+=1

while(j < n2):
    arr3[k] = arr2[j]
    j+=1
    k+=1