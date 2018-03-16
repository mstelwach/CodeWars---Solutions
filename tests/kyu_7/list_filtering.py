def filter_list(l):
    list = []
    for i in l:
        if type(i) == int:
            list.append(i)
    return list
print (filter_list([1, 2, 'a', 'b']))

