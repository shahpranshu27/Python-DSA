n = int(input("enter n: "))

# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print("\n")

for i in range(n):
    print("*" * (i+1))