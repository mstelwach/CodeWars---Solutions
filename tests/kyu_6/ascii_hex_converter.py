import codecs

class Converter():

    @staticmethod
    def to_ascii(h):
        return codecs.decode(codecs.decode(h, "hex"), 'ascii')
    @staticmethod
    def to_hex(s):
        s = list(s)
        array = []
        for i in s:
            i = format(ord(i), "x")
            array.append(i)
        return ''.join(array)
print(Converter.to_hex("Look mom, no hands"))
print(Converter.to_ascii("4c6f6f6b206d6f6d2c206e6f2068616e6473"))

