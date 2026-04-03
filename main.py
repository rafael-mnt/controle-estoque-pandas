import pandas as pd
from functions import *

produtos = {
    'ID': ['N1','N4','M3','C2'],
    'PRODUTO': ['Notebook Asus','Notebook Positivo', 'Celular Xiaomi', 'Carregador Samsung'],
    'PREÇO': [3500.00, 1500.00, 1950.00, 35.00],
    'QUANTIDADE': [32, 55, 26, 14]
}

df_produtos = pd.DataFrame(produtos)
    
while True:
    print(f'\n{df_produtos}\n')

    print('Menu Inicial:')
    print('1 - Cadastrar Produto')
    print('2 - Excluir Produto')
    print('3 - Registrar Entrada')
    print('4 - Registrar Saída')
    print('5 - Visualizar Estoque')
    print('0 - Sair\n')
    
    opcao = input('Selecione a sua opção: ')
    
    if opcao == '0':
        break
    elif opcao == '1':
        df_produtos = cadastrar_produto(df_produtos)
    elif opcao == '2':
        df_produtos = excluir_produto(df_produtos)
    else:
        print('Vamo de novo')
        
print('Programa Finalizado')