print('Validação de informações:')

nome = input('Digite o seu nome (maior que 3 caracteres): ')
ler_idade = input('Digite a sua idade (entre 0 e 150): ')
ler_salario = input('Digite o seu salário (maior que 0): ')
sexo = input('Digite o seu sexo ("f" ou "m"): ')
estado_civil = input('Digite o seu estado civil ("s", "c", "v", "d"):')

idade = int(ler_idade)
salario = float(ler_salario)

while len(nome) < 4:
    print('Nome inválido!')
    nome = input('Digite o seu nome (maior que 3 caracteres): ')

while idade < 0 or idade > 150:
    print('Idade inválida!')
    ler_idade = input('Digite a sua idade (entre 0 e 150): ')
    idade = int(ler_idade)

while salario < 0:
    print('Salário inválido!')
    ler_salario = input('Digite o seu salário (maior que 0): ')
    salario = float(ler_salario)

while sexo != 'f' and sexo != 'm':
    print('Sexo inválido!') 
    sexo = input('Digite o seu sexo ("f" ou "m"): ')

while estado_civil != 's' and estado_civil != 'c' and \
    estado_civil != 'v' and estado_civil != 'd': 
    print('Estado Civil inválido!') 
    estado_civil = input('Digite o seu estado civil ("s", "c", "v", "d"): ')

print('Todas as informações são válidas!')

