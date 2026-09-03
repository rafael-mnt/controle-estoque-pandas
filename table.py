import datetime


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

def criar_linha_tabela(larguras, colunas):
    linha = "+"

    for coluna in range(colunas):
        linha += f"{"-" * (larguras[coluna] + 2)}+"

    return linha

def inserir_titulos_tabela(titulos, colunas, larguras):
    dados = "|"

    for titulo in range(colunas):
        dados += f" {str(titulos[titulo]):<{larguras[titulo]}} |"

    print(dados)

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

def calcular_largura_tabela_opcoes(menu, colunas):
    larguras = []

    for coluna in range(colunas):
        maior = 0
        for item in menu:
            if len(str(item[coluna])) > maior:
                maior = len(str(item[coluna]))
        larguras.append(maior)

    return larguras

def criar_linha_tabela_opcoes(larguras, colunas):
    linha = "="

    for coluna in range(colunas):
        linha += f"{"=" * (larguras[coluna] + 2)}="

    return linha

def inserir_dados_tabela_opcoes(menu, colunas, larguras):

    for produto in menu:
        dados = "["

        for coluna in range(colunas):
            if coluna == 0:
                dados += f" {str(produto[coluna]):<{larguras[coluna]}} ]"
            else:
                dados += f"[ {str(produto[coluna]):<{larguras[coluna]}} ]"

        print(dados)

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

def criar_tabela_opcoes(menu):
    colunas = 2
    titulos = selecionar_titulos_tabela("opcoes")
    larguras = calcular_largura_tabela_opcoes(menu, colunas)

    print(titulos[0])
    inserir_dados_tabela_opcoes(menu, 2, larguras)

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