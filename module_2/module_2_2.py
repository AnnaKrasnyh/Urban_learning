first = int(input('1 число: '))
second = int(input('2 число: '))
third  = int(input('3 число: '))
if first == second == third:
    print(3)
elif first==second!=third or first==third!=second or first!=second==third:
    print(2)
else:
    print(0)

