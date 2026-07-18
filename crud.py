def cadastrar_categoria(conexao, cursor, nome):
    query = """
            INSERT INTO categoria (nome) 
            VALUES (%s); 
            """

    cursor.execute(query,(nome,))
    conexao.commit()
    print("- Categoria cadastrada com sucesso! -")
    
def cadastrar_produto(conexao, cursor, nome_produto, nome_categoria, nome_fornecedor, preco, estoque_minimo):
    query = """
            INSERT INTO produto (nome, categoria_id, fornecedor_id, preco, estoque_minimo)
            VALUES (%s, %s, %s, %s, %s);
            """

    cursor.execute(query, (nome_produto, nome_categoria, nome_fornecedor, preco, estoque_minimo))
    conexao.commit()
    print("- Produto cadastrado com sucesso! -")

def cadastrar_fornecedor(conexao, cursor, nome_fornecedor, cpf_cnpj, telefone, email):
    query = """
            INSERT INTO fornecedor (nome, cpf_cnpj, telefone, email)
            VALUES (%s,%s,%s,%s);
            """
    
    cursor.execute(query, (nome_fornecedor, cpf_cnpj, telefone, email))
    conexao.commit()
    print("- Fornecedor cadastrado com sucesso! -")

# Responsável por alterar os dados solcitados do usuário pós confirmação do mesmo
def alterar_dados(conexao, cursor, tabela, coluna, id, item_novo):
    if confirmar_alteracao():
        query = f"""
                UPDATE {tabela} SET {coluna} = %s WHERE id = %s;
                """
    
        cursor.execute(query, (item_novo, id))
        conexao.commit()
        print("- Alteração realizada com sucesso! -")
    else:
        print("# Aviso: Alteração de produto cancelada!")
    
# Responsável por confirmar alteração solicitada pelo usuário
def confirmar_alteracao():
    while True:
        confirmacao = input("\nDeseja prosseguir com a alteração? S(Sim) / N(Não)\nConfirmação: ").lower()
        if confirmacao == "s":
            return True
        elif confirmacao == "n":
            return False
        else:
            print("\n# Aviso: Erro de entrada!\nResponda a confirmação com 'S' para Sim e 'N' para Não.\n")

def excluir_dado(conexao, cursor, tabela, id): 
    if confirmar_exclusao():
        query = f"""
                DELETE FROM {tabela} WHERE id = %s;
                """
    
        cursor.execute(query, (id,))
        conexao.commit()
        print("- Exclusão realizada com sucesso! -")
    else:
        print("# Aviso: Alteração de produto cancelada!")

def confirmar_exclusao():
    while True:
        confirmacao = input("\nDeseja prosseguir com a exclusão?\n# AVISO: ESSA AÇÃO NÃO PODERÁ SER DESFEITA APÓS CONFIMAÇÃO!\n S(Sim) / N(Não)\nConfirmação: ").lower()
        if confirmacao == "s":
            return True
        elif confirmacao == "n":
            return False
        else:
            print("\n# Aviso: Erro de entrada!\nResponda a confirmação com 'S' para Sim e 'N' para Não.\n")
