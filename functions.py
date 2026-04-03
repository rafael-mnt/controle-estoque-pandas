import pandas as pd



def cadastrar_produto(df_produtos):
    
    c_id = input('Código ID: ')
    nome = input('Nome do Produto: ')
    
    while True:
        try:
            preco = float(input('Valor: '))
            break
        except ValueError:
            print('Entrada inválida, tente novamente')
    
    while True:
        try:
            quant = int(input('Quantidade em Estoque: '))
            break
        except ValueError:
            print('Entrada inválida, tente novamente')
    
    novo = pd.DataFrame({
        'ID': [c_id],
        'PRODUTO': [nome],
        'PREÇO': [preco],
        'QUANTIDADE': [quant]
    })
    
    
    
    df_produtos = pd.concat([df_produtos, novo], ignore_index=True)
    
    return df_produtos



def excluir_produto(df_produtos):
    
    id_ex = input('\nInforme o ID do produto a ser deletado: ')
    filtro = df_produtos["ID"] == id_ex
    df_produtos = df_produtos.drop(df_produtos[filtro].index)
    
    return df_produtos



def registrar_entrada(df_produtos):
    return df_produtos
    
    
    
def registrar_saída(df_produtos):
    return df_produtos