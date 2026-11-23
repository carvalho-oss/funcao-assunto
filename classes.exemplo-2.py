from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class cliente:
    # NOME DA VARIÁVEL: TIPO VARIÁVEL
    nome: str
    idade: int


# SOLICITANDO DADOS DE UM CLIENTE.
cliente1 = cliente('Marta', 30)

#SOLICITANDO DADOS DO OUTRO CLIENTE.
cliente2 = cliente('José', 40)

print(f'nome: {cliente1.nome}')
print(f'idade: {cliente1.idade}')

print(f'nome: {cliente2.nome}')
print(f'idade: {cliente2.idade}')

