# Responsável por conferir se há duplicidade do input inserido no banco de dados 
def conferir_duplicidade(cursor, tabela, coluna, resposta):
    query = f"""
            SELECT * FROM {tabela}
            WHERE {coluna} = %s;
            """
    
    cursor.execute(query, (resposta,))
    resultado = cursor.fetchone()
    return resultado is None

# Responsável por conferir se há registro do input inserido no banco de dados
def conferir_registro(cursor, tabela, resposta):
    query = f"""
            SELECT id FROM {tabela} WHERE nome = %s;
            """
    
    cursor.execute(query, (resposta,))
    resultado = cursor.fetchone()
    return resultado

# Responsável por validar um input não duplicado no banco de dados
def validar_duplicidade(entrada, cursor, tabela, coluna):
    while True:
        resposta = input(f"{entrada}: ")
        if conferir_duplicidade(cursor, tabela, coluna, resposta):
            return resposta
        print(f'# Aviso: Duplicidade Inválida!\n{entrada} {resposta} já consta em cadastro. Tente novamente!')

# Responsável por extrair o primary key da linha do dado fornecido
def extrair_id(entrada, cursor, tabela):
    while True:
        resposta = input(f"{entrada}: ").upper()
        id = conferir_registro(cursor, tabela, resposta)
        if id is not None:
            return id[0]
        print(f'# Aviso: Erro de Pesquisa!\n{entrada} {resposta} não consta em cadastro. Tente novamente!\n')

# Responsável por validar a formatação int ou float do input
def validar_atributo(texto, atributo):
    while True:
        try:
            return atributo(input(texto))
        except ValueError:
            print(f"# Aviso: Erro de atributo!\nEntrada precisa ser do atributo {atributo}. Tente novamente!")

def conferir_registros_id(cursor, coluna):
    query = f"""
            SELECT {coluna} FROM produto;
            """
    
    cursor.execute(query)
    return cursor.fetchall()

def validar_exclusao(cursor, coluna, id):
    lista = conferir_registros_id(cursor, coluna)
    for item in lista:
        print(item)
        print(id)
        if item[0] == id:
            print(item)
            print
            return False
    return True