def perimeter(n):
    fib = []
    a = 0
    b = 1
    for i in range(n+2):
        fib.append(a)
        a, b = b, a + b
    return sum(fib[1::]) * 4

