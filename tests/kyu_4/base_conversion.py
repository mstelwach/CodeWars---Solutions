def convert(input, source, target):
    source = 'dec'
    if source == 'dec':
        if target == bin:
            input = int(input)
            return str(bin(input).replace('0b', ''))
        elif target == 'oct':
            input = int(input)
            return oct(input).replace('0o', '')
        elif target == 'hex':
            input = int(input)
            return hex(input).replace('0x', '')


print(convert('15', dec, bin))