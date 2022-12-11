print('Taxa de crescimento 2.0:')

resposta = True
while resposta == True:
    populacao_a = 0
    taxa_crescimento_a = 0
    populacao_b = 0
    taxa_crescimento_b = 0 

    while populacao_a <= 0 or taxa_crescimento_a <= 0:
        ler_populacao_a = input('Digite a quantidade de habitantes do país "A": ')
        ler_taxa_crescimento_a = input('Digite a taxa de crescimento do país "A"(%): ')

        populacao_a = int(ler_populacao_a)
        taxa_crescimento_a = float(ler_taxa_crescimento_a)

    while populacao_b <= 0 or taxa_crescimento_b <= 0:
        ler_populacao_b = input('Digite a quantidade de habitantes do país "B": ')
        ler_taxa_crescimento_b = input('Digite a taxa de crescimento do país "B"(%): ')

        populacao_b = int(ler_populacao_b)
        taxa_crescimento_b = float(ler_taxa_crescimento_b)

    anos = 0

    taxa_crescimento_a /= 100
    taxa_crescimento_b /= 100

    while populacao_a <= populacao_b:
        populacao_a = populacao_a + (populacao_a * taxa_crescimento_a)
        populacao_b = populacao_b + (populacao_b * taxa_crescimento_b)
        anos += 1

    print(f'É necessário {anos} anos para que a população "A" ultrapasse a população "B".') 

    while True:
        resposta = input('Deseja repetir a operação: 1 - Sim : 2 - Não: ')
        if resposta == '1':
            resposta = True
            break
        elif resposta == '2':
            resposta == False
            break
        else:
            print('Opção inválida!')    

