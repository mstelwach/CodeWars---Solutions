def is_interesting(number, awesome_phrases):
    criteria = [0, 1, 2]
    if number >= 98:
        for n in range(number, number + 3):
            if n == number and number > 99:
                if n % 10 == 0 and str(n).count('0') >= 2:
                    return criteria[2]
                if all(str(n).count(i) == len(str(n)) for i in str(n)):
                    return criteria[2]
                if str(n)[-1] == '0' and str(n)[-2] == '9':
                    if all(int(str(n)[i - 1]) + 1 == int(str(n)[i]) for i in range(1, len(str(n).replace('0', '')))):
                        return criteria[2]
                if all(int(str(n)[i - 1]) + 1 == int(str(n)[i]) for i in range(1, len(str(n)))):
                    return criteria[2]
                if all(int(str(n)[i-1]) == int(str(n)[i]) + 1 for i in range(1, len(str(n)))):
                    return criteria[2]
                if str(n) == str(n)[::-1]:
                    return criteria[2]
                if n in awesome_phrases:
                    return criteria[2]
            else:
                if n % 10 == 0 and str(n).count('0') >= 2:
                    return criteria[1]
                if all(str(n).count(i) == len(str(n)) for i in str(n)):
                    return criteria[1]
                if str(n)[-1] == '0' and str(n)[-2] == '9':
                    if all(int(str(n)[i - 1]) + 1 == int(str(n)[i]) for i in range(1, len(str(n).replace('0', '')))):
                        return criteria[1]
                if all(int(str(n)[i - 1]) + 1 == int(str(n)[i]) for i in range(1, len(str(n)))):
                    return criteria[1]
                if all(int(str(n)[i - 1]) == int(str(n)[i]) + 1 for i in range(1, len(str(n)))):
                    return criteria[1]
                if str(n) == str(n)[::-1]:
                    return criteria[1]
                if n in awesome_phrases:
                    return criteria[1]
    return criteria[0]