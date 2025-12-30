from itertools import permutations

def nextPermutation(nums):
    perms = sorted(set(permutations(nums)))
    
    print(perms)
    
    current = tuple(nums)
    for i in range(len(perms)):
        if perms[i] == current:
            if i == len(perms) - 1:
                return list(perms[0])
            return list(perms[i+1])
        
    return nums
print(nextPermutation([1,3,2]))