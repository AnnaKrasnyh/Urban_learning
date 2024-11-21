def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(3, 'list', False)

values_list = ['Apple', 2, False]
values_dict = {'a': 1, 'b': 'string', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [1, 'String']

print_params(*values_list_2, 42)