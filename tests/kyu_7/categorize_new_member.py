def openOrSenior(data):
    list = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            i = 'Senior'
            list.append(i)
        else:
            i = 'Open'
            list.append(i)
    return list
