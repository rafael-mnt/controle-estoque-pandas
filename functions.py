import pandas as pd

def valor_existe(coluna, valor):
    return (coluna == valor).any()

def pedir_valor_unico(coluna, texto):

    while True:
        valor = input(texto)
        if valor_existe(coluna, valor):
            print('Entrada já existente, utilize outra')
        else:
            return valor

def pedir_tipo_variavel(tipo, texto):

    while True:
        try:
            valor = tipo(input(texto))
            return valor
        except ValueError:
            print('Entrada inválida, tente novamente')

def cadastrar_produto(c_id, nome, preco, quant, df_produtos):
    
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

def entrada_saida_estoque(opcao, c_id, quant, df_produtos):

    if (df_produtos["ID"] == c_id).any():
        
        if opcao == 'entrada':
            entrada = int(df_produtos.loc[df_produtos['ID'] == c_id, 'QUANTIDADE'].iloc[0]) + int(quant)
            df_produtos.loc[df_produtos['ID'] == c_id, 'QUANTIDADE'] = entrada
            return df_produtos
        
        elif opcao == 'saida':
            saida = int(df_produtos.loc[df_produtos['ID'] == c_id, 'QUANTIDADE'].iloc[0]) - int(quant)
            if saida < 0:
                print('Não é possível quantidade negativa em estoque, operação cancelada')
                return df_produtos
            else:
                df_produtos.loc[df_produtos['ID'] == c_id, 'QUANTIDADE'] = saida
                return df_produtos
        
    else:
        print(f'Código ID {c_id} não existente')
        return df_produtos
