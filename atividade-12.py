import os
os.system('cls')
from datetime import date

def nascimento(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

print('= SOLICITANDO DADOS =')
ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade = nascimento(ano_nascimento)

print(' EXIBINDO DADOS ')
print(f'Sua idade é: {idade} anos.')
