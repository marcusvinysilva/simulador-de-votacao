# Crie um programa que simule um sistema de votação, ele deve receber votos até que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá da função autoriza_voto()) e o voto que é o número que a pessoa votou. Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o contrário a 2° função deve validar o número que a pessoa escolheu, ela pode escolher de 1 a 5 (crie 3 candidatos para a votação):
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.

def autoriza_voto(ano_nascimento):
    ano_atual = 2021
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'NEGADO'
    elif idade == 16 or idade == 17 or idade >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

def votacao(autorizacao,voto):   
    autorizacao = autoriza_voto(ano_nascimento)
    if autorizacao == 'NEGADO':
        return 'Você não pode votar'
    else:
        if voto == 1:
            dic_candidatos['Pedro'] += 1
        elif voto == 2:
            dic_candidatos['Tiago'] += 1
        elif voto == 3:
            dic_candidatos['João'] += 1
        elif voto == 4:
            dic_candidatos['Nulo'] += 1
        elif voto == 5:
            dic_candidatos['Branco'] += 1
    return 'Seu voto foi computado'
    
dic_candidatos = {'Pedro':0, 'Tiago':0, 'João':0, 'Nulo':0, 'Branco':0}
lista_nome_candidatos = []
for nome,n_votos in dic_candidatos.items():
    lista_nome_candidatos.append(nome)

while True:
    print('='*35)
    print('-'*10, 'ELEIÇÕES 2021', '-'*10)
    print('='*35)
    ano_nascimento = int(input('Informe o ano que você nasceu: '))
    print()
    for i in range(len(lista_nome_candidatos)):
        print(f'[{i+1}] {lista_nome_candidatos[i]}')
    voto = int(input('Informe o número do seu voto: '))
    autorizacao = autoriza_voto(ano_nascimento)
    print()  
    print(votacao(autorizacao,voto))
    print()
    cont = input('Você deseja continuar? [S/N] ').upper()[0]
    while cont not in 'SN':
        cont = input('Você deseja continuar? [S/N] ').upper()[0]
    print()
    if cont == 'N':
        break
for c,v in dic_candidatos.items():
    print(f'{c} recebeu {v} votos.')
print()

import operator

vencedor_nome = max(dic_candidatos.items(), key=operator.itemgetter(1))[0]
vencedor_votos = max(dic_candidatos.items(), key=operator.itemgetter(1))[1]

empates = []
for i in dic_candidatos.items():
    if vencedor_votos == i[1]:  
        empates.append(i[0])

if len(empates) > 1:
    print(f'{" e ".join(empates)} empataram')
    dic_candidatos_2turno = {}
    for i in empates:
        dic_candidatos_2turno[i] = 0

    lista_nome_candidatos_2turno = []
    for nome2,n_votos2 in dic_candidatos_2turno.items():
        lista_nome_candidatos_2turno.append(nome2)

    while True:
        print('='*36)
        print('-'*5, 'ELEIÇÕES 2021 - 2º TURNO', '-'*5)
        print('='*36)
        ano_nascimento = int(input('Informe o ano que você nasceu: '))
        print()
        for i in range(len(lista_nome_candidatos_2turno)):
            print(f'[{i+1}] {lista_nome_candidatos_2turno[i]}')
        voto = int(input('Informe o número do seu voto: '))
        autorizacao = autoriza_voto(ano_nascimento)
        print()  
        print(votacao(autorizacao,voto))
        print()
        cont = input('Você deseja continuar? [S/N] ').upper()[0]
        while cont not in 'SN':
            cont = input('Você deseja continuar? [S/N] ').upper()[0]
        print()
        if cont == 'N':
            break
    for c,v in dic_candidatos_2turno.items():
        print(f'{c} recebeu {v} votos.')
    print()

    vencedor_nome_2turno = max(dic_candidatos_2turno.items(), key=operator.itemgetter(1))[0]
    print(f'{vencedor_nome_2turno} venceu as Eleições 2021')
else:
    print(f'{vencedor_nome} venceu as Eleições 2021')

