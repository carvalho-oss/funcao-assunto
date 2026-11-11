import os
os.system ("cls")

# CRIANDO A FUNÇÃO.
def cabecalho():
    print('\n')
    print('='*15)
    print(' SENAI')
    print('='*15)

cabecalho() # Usando a função.
nome = input('Digite seu nome: ')

cabecalho() # Usando a função.
idade = input('Digite sua idade: ')

cabecalho() # Usando A FUNÇÃO.
print(f'Nome: {nome}')
print(f'Idade:{idade}')