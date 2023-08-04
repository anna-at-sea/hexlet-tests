def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    print(f'{first_char}{rest_substring}')
    return f'{first_char}{rest_substring}'
