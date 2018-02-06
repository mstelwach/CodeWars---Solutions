SYMBOLS = [
    ('A', '.-'),
    ('B', '-...'),
    ('C', '-.-.'),
    ('D', '-..'),
    ('E', '.'),
    ('F', '..-.'),
    ('G', '--.'),
    ('H', '....'),
    ('I', '..'),
    ('J', '.---'),
    ('K', '-.-'),
    ('L', '.-..'),
    ('M', '--'),
    ('N', '-.'),
    ('O', '---'),
    ('P', '.--.'),
    ('Q', '--.-'),
    ('R', '.-.'),
    ('S', '...'),
    ('T', '-'),
    ('U', '..-'),
    ('V', '...-'),
    ('W', '.--'),
    ('X', '-..-'),
    ('Y', '-.--'),
    ('Z', '--..'),
    (' ', '/'),
    ('!', '-.-.--'),
    ('.', '.-.-.-'),
    ('SOS', '...---...'),
]

def decodeMorse(morseCode):
    decode = ''
    morseCode = morseCode.replace('   ', ' / ')
    morseCode = morseCode.split()
    for word in morseCode:
        for letter, symbol in SYMBOLS:
            if word == symbol:
                decode += letter
    if decode[0:2] == '  ': return decode[2::]
    if decode[0] == ' ': return decode[1::]
    return decode