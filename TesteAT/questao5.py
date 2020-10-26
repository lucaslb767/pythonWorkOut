import os
import math

#abre arquivo
file = open('Assessment_PIBs_-_Planilha1.csv', 'r', encoding='utf8')

#le arquivos já em formato de lista
lista_naoTratada = file.readlines()

file.close()

#remove \\n e faz cada string virar uma lista
lista_tratada = []
for n in lista_naoTratada:
    a = n.rstrip()
    a = a.split(',')
    lista_tratada.append(a)

#já separa o label de pais e ano
label_pais_ano = lista_tratada.pop(0)
print(label_pais_ano)


#faz conversao dos valores em inteiro para float
lista_paises = []
for k in lista_tratada:
    pais = []
    pais.append(k.pop(0))

    for a in k:
        pais.append(float(a))

    lista_paises.append(pais)

print(lista_paises)

#LETRA A

def verifica_pais_ano_existe( objeto_procurado,lista_paises =[], label_pais_ano =[]):
    """Percorre lista procurando por match entre valores. Retorna verdadeiro caso alguns dos itens seja igual ao informado"""
    resposta = False

    for pais in lista_paises:
        for elemento in pais:
            if elemento == objeto_procurado:
                resposta = True

    for ano in label_pais_ano:
        if ano == objeto_procurado:
            resposta = True
    return resposta

def solicita_pais(lista_paises):
    """Solicita ao usuário um país e retorna a posição dele na lista de países"""
    pais_selecionado = input("Informe um país: ")

    if verifica_pais_ano_existe(pais_selecionado,lista_paises):
        for pais in lista_paises:
            if pais[0] == pais_selecionado:
                return lista_paises.index(pais)
    else:
        print("pais nao encontrado")
        return solicita_pais(lista_paises)

def solicita_ano(label_pais_ano):
    "Solcita o ano e retorna a posição dele na lista label_pais_ano"
    ano_selecionado = input("Informe um ano: ")

    if verifica_pais_ano_existe(ano_selecionado,[],label_pais_ano):
        return label_pais_ano.index(ano_selecionado)
    else:
        print('ano selecionado não foi encontrado')
        return solicita_ano(label_pais_ano)

def solicita_PIB(lista_paises, label_pais_ano):
    pais_index = solicita_pais(lista_paises)
    pais = lista_paises[pais_index][0]
    ano_index = solicita_ano(label_pais_ano)
    ano = label_pais_ano[ano_index]
    return f'PIB {pais} em {ano}: US${lista_paises[pais_index][ano_index]} trilhões.'

print(solicita_PIB(lista_paises,label_pais_ano))

