def decomp(n):
    primes = [i for i in range(2, n+1) if all(i % j != 0 for j in range(2, i))]
    factorial = 1
    for i in range(n, 0, -1):
        factorial *= i
    total = 0
    result = ''
    for i in primes:
        pass


print(decomp(5))
print(decomp(14))

print(2 ** 11)
print(17**2)