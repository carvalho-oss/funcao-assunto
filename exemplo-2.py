import os
os.system ('cls')

def mostrar_saudacao(nome, idade):
    print(f'{nome}tem {idade} anos.')

print('= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

print('\n= EXIBINDO DADOS =')
mostrar_saudacao(nome, idade)