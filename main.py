import pandas as pd
from functions import cadastrar_produto, excluir_produto, registrar_entrada, registrar_saida
df_produtos = pd.DataFrame({
    'ID': ['N1','N4','M3','C2'],
    'PRODUTO': ['Notebook Asus','Notebook Positivo', 'Celular Xiaomi', 'Carregador Samsung'],
    'PREÇO': [3500.00, 1500.00, 1950.00, 35.00],
    'QUANTIDADE': [32, 55, 26, 14]
})
    
while True:
    
    print('\nMenu Inicial:')
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
    elif opcao == '3':
        df_produtos = registrar_entrada(df_produtos)
    elif opcao == '4':
        df_produtos = registrar_saida(df_produtos)
    elif opcao == '5':
        print(f'\n{df_produtos}\n')
    else:
        print('Entrada inválida, utilize números de 0 a 5!')
        
print('Programa Finalizado')
