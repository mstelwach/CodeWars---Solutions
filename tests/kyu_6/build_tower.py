def tower_builder(n_floors):
    list = []
    for i in range(n_floors):
        n_floors -= 1
        list.append(' ' * n_floors + '*' * (i * 2 + 1) + ' ' * n_floors)
    return list

