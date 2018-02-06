import re

def decodeBits(bits):
    bits = bits.strip('0')
    time_unit = min([len(m) for m in re.findall(r'1+|0+', bits)])
    return bits[::time_unit].replace('111', '-').replace('1', '.').replace('0000000', '   ').replace('000', ' ').replace('0', '')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.split('   '))