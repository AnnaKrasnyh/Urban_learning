from  random import randint

def code():
    number = randint(3, 20)
    print(f'первое число {number}')

    for i in range(1,number):
        for j in range(i, number):
            if number % (i + j) == 0 and i != j :
                print(f'{i}-{j} ', end = '')
code()

