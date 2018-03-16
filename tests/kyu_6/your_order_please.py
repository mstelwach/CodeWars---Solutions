def order(sentence):
    words = sentence.split()
    return ' '.join([word for i in range(1,10) for word in words if str(i) in word])


