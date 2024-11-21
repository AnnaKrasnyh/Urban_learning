def get_matrix (n, m, value):
    matrix = []
    if n > 0 and m > 0 and value > 0:
        for i in range(n):
            suppor_list = []
            matrix.append(suppor_list)
            for j in range(m):
                suppor_list.append(value)
    return matrix

n = int(input('Введите кол-во строк'))
m = int(input('Введите кол-во столбцов'))
value = int(input('Введите значение'))

print(get_matrix(n, m, value))