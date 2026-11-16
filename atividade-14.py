import os
os.system('cls')


def calcular_e_mostrar(vetor_notas):
    soma = 0
    for nota in vetor_notas:
        soma += nota
    media = soma / len(vetor_notas)

    print('\n= EXIBINDO NOTAS =')
    for nota in vetor_notas:
        print(f'Nota: {nota}')

    print(f'\nMédia: {media:.2f}')


notas = []

for i in range(3):
    nota = float(input(f'Digite sua {i+1}ª nota: '))
    notas.append(nota)

calcular_e_mostrar(notas)