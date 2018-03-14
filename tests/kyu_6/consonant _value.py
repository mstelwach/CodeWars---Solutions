def solve(s):
    consonant = 'bcdfghjklmnpqrstvwxyz'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for letter in s:
        if letter in consonant:
            result += letter
        else:
            result += ' '
    substrings = result.split()
    consonant_value = [(ascii_lowercase[i], i+1) for i in range(len(ascii_lowercase)) if ascii_lowercase[i] in consonant]

    arr = []
    for strng in substrings:
        max_value = 0
        for value in consonant_value:
            for char in strng:
                if char == value[0]:
                    max_value += value[1]
                    arr.append(max_value)
    return max(arr)
print(solve('zodiacs'))
print(solve('chruschtschov'))

