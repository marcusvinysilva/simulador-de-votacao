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

