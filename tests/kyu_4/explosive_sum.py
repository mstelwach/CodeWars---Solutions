def exp_sum(n):
    return e_sum(n, 0, 1)
    
def e_sum(n, current, index):
    if current == n:
        return 1
    if current > n:
        return 0
    
    count = 0
    for i in range(index, n+1):
        count += e_sum(n, current+i, i)
        
    return count
