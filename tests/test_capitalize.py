from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Function error!')

if capitalize('') != '':
    raise Exception('Function error!')

print('All tests passed!')
