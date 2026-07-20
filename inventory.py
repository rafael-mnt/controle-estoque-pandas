from functions import extrair_estoque_atual

def registrar_movimento(conexao, cursor, produto_id, tipo, quantidade, observacao):

    estoque_atual = extrair_estoque_atual(cursor, produto_id)
    atualizar_estoque_atual(conexao, cursor, produto_id, tipo, quantidade, estoque_atual)

    query = """
            INSERT INTO estoque (produto_id, tipo, quantidade, observacao)
            VALUES (%s, %s, %s, %s);
            """
    
    cursor.execute(query, (produto_id, tipo, quantidade, observacao))
    conexao.commit()

def atualizar_estoque_atual(conexao, cursor, produto_id, tipo, quantidade, estoque_atual):

    if tipo == "Entrada":
        quantidade = int(estoque_atual) + quantidade
    if tipo == "Saída":
        quantidade = int(estoque_atual) - quantidade

    query = """
            UPDATE produto SET estoque_atual = %s WHERE id = %s;
            """

    cursor.execute(query, (quantidade, produto_id))
    conexao.commit()