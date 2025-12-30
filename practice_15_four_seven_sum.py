'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC08
'''

nums = list(map(int, input().split()))

ind4 = nums.index(4)
ind7 = nums.index(7)

sum_before_4 = sum(nums[:ind4])
print(sum_before_4)

sum_after_7 = sum(nums[ind7+1:])
print(sum_after_7)

sum_ = sum_after_7 + sum_before_4

nums_between = int(''.join(map(str, nums[ind4: ind7+1])))
print(nums_between)

final_result = sum_ + nums_between
print(final_result)