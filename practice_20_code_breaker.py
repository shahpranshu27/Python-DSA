input_str = input().strip()
pairs = input_str.split(',')

result = ""

for pair in pairs:
    name, code = pair.split(':')
    n = len(name)
    
    valid_digits = []
    
    for ch in code:
        d = int(ch)
        
        if 1 <= d <= n:
            valid_digits.append(d)
            
    if valid_digits:
        max_digit = max(valid_digits)
        result += name[max_digit - 1]
    else:
        result += "X"

print(result)