import re


# Responsável por validar um input não duplicado no banco de dados
def validar_duplicidade(entrada, cursor, tabela, coluna):
    while True:
        resposta = input(f"{entrada}: ")
        if conferir_duplicidade(cursor, tabela, coluna, resposta):
            return resposta
        print(f'# Aviso: Duplicidade Inválida!\n{entrada} {resposta} já consta em cadastro. Tente novamente!')

# Responsável por validar a formatação int ou float do input
def validar_atributo(texto, atributo):

    while True:
        try:
            return atributo(input(texto))
        except ValueError:
            print(f"# Aviso: Erro de atributo!\nEntrada precisa ser do atributo: {atributo}. Tente novamente!")

# Responsável por validar a exclusão de um dado
def validar_exclusao(cursor, coluna, id):
    lista = conferir_registros_id(cursor, coluna)
    for item in lista:
        if item[0] == id:
            return False
    return True

# Responsável por validar CPF sem duplicidade, com a quantidade certa de números e retornar o dado no formato certo
def validar_cpf(entrada, cursor, tabela, coluna):
    while True:
        cpf = validar_duplicidade(entrada, cursor, tabela, coluna)
        regex_cpf = r"^[0-9]{11}$"
        resultado = re.fullmatch(regex_cpf, cpf)
        if resultado:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
            return cpf
        print("# Aviso: CPF inválido! \nPor favor, insira um CPF existente. Apenas números com 11 caracteres")

# Responsável por validar CNPJ sem duplicidade, com a quantidade certa de números e retornar o dado no formato certo
def validar_cnpj(entrada, cursor, tabela, coluna):
    while True:
        cnpj = validar_duplicidade(entrada, cursor, tabela, coluna)
        regex_cnpj = r"^[0-9]{14}$"
        resultado = re.fullmatch(regex_cnpj, cnpj)
        if resultado:
            cnpj = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
            return cnpj
        print("# Aviso: CNPJ inválido! \nPor favor, insira um CNPJ existente. Apenas números com 14 caracteres.")

# Responsável por validar número de telefone, com a quantidade certa de números e retornar o dado no formato certo
def validar_telefone(entrada):
    while True:
        telefone = input(f"{entrada}: ")
        regex_telefone = r"^[0-9]{10,}$"
        resultado = re.fullmatch(regex_telefone, telefone)
        if resultado:
            telefone = f"({telefone[0:2]}) {telefone[2:-4]}-{telefone[-4:]}"
            return telefone
        print("# Aviso: Telefone inválido! \nPor favor, insira um telefone existente. Apenas números com no mínimo 10 caracteres, incluindo DDD")

# Responsável por validar endereço de e-mail, com a quantidade certa de números e retornar o dado no formato certo
def validar_email(entrada):
    while True:
        email = input(f"{entrada}: ")
        regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        resultado = re.fullmatch(regex_email, email)
        if resultado:
            return email
        print("# Aviso: E-mail inválido! \nPor favor, insira um e-mail existente.")

# Responsável por conferir se há registro do input inserido no banco de dados
def conferir_registro(cursor, tabela, resposta):
    query = f"""
            SELECT id FROM {tabela} 
            WHERE nome = %s;
            """
    
    cursor.execute(query, (resposta,))
    resultado = cursor.fetchone()
    return resultado

# Responsável por conferir registros na tabela produto pelo id fornecido 
def conferir_registros_id(cursor, coluna):
    query = f"""
            SELECT {coluna} FROM produto;
            """
    
    cursor.execute(query)
    return cursor.fetchall()

# Responsável por conferir se há duplicidade do input inserido no banco de dados 
def conferir_duplicidade(cursor, tabela, coluna, resposta):
    query = f"""
            SELECT * FROM {tabela}
            WHERE {coluna} = %s;
            """
    
    cursor.execute(query, (resposta,))
    resultado = cursor.fetchone()
    return resultado is None

# Responsável por extrair o primary key da linha do dado fornecido
def extrair_id(entrada, cursor, tabela):
    while True:
        resposta = input(f"{entrada}: ").upper()
        id = conferir_registro(cursor, tabela, resposta)
        if id is not None:
            return id[0]
        print(f'# Aviso: Erro de Pesquisa!\n{entrada} {resposta} não consta em cadastro. Tente novamente!\n')

# Responsável por validar uma quantidade para entrada e saída de estoque, impedindo ser negativo e estoque atual abaixo de zero
def validar_quantidade(cursor, tipo, produto_id):
    while True:
        quantidade = validar_atributo("Quantidade: ", int)
        estoque_atual = extrair_estoque_atual(cursor, produto_id)

        if tipo == "Entrada":
            if quantidade < 0:
                print("# Aviso: Não é possível registrar números negativos!\n")
            else:
                return quantidade

        if tipo == "Saída":
            if quantidade < 0:
                print("# Aviso: Não é possível registrar números negativos!\n")
            else:
                if (quantidade - estoque_atual) < 0:
                    print("# Aviso: Estoque atual não pode ficar negativo!\nRegistre uma nova quantidade.\n")
                else:
                    return quantidade

#Responsável por extrair o estoque atual do produto selecionado
def extrair_estoque_atual(cursor, produto_id):
    query = """
            SELECT estoque_atual FROM produto
            WHERE id = %s
            """
    
    cursor.execute(query, (produto_id,))
    estoque_atual = cursor.fetchone()
    return estoque_atual[0]

def validar_nulo(cursor, tabela):
    query = f"""
            SELECT * FROM {tabela}
            """
    
    cursor.execute(query)
    nulo = cursor.fetchone()
    return nulo is None