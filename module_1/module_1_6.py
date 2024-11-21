my_dict = {'Max': 2000, 'Alex': 2001, 'Ivan': 2002}
print('Dict: ', my_dict)
print(f"Existing value: {my_dict['Max']}")
print(f'Not existing value: {my_dict.get("Denis")}')
my_dict.update({'Sam': 2003,
                'John': 2004})
a = my_dict.pop('Ivan')
print(f"Deleted value: ,{a}")
print(f'Modified dictionary: {my_dict}')

my_set = {1, 2, 3, True, 'a', 'b', 'a'}
print(f'Set: {my_set}')
my_set.add(4)
my_set.add('False')
my_set.remove(1)
print(f'Modified set: {my_set}')