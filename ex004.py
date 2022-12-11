populacao_a = 80000
taxa_crescimento_a = 0.03

populacao_b = 200000
taxa_crescimento_b = 0.015

anos = 0

while populacao_a <= populacao_b:
    populacao_a = populacao_a + (populacao_a * taxa_crescimento_a)
    populacao_b = populacao_b + (populacao_b * taxa_crescimento_b)
    anos += 1

print(f'É necessário {anos} anos para que a população "A" ultrapasse a população "B".') 

