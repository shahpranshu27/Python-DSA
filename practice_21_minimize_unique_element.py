'''
https://www.codechef.com/practice/course/infosys-pyq/INFOSYS04/problems/QQQUOC16?tab=statement
'''

from collections import Counter

x = int(input().strip())
l = list(map(int, input().split()))

freq = Counter(l)

freq_list = sorted(freq.values())
unique_count = len(freq_list)

for f in freq_list:
    if x >= f:
        x -= f
        unique_count -= 1
    else:
        break

print(unique_count)