def get_ans(n, a, p, q, queries):
    count = 0
    
    for x in a:
        if x%p == 0:
            count +=1
        
    answer = 0
    
    for i, new_val in queries:
        i -= 1 # convert to 0 based index
        
        if a[i] % p == 0:
            count -= 1
        
        a[i] = new_val
        
        if a[i] % p == 0:
            count += 1
        
        if count >= 1:
            answer += 1
        
    return answer