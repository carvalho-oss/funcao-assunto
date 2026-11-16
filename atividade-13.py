import os
os.system('cls')

def calcular_media(vetor_notas):
    soma = 0
    for nota in vetor_notas:
        soma += nota
    return soma / len(vetor_notas)

notas = []

for i in range(3):
    nota = float(input(f'Digite sua {i+1}ª nota: '))
    notas.append(nota)


media = calcular_media(notas)
print(f'Sua média é: {media}')