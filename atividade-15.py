import os
os.system('cls')

def ler_nota(numero_nota):
    while True:
        nota = float(input(f'Digite a {numero_nota}ª nota (0 a 10): '))
        if 0 <= nota <= 10:
            return nota
        print('Nota inválida! Digite um valor entre 0 e 10.')

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificacao_aprovacao(media):
    if media >= 7.0:
        return 'Aprovado'
    else:
        return 'Reprovado'

nota1 = ler_nota(1)
nota2 = ler_nota(2)

media = calcular_media(nota1, nota2)
situacao = verificacao_aprovacao(media)

print(f'\nMédia: {media}')
print(f'Situação: {situacao}')
