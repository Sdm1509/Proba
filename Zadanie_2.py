def hexx(n):
    alf = '0123456789ABCDEF'
    if n == 0:
        return '0'
    else:
        n = abs(n)
        h_x = ''
        while n > 0:
            h_x = alf[n%16] + h_x
            n //= 16
        return h_x

x = int(input('Введите число в десятичном виде: '))
if x < 0:
    print('-' + hexx(x))
else:
    print(hexx(x))
