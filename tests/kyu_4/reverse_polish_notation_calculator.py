operations = {
    '+': (lambda a, b: a + b),
    '-': (lambda a, b: a - b),
    '*': (lambda a, b: a * b),
    '/': (lambda a, b: a / b),
}

def calc(expr):
    score = []
    for i in expr.split():
        if i in operations:
            a = score.pop()
            b = score.pop()
            score.append(operations[i](b, a))
        else:
            score.append(float(i))
    if score == []: return 0
    else: return score.pop()