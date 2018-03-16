def move_zeros(array):
    arr_zero = [i for i in array if i is 0 or type(i) == float]
    arr_int = [i for i in array if i != 0 or type(i) == bool]
    return arr_int + arr_zero

