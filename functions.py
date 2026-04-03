import pandas as pd

def cadastrar_produto(df_produtos):
    
    while True:
        c_id = input('Código ID: ')
        if (df_produtos['ID'] == c_id).any():
            print('Código já existente, utilize outro')
        else:
            break
        
    while True:
        nome = input('Nome do Produto: ')
        if (df_produtos['PRODUTO'] == nome).any():
            print('Nome já existente, utilize outro')
        else:
            break
    
    while True:
        try:
            preco = float(input('Valor: '))
            break
        except ValueError:
            print('Entrada inválida, tente novamente')
    
    while True:
        try:
            quant = int(input('Quantidade em Estoque:'))
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
    
    filtro = input('\nInforme código ID do produto: ')
    
    if (df_produtos["ID"] == filtro).any():
        
        conf = input(f"Deseja deletar produto {filtro}? \ns/n")
        if conf == 's':
            df_produtos = df_produtos.drop(df_produtos[filtro].index)
        elif conf == 'n':
            print('Operação cancelada')
        else:
            print('Operação inválida')
            
    else:
        print(f'Código ID {filtro} não existente')
    
    return df_produtos

def registrar_entrada(df_produtos):
    
    filtro = input('\nInforme código ID do produto: ')
    
    if (df_produtos["ID"] == filtro).any():
        
        while True:
            try:
                entrada = int(input('Informe o número de entrada de estoque:'))
                break
            except ValueError:
                print('Valor inválida, tente novamente!')
        
        entrada = int(df_produtos.loc[df_produtos['ID'] == filtro, 'QUANTIDADE']) + int(entrada)
        df_produtos.loc[df_produtos['ID'] == filtro, 'QUANTIDADE'] = entrada
        
    else:
        print(f'Código ID {filtro} não existente')
            
    return df_produtos
     
def registrar_saida(df_produtos):
    
    filtro = input('\nInforme código ID do produto: ')
    
    if (df_produtos["ID"] == filtro).any():
        
        while True:
            try:
                saida = int(input('Informe o número de saida de estoque:'))
                break
            except ValueError:
                print('Valor inválida, tente novamente!')
        
        saida = int(df_produtos.loc[df_produtos['ID'] == filtro, 'QUANTIDADE']) - int(saida)
        df_produtos.loc[df_produtos['ID'] == filtro, 'QUANTIDADE'] = saida
        
    else:
        print(f'Código ID {filtro} não existente')
            
    return df_produtos
    
    
def registrar_saída(df_produtos):
    return df_produtos
