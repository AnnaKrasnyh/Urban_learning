def  calculate_structure_sum(data_structure):
    summ = 0
    if isinstance(data_structure, int | float):
        summ += data_structure
    elif isinstance(data_structure, str):
        summ += len(data_structure)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summ = summ + calculate_structure_sum(key) + calculate_structure_sum(value)
    elif isinstance(data_structure, list | tuple | set):
        for j in data_structure:
            summ += calculate_structure_sum(j)
    return summ


data_structure = [
    [1, 2, 3], # 6
    {'a': 4, 'b': 5}, # 11
    (6, {'cube': 7, 'drum': 8}), #29
    "Hello", # 5
    ((), [{(2, 'Urban', ('Urban2', 35))}]) #48
]


print(calculate_structure_sum(data_structure))