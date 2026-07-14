# Responsável por pegar os dados da tabela selecionada no banco de dados
def criar_menu_tabela(cursor, tabela):
    if tabela == "categoria":
        query = """
                SELECT 
                categoria.nome 
                FROM categoria;
                """
        
        cursor.execute(query)
        return cursor.fetchall()
        
    if tabela == "produto":
        query = """
                SELECT 
                produto.nome, 
                categoria.nome,
                fornecedor.nome,
                produto.preco, 
                produto.estoque_atual, 
                produto.estoque_minimo,
                produto.data_de_cadastro
                FROM produto
                INNER JOIN categoria
                ON produto.categoria_id = categoria.id
                INNER JOIN fornecedor
                ON produto.fornecedor_id = fornecedor.id;
                """
        
        cursor.execute(query)
        return cursor.fetchall()

    if tabela == "fornecedor":
        query = """
                SELECT 
                fornecedor.nome,
                fornecedor.cpf_cnpj,
                fornecedor.telefone,
                fornecedor.email
                FROM fornecedor;
                """
        
        cursor.execute(query)
        return cursor.fetchall()

# Responsável por pegar dados da primary key selecinada do banco de dados
def criar_menu_id_unico(cursor, tabela, id):
    if tabela == "categoria":

        query = """
                SELECT 
                categoria.nome 
                FROM categoria
                WHERE id = %s;
                """
        
        cursor.execute(query, (id,))
        return cursor.fetchall()
    
    if tabela == 'produto':

        query = """
                SELECT 
                produto.nome, 
                categoria.nome,
                fornecedor.nome,
                produto.preco, 
                produto.estoque_atual, 
                produto.estoque_minimo,
                produto.data_de_cadastro
                FROM produto
                INNER JOIN categoria
                ON produto.categoria_id = categoria.id
                INNER JOIN fornecedor
                ON produto.fornecedor_id = fornecedor.id
                WHERE produto.id = %s;
                """
    
        cursor.execute(query, (id,))
        return cursor.fetchall()
    
    if tabela == "fornecedor":

        query = """
                SELECT 
                fornecedor.nome,
                fornecedor.cpf_cnpj,
                fornecedor.telefone,
                fornecedor.email
                FROM fornecedor
                WHERE id = %s;
                """
        
        cursor.execute(query, (id,))
        return cursor.fetchall()
    
# Responsável por pegar dados específicos do banco de dados para consultas
def criar_menu_consulta(cursor, tabela_consulta):
    if tabela_consulta == 'categoria':
        query = """
                SELECT 
                categoria.nome 
                FROM categoria
                """
        
        cursor.execute(query)
        return cursor.fetchall()
    
    if tabela_consulta == 'fornecedor':
        query = """
                SELECT
                fornecedor.nome 
                FROM fornecedor
                """
        
        cursor.execute(query)
        return cursor.fetchall()
    
def criar_menu_opcoes(opcoes):

    if opcoes == "menu_principal":
        opcoes_menu_principal = [
        [1, 'Categorias'],
        [2, 'Produtos'],
        [3, 'Fornecedores'],
        [0, 'Sair do Programa']
    ]
        return opcoes_menu_principal
    
    if opcoes == "menu_categorias":
        opcoes_menu_categorias = [
        [1, 'Cadastrar Categoria'],
        [2, 'Alterar Categoria'],
        [3, 'Deletar Categoria'],
        [0, 'Voltar']
    ]
        return opcoes_menu_categorias
    
    if opcoes == "menu_produtos":
        opcoes_menu_produtos = [
        [1, 'Cadastrar Produto'],
        [2, 'Alterar Produto'],
        [3, 'Deletar Produto'],
        [0, 'Voltar']
    ]
        return opcoes_menu_produtos
    
    if opcoes == "menu_fornecedores":
        opcoes_menu_fornecedores = [
        [1, 'Cadastrar Fornecedor'],
        [2, 'Alterar Fornecedor'],
        [3, 'Deletar Fornecedor'],
        [0, 'Voltar']
    ]
        return opcoes_menu_fornecedores
    
    if opcoes == "opcoes_alterar_categoria":
        opcoes_alterar_categoria = [
        [1, 'Alterar Nome'],
        [0, 'Voltar']
    ]
        return opcoes_alterar_categoria
    
    if opcoes == "opcoes_alterar_produto":
        opcoes_alterar_produto = [
        [1, 'Alterar Nome'],
        [2, 'Alterar Categoria'],
        [3, 'Alterar Fornecedor'],
        [4, 'Alterar Preço'],
        [5, 'Alterar Estoque Mínimo'],
        [0, 'Voltar']
    ]
        return opcoes_alterar_produto
    
    if opcoes == "opcoes_alterar_fornecedor":
        opcoes_alterar_fornecedor = [
        [1, 'Alterar Nome'],
        [2, 'Alterar CPF/CNPJ'],
        [3, 'Alterar Telefone'],
        [4, 'Alterar E-mail'],
        [0, 'Voltar']
    ]
        return opcoes_alterar_fornecedor
