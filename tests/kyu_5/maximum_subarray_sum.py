def maxSequence(arr):
    if len(arr) == 0:
        return 0
    else:
        temp = 0
        max_sum = arr[0]
        for i in range(0, len(arr)):
            temp = max(arr[i], arr[i] + temp)
            if temp > max_sum:
                max_sum = temp
        return max_sum

