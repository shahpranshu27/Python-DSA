# Arrays lec 1 codebasics


# stock_price = [12,24,34,15,20]

# print(stock_price)

# print(stock_price[2]) # O(1)

# print(stock_price.insert(1,23)) # O(n)
# print(stock_price)

# print(stock_price.remove(23)) # O(n)
# print(stock_price)

# ----------------------------------------

# expense = [2200, 2350, 2600, 2130, 2190]

# print(expense[1] - expense[0])

# print(expense[0] + expense[1] + expense[2])

# print(2000 in expense)

# expense.append(1980)
# print(expense)

# expense[3] = expense[3] - 200
# print(expense)

# -----------------------------------------

# heros=['spider man','thor','hulk','iron man','captain america']

# print(len(heros))

# heros.append("black panther")
# print(heros)

# heros.pop()

# heros.insert(3, "black panther")
# print(heros)

# heros[1:3] = ['doc strange']
# print(heros)

# heros.sort()
# print(heros)

# -------------------------------------------

max_num = int(input("enter max number: "))
odd_nums = []
for i in range(1, max_num):
    if i%2 == 1:
        odd_nums.append(i)
        
print(odd_nums)