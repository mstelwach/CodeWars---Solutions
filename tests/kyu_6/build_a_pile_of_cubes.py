def find_nb(m):
    n = 0
    sum = 0
    while sum < m:
        sum += n ** 3
        if sum == m:
            return n
        n += 1
    return -1

