numero = int(input('Digite um número: '))
print(f'TABUADA DE {numero}')
print('-' * 12)
for x in range(1, 11):
    print(f'{numero} x {x:2} = {numero * x}')
    x += 1
print('-' * 12)