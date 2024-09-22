

def print_params(a = 1, b = 'Строка', c = True):
    print(a,b,c)

values_list = [38, 'Текст', True]
values_dict = {'a': 5, 'b': 'Hello', 'c': False}

values_list_2 = [54.32, 'Строка' ]

print_params()
print()
print_params('Привет', 25, False)
print()
print_params(b=25)
print()
print_params(c = [1,2,3])
print()
print_params(*values_list)
print()
print_params(**values_dict)
print()
print_params(*values_list_2, 42)
