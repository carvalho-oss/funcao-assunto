import os
os.system('cls')


def inflacao_produto(preco_produto):
    if inflacao >= 100:
        inflacao = preco_produto * 1.20
    else:
        resultado = preco_produto * 1.10
    return resultado

print('= SOLICITANDO DADOS =')
preco_produto = float(input('Digite seu preço: '))

preco_produto = inflacao_produto(preco_produto)

print('\n=  EXIBINDO DADOS =')
print(f'preço inicial: R$ {preco_produto}')
print(f'inflacionando = {preco_produto}')








