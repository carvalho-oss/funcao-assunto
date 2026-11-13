import os
os.system('cls')

def calcular_notas(nota1, nota2)
    resultado = nota1 + nota2
    return resultado

    print('= SOLICITANDO NOTAS =')
    nota1 = float(input(' Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))


# USANDO A FUNÇÃO COM PARÂMETROS E
# INSERINDO O RETORNO NA VARIÀVEL SOMA.
soma = calcular_notas(nota1, nota2)



print('\n= EXIBINDO NOTAS =')
print(f'soma: {soma}')
