def remove_smallest(numbers):
    if numbers == []:
        return numbers
    else:
        numbers.remove(min(numbers))
        return numbers

