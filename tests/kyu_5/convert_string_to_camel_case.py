def to_camel_case(text):
    text_list = text.replace('-', '_').split('_')
    answer_list = [text_list[0], ]
    for word in text_list[1:]:
        answer_list.append( word.title() )
    return ''.join(answer_list)

