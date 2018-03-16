def high_and_low(numbers):
    numbers = [int(numb) for numb in numbers.split()]
    return "{} {}".format(max(numbers), min(numbers))
