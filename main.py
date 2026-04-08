import pandas as pd
from functions import cadastrar_produto, excluir_produto, entrada_estoque, saida_estoque, pedir_valor_unico, pedir_tipo_variavel, confirmar_id_unico

df_produtos = pd.DataFrame({
    'ID': ['NJQ1627','NMT4639','MPV3588','CBN2845'],
    'PRODUTO': ['Notebook Asus','Notebook Positivo', 'Celular Xiaomi', 'Carregador Samsung'],
    'PREÇO': [3500.00, 1500.00, 1950.00, 35.00],
    'QUANTIDADE': [32, 55, 26, 14]
})

df_produtos = df_produtos.set_index('ID')

while True:

    print('\n== SISTEMA DE ESTOQUE ==')
    print('\nMenu Inicial:')
    print('1 - Cadastrar Produto')
    print('2 - Excluir Produto')
    print('3 - Registrar Entrada')
    print('4 - Registrar Saída')
    print('5 - Visualizar Estoque')
    print('0 - Sair\n')
    
    opcao = input('Selecione a sua opção: ')
    
    if opcao == '1':
        
        nome = pedir_valor_unico(df_produtos['PRODUTO'], 'Produto: ')
        preco = pedir_tipo_variavel(float, 'Valor: ')
        quant = pedir_tipo_variavel(int, 'Quantidade: ')
        
        df_produtos = cadastrar_produto(nome, preco, quant, df_produtos)
        
    elif opcao == '2':

        c_id = input('Código ID: ')
        if confirmar_id_unico(c_id, df_produtos) == True:

            conf = input(f"Deseja mesmo deletar produto {c_id}? \nDigite: Sim / Não\nResposta: ").lower()
            excluir_produto(conf, c_id, df_produtos)
            df_produtos = excluir_produto(c_id, df_produtos)

    elif opcao == '3':

        c_id = input('Código ID: ')
        if confirmar_id_unico(c_id, df_produtos) == True:

            quant = pedir_tipo_variavel(int, 'Informe o número de entrada de estoque: ')
            df_produtos = entrada_estoque('entrada', c_id, quant, df_produtos)
        
    elif opcao == '4':

        c_id = input('Código ID: ')
        if confirmar_id_unico(c_id, df_produtos) == True:

            quant = pedir_tipo_variavel(int, 'Informe o número de saída de estoque: ')
            df_produtos = saida_estoque('saida', c_id, quant, df_produtos)
        
    elif opcao == '5':
        print(f'\n{df_produtos}\n')

    elif opcao == '0':
        break
        
    else:
        print('Entrada inválida, utilize números de 0 a 5!')
        
print('Programa Finalizado')
