import os
os.system('cls')


def logo_senai():
    print('=========')
    print(' SENAI BAHIA')
    print('=========')

def cadastrar_cliente():
    logo_senai()
    print("=== CADASTRO DE CLIENTE ===")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail: ")
    telefone = input("Digite o telefone: ")
    print("\nCliente cadastrado com sucesso!")
    input("\nPressione Enter para continuar...")
    return nome, email, telefone

def mostrar_dados(nome, email, telefone):
    logo_senai()
    print("=== DADOS DO CLIENTE ===")
    if nome:
        print(f'Nome: {nome}')
        print(f'E-mail: {email}')
        print(f'Telefone: {telefone}')
    else:
        print("Nenhum cliente cadastrado ainda.")
    input("\nPressione Enter para continuar...")

# Variáveis para armazenamento  dos dados do cliente.
nome = ""
email = ""
telefone = ""

while True:
    logo_senai()
    print("1 - CADASTRAR CLIENTE")
    print("2 - MOSTRAR DADOS DO CLIENTE")
    print("3 - SAIR\n")
    
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome, email, telefone = cadastrar_cliente()
        case "2":
            mostrar_dados(nome, email, telefone)
        case "3":
            print("\nSaindo do programa...")
            exit()
        case _:
            print("\nOpção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")
