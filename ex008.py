print('Soma e Média: ')
soma = 0
media = 0
for i in range(1, 6):
    ler_valor = input('Digite um valor: ')
    valor = float(ler_valor)
    soma += valor
    media = soma / i

print(f'Soma = {soma}, Media = {media:.2f}')   

