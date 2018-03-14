def get_issuer(number):
    mastercard_begins = [str(i) for i in range(51, 56)]
    if str(number)[0] == '4' and (len(str(number)) == 13 or len(str(number)) == 16):
        return 'VISA'
    elif (str(number)[0:2] == '34' or str(number)[0:2] == '37') and len(str(number)) == 15:
        return 'AMEX'
    elif str(number)[0:2] in mastercard_begins and len(str(number)) == 16:
        return 'Mastercard'
    elif str(number)[0:4] == '6011' and len(str(number)) == 16:
        return 'Discover'
    else:
        return 'Unknown'
