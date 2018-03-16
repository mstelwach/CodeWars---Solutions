def is_square(n):
    if n == 1:
        return True
    low = 0
    high = n // 2
    root = high
    while root * root != n:
       root = (low + high) // 2
       if low + 1 >= high:
          return False
       if root * root > n:
          high = root
       else:
          low = root
    return True

