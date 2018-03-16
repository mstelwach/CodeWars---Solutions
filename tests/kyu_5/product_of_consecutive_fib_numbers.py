def productFib(prod):
    arr = []
    a, b = 0, 1
    for i in range(1, 1000):
        a, b = b, a+b
        arr.append(a)
    for j in range(1, len(arr)):
        if arr[j-1] * arr[j] == prod:
            return [arr[j-1], arr[j], True]
        elif arr[j-1] * arr[j] > prod:
            return [arr[j-1], arr[j], False]

