print('Validar nome e senha')

nome_usuario = input('Digite o seu nome de usuário: ')
senha = input('Digite a sua senha: ')

while nome_usuario == senha:
    print('Error login! Nome de usuário igual senha')
    nome_usuario = input('Digite o seu nome de usuário: ')
    senha = input('Digite a sua senha: ')

print('Login feito com sucesso!')

