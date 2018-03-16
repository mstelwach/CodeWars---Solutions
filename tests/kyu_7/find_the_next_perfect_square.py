def find_next_square(sq):
    perfect_square = int((sq ** 0.5)) ** 2
    if sq == perfect_square:
        next_square = int(sq ** 0.5) + 1
        next = next_square ** 2
        return next
    else:
        return -1
