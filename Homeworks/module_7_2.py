from pprint import pprint
def custom_write(file_name, strings):
    strings_positions = {}
    x = 0
    for i in strings:
        x += 1
        file = open(file_name, 'a', encoding='utf-8')
        position = file.tell()
        file.write(i + '\n')
        strings_positions[(x, position, i)] = strings
        file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for i in result:
    print(i)