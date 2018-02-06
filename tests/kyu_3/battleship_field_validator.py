def validateBattlefield(field):
    s = [3,3,6,1,1,3,1,1,1,0]
    for i in range(len(field)):
        if sum(field[i]) != s[i]: return False
    return True
