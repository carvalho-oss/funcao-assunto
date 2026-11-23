from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class cliente:
    nome =   str
    telefone: int
    email: str

lista_clientes = []

# SOLICITANDO DADOS.
for i in range(2):
    dados_do_cliente = cliente(
        nome= input('Digite seu nome: '),
        telefone= input('Digite seu telefone: '),
        email= input('Digite seu email: ')
    )
lista_clientes.append(dados_do_cliente)

print('\nEXIBINDO DADOS')
for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'idade: {cliente.telefone}')
    print(f'email: {cliente.email}')
    print('='*15)
    
