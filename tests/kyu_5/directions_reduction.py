def dirReduc(arr):
    directions = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 
'WEST': 'EAST'}
    final_direction = []
    for i in arr:
        if len(final_direction) == 0:
            final_direction.append(i)
        else:
            if final_direction[len(final_direction)-1] == directions[i]:
                final_direction.pop()
            else:
                final_direction.append(i)
    return final_direction

