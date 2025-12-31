num = input().strip()
digit = input()
ans = []

for i in range(len(num)):
    if num[i] == digit:
        t = num[0:i] + num[i+1:]
        ans.append(int(t))
        
print(str(max(ans)))