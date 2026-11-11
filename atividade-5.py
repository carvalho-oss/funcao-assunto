import os
os.system('cls')

def meumodo_exibir_tabuada(numero):
    print(f"\n--- Tabuada do {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2d} = {resultado}")

# Solicita o número ao usuário
num = int(input("Digite um número para ver a tabuada: "))

# Chama a função para exibir o resultado
meumodo_exibir_tabuada(num)