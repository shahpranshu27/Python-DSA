name = "aabc"
name_list = list(name)
print(name_list)
for i in range(1, len(name)):
    print(name_list[i])
    if name_list[i-1] == name_list[i]:
        name_list[i] = "#"

print(''.join(name_list))
print(name)