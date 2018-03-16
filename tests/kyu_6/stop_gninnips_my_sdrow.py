def spin_words(sentence):
    words = sentence.split()
    list = []
    for word in words:
        if len(word) >= 5:
            pal = word[::-1]
        else:
            pal = word
        list.append(pal)
    return ' '.join(list)
