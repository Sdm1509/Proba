nom = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
cif = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
ch = ''
x = int(input('Введите число в десятичной форме: '))
for i in range(len(cif)):
    ch += (x // nom[i])*cif[i]
    x -= nom[i]*(x // nom[i])
print(ch)

