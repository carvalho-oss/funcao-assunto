from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class cliente:
    # NOME DA VARIÁVEL: TIPO VARIÁVEL
    nome: str
    idade: int
    altura: float
    peso: float

lista_clientes = []

# SOLICITANDO DADOS DE DOIS CLIENTES.
for i in range(2):
    dados_do_clinte = cliente(
        nome= input('\nDigite seu nome: '),
        idade= int(input('Digite sua idade: ')),
        altura= float(input('Digite sua altura: ')),
        peso= float(input('Digite seu peso: '))
        )
    lista_clientes.append(dados_do_clinte)
print('\nEXIBINDO DADOS')
for cliente in lista_clientes:
    print(f'nome: {cliente.nome}')
    print(f'idade: {cliente.idade}')
    print(f'altura: {cliente.altura}')
    print(f'peso: {cliente.peso}')
    print('='*15)
