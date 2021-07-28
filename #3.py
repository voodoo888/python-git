# Узнать число n
n = input('Введите число n: ')

# найти сумму чисел n + nn + nnn
nn = int(n + n)
nnn = int(n + n + n)
result = int(n) + nn + nnn

print(f'{n} + {nn} + {nnn} = {result}')