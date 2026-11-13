import os
os.system('cls')

def verificar_positivo_negativo(numero):
    if numero > 0:
        return "O valor é positivo."
    elif numero < 0:
        return "O valor é negativo."
    else:
        return "O valor é zero (neutro)."

numero = int(input('Digite um número: '))

resultado = verificar_positivo_negativo(numero)
print(f' o número: {numero} é {resultado}')
