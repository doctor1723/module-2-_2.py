number= int(input("Введите число: " ))
if number % 2 == 0:
    print('first')
if number % 3 == 0 :
    print( 'second')
if number % 4 == 0 :
    print('third')
number = int(input("Введите число :"))
if number % 6 == 0 and number % 4 == 0:
    print('first' , 'second')
else:
    print('third')
number = int(input("Введите число :"))
if number % 7 == 0 or number % 8 == 0 :
    print('first')
elif number % 3 == 0 :
    print('second')
else:
    print('Нет такого числа')

