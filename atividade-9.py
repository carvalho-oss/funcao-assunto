import os
os.system('cls')

def calcular_soma(num1,num2):
    resultado = num1 + num2
    return resultado

def calcular_subtracao(num1,num2):
    resultado = num1 - num2
    return resultado

def calcular_multiplicacao(num1,num2):
    resultado =num1 * num2
    return resultado

def calcular_divisao(num1,num2):
    if num2 == 0:
        return ' Atenção, divisão por zero'
        return num1 / num2

num1 = float(input(' Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print(f"Soma:", calcular_soma(num1,num2))
print(f"Subtração:", calcular_subtracao (num1,num2))
print(f"Multiplicação:", calcular_multiplicacao(num1,num2))
print(f"Divisão:", calcular_divisao(num1,num2))