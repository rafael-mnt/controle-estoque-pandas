import random
import string

def gerar_id():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=4))
    return letras + numeros

def gerar_id_unico(df_produtos):
    while True:
        novo_id = gerar_id()
        if novo_id not in df_produtos.index:
            return novo_id

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

def cadastrar_produto(nome, preco, quant, df_produtos):
    
    novo_id = gerar_id_unico(df_produtos)

    df_produtos.loc[novo_id] = {
        'PRODUTO': nome,
        'PREÇO': preco,
        'QUANTIDADE': quant
    }
    
    return df_produtos

def excluir_produto(c_id, df_produtos):
    
    if c_id not in df_produtos.index:
        print(f'Código ID {c_id} não existente')
        return df_produtos
        
    conf = input(f"Deseja deletar produto {c_id}? \ns/n")
    if conf == 's':
        df_produtos = df_produtos.drop(c_id)
        print(f'Produto {c_id} deletado com sucesso')
        return df_produtos
    
    elif conf == 'n':
        print('Operação cancelada')
        return df_produtos
    
    else:
        print('Operação inválida')
    
    return df_produtos

def entrada_saida_estoque(opcao, c_id, quant, df_produtos):

    if c_id not in df_produtos.index:
        print(f'Código ID {c_id} não existente')
        return df_produtos
        
    if opcao == 'entrada':
        df_produtos.loc[c_id, 'QUANTIDADE'] += quant
    
    elif opcao == 'saida':
        
        if df_produtos.loc[c_id, 'QUANTIDADE'] - quant < 0:
            print('Não é possível quantidade negativa em estoque, operação cancelada')
            return df_produtos  
        
        df_produtos.loc[c_id, 'QUANTIDADE'] -= quant

    return df_produtos
