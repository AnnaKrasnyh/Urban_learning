calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    tup =(len(string), string.upper(), string.lower())
    return tup

def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in list_to_search:
        if string.lower() == i.lower():
            flag = True
    if flag:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)