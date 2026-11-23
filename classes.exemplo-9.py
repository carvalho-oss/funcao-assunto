from dataclasses import dataclass
import os
os.system('cls')


@dataclass
class paciente:
    nome =   str
    idade = int
    telefone: int
    endereco =str
    
def mostrar_dados(sef):
    print(f'nome: {self.nome}')
    print(f'idade: {self.idade}')
    print(f'telefone: {self.telefone}')
    print(f'endereço: {self.endereco}')

    lista_paciente = []
