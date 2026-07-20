import datetime

# Responsável por selecionar os títulos da tabela
def selecionar_titulos_tabela(tabela):
    if tabela == "categoria":
        return ["CATEGORIA"]
    if tabela == "produto":
        return ["PRODUTO", "CATEGORIA", "FORNECEDOR", "PREÇO", "ESTOQUE MÍNIMO", "ESTOQUE ATUAL", "DATA DE CADASTRO"]
    if tabela == "fornecedor":
        return ["FORNECEDOR", "CPF/CNPJ", "TELEFONE", "E-MAIL"]
    if tabela == "estoque":
        return ["DATA DE MOVIMENTAÇÃO", "PRODUTO", "EXECUÇÃO", "QUANTIDADE", "OBSERVAÇÃO"]
    if tabela == "opcoes":
        return ["# SELECIONE A OPÇÃO DESEJADA"]

# Responsável por calcular largura da tabela
def calcular_largura_tabela(menu, colunas, titulos):
    larguras = []

    for coluna in range(colunas):
        maior = 0
        for item in menu:
            if len(str(item[coluna])) > maior:
                maior = len(str(item[coluna]))
        larguras.append(maior)

    for coluna in range(colunas):
        if len(str(titulos[coluna])) > larguras[coluna]:
            larguras[coluna] = len(str(titulos[coluna]))

    return larguras

#Responsável por criar as linhas da tabela
def criar_linha_tabela(larguras, colunas):
    linha = "+"

    for coluna in range(colunas):
        linha += f"{"-" * (larguras[coluna] + 2)}+"

    return linha

#Responsável por inserir os títulos da tabela
def inserir_titulos_tabela(titulos, colunas, larguras):
    dados = "|"

    for titulo in range(colunas):
        dados += f" {str(titulos[titulo]):<{larguras[titulo]}} |"

    print(dados)

#Responsável por inserir os dados da tabela
def inserir_dados_tabela(menu, colunas, larguras):

    if len(menu) == 0:
        menu = [["-"] * colunas]

    for item in menu:
        dados = "|"

        for coluna in range(colunas):
            if type(item[coluna]) is datetime.date:
                data = item[coluna].strftime("%d/%m/%Y")
                dados += f" {data:<{larguras[coluna]}} |"
            else:
                dados += f" {str(item[coluna]):<{larguras[coluna]}} |"

        print(dados)

# Responsável por calcular largura da tabela de opções
def calcular_largura_tabela_opcoes(menu, colunas):
    larguras = []

    for coluna in range(colunas):
        maior = 0
        for item in menu:
            if len(str(item[coluna])) > maior:
                maior = len(str(item[coluna]))
        larguras.append(maior)

    return larguras

# Responsável por criar as linhas da tabela de opções
def criar_linha_tabela_opcoes(larguras, colunas):
    linha = "="

    for coluna in range(colunas):
        linha += f"{"=" * (larguras[coluna] + 2)}="

    return linha

#Responsável por inserir os dados da tabela de opcoes
def inserir_dados_tabela_opcoes(menu, colunas, larguras):

    for produto in menu:
        dados = "["

        for coluna in range(colunas):
            if coluna == 0:
                dados += f" {str(produto[coluna]):<{larguras[coluna]}} ]"
            else:
                dados += f"[ {str(produto[coluna]):<{larguras[coluna]}} ]"

        print(dados)

#Responsável por criar colunas da tabela
def criar_coluna_tabela(cursor, tabela):
    query = """
            SELECT count(column_name) AS numero_de_colunas
            FROM information_schema.columns
            WHERE table_name = %s;
            """
    
    cursor.execute(query, (tabela,))
    colunas = cursor.fetchone()
    colunas = colunas[0] - 1
    return colunas

# Responsável por criar uma tabela para as opções do menu
def criar_tabela_opcoes(menu):
    colunas = 2
    titulos = selecionar_titulos_tabela("opcoes")
    larguras = calcular_largura_tabela_opcoes(menu, colunas)

    print(titulos[0])
    inserir_dados_tabela_opcoes(menu, 2, larguras)

#Responsável por criar a tabela
def criar_tabela(cursor, menu, tabela):

    colunas = criar_coluna_tabela(cursor, tabela)
    titulos = selecionar_titulos_tabela(tabela)
    larguras = calcular_largura_tabela(menu, colunas, titulos)
    linha = criar_linha_tabela(larguras, colunas)

    print(linha)
    inserir_titulos_tabela(titulos, colunas, larguras)
    print(linha)
    inserir_dados_tabela(menu, colunas, larguras)
    print(linha)