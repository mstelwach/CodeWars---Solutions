def find_uniq(arr):
    keys = {}
    for e in arr:
        keys[e] = 1
        a = keys.keys()
    unique = [i for i in a if arr.count(i) <= 1]
    return unique[0]

