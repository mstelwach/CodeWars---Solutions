SYMBOLS = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
]

def solution(roman):
    strng = ''
    for k, v in SYMBOLS:
        for i in range(10,0,-1):
            if v * i <= roman:
                strng += k * i
                roman -= v * i
                if roman == 0:
                    break
    return strng