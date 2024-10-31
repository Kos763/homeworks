def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    str_num = 0
    start_byte = file.seek(0)
    for string in strings:
        file.write(f'{string}\n')
        str_num += 1
        key = (start_byte, str_num)
        strings_positions[key] = string
        start_byte = file.tell()
    file.close()
    return strings_positions


file_name = 'test.txt'
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
