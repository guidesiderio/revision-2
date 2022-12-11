print('Maior número:')

maior = 0
for i in range(1, 6):
    ler_valor = input('Digite um valor: ')
    valor = float(ler_valor)
    if valor >= maior:
        maior = valor

print(f'Maior = {maior}')  

