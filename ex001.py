print('Nota entre 0 e 10:')

nota = input('Digite uma nota entre 0 e 10: ')
nota_f = float(nota)

while nota_f < 0 or nota_f > 10:
    print('Valor inválido!')
    nota = input('Digite uma nota entre 0 e 10: ')
    nota_f = float(nota)

print('Valor válido!')

