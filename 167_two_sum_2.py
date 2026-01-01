numbers = [2,7,11,15]
target = 9

left=0
right=len(numbers) - 1

while left <= right:
    if target == numbers[left] + numbers[right]:
        print([left+1, right+1])
    if numbers[left] + numbers[right] < target:
        left+=1
    else:
        right-=1