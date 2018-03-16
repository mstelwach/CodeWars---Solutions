def dig_pow(n, p):
    numbers = [int(i) for i in str(n)]
    sum = 0
    for number in numbers:
        number_pow = number ** p
        p += 1
        sum += number_pow
    return int(sum/n) if sum % n == 0 else -1

