def land_perimeter(arr):
    sum = 0
    for word in arr:
        for i in word:
            if i == 'X':
                i = 4
                sum += i

    for word in arr:
        for i in range(len(word)-1):
            if word[i] == word[i+1] and word[i+1] == 'X':
                sum -= 2

    for word in zip(*arr):
        for i in range(len(word)-1):
            if word[i] == word[i+1] and word[i+1] == 'X':
                sum -= 2
    return "Total land perimeter: {}".format(sum)

