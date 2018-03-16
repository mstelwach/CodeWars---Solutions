def is_valid_IP(strng):
    number = [int(i) for i in strng.split('.') if i.isdigit() and i[0] != '0' or i == '0']

    if len(number) == 4 and max(number) <= 255:
        return True
    else:
        return False

