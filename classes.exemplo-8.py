from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class cliente:
    nome =   str
    telefone: int
    email: str

    def mostrar_dados(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print(f'email: {self.email}')
        print('='*15)


# FUNÇÃO PARA IDADE.
    def mostrar_nome_idade(sef):
    print(f'nome: {self.nome}')
    print(f'telefone: {self.idade}')
    print('='*15)


# FUNÇÃO SOMENTE PARA ENVIAR TELEFONE..
    def whatsApp_marketing(self):
        print(f'nome: {self.nome}')
        print(f'telefone: {self.telefone}')
        print('='*15)



lista_clientes = []

# SOLICITANDO DADOS.
for i in range(2):
    dados_do_cliente = cliente(
        nome= input('Digite seu nome: '),
        telefone= input('Digite seu telefone: '),
        email= input('Digite seu email: ')
    )
    lista_clientes.append(dados_do_cliente)
print('\n= EXIBINDO DADOS =')
for i in lista_clientes:
    cliente.mostrar_dados()
print('\n= EXIBINDO DADOS =')
for i in lista_clientes:
    cliente.telefone_marketing_marketing()
