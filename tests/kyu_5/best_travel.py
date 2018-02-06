import itertools

def choose_best_sum(t, k, ls):
    array = list(itertools.combinations(ls, k))
    array_format = [i for i in array if sum(i) <= t]
    if array_format == []:
        return None
    else:
        sum_road = [sum(i) for i in array_format]
        return min(sum_road, key=lambda x: abs(x - t))

