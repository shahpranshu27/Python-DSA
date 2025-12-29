nums = [2, 7, 11, 15, 21, 12, 34, 9, 35, 29]
target = 9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# nums.sort(reverse=True)
# sec_max = nums[1]
# for i in range(1, len(nums)):
#     if nums[i] > sec_max:
#         sec_max = nums[i]
# print("second largest number is:", sec_max)