a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while b != 0:
    a, b = b, a%b
print('НОД =', a)