import os
os.system('cls')


def logo_senai():
    print('=========')
    print(' SENAI BAHIA')
    print('=========')

def mostrar_dados(nome, email, telefone):
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Telefone: {telefone}')

    logo_senai()
    print('= SOLICITANDO DADOS =')
    nome = input(' Digite seu nome: ')

    logo_senai()
    email = input(' Digite seu email: ')

    logo_senai()
    telefone = input(' Digite seu telefone: ')

    logo_senai()
    print('\n= EXIBINDO DADOS =')
    mostrar_dados(nome, email, telefone)