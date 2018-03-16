def solution(digits):
    arr = []
    if len(str(digits)) > 5:
        for i in range(0,len(str(digits))-4):
            arr.append([str(digits)[i:i+5]])
        return int(''.join(max(arr)))

