import datetime

# Responsável por selecionar os títulos da tabela
def selecionar_titulos_tabela(tabela):
    if tabela == "categoria":
        return ["CATEGORIA"]
    if tabela == "produto":
        return ["PRODUTO", "CATEGORIA", "FORNECEDOR", "PREÇO", "ESTOQUE MÍNIMO", "ESTOQUE ATUAL", "DATA DE CADASTRO"]
    if tabela == "fornecedor":
        return ["FORNECEDOR", "CPF/CNPJ", "TELEFONE", "E-MAIL"]
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

    for produto in menu:
        dados = "|"

        for coluna in range(colunas):
            if type(produto[coluna]) is datetime.date:
                data = produto[coluna].strftime("%d/%m/%Y")
                dados += f" {data:<{larguras[coluna]}} |"
            else:
                dados += f" {str(produto[coluna]):<{larguras[coluna]}} |"

        print(dados)

#Responsável por criar a tabela
def criar_tabela(cursor, menu, tabela):

    colunas = len(menu[0])
    titulos = selecionar_titulos_tabela(tabela)
    larguras = calcular_largura_tabela(menu, colunas, titulos)
    linha = criar_linha_tabela(larguras, colunas)

    print(linha)
    inserir_titulos_tabela(titulos, colunas, larguras)
    print(linha)
    inserir_dados_tabela(menu, colunas, larguras)
    print(linha)

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

# Responsável por criar uma tabela para as opções do menu
def criar_tabela_opcoes(menu):
    colunas = 2
    titulos = selecionar_titulos_tabela("opcoes")
    larguras = calcular_largura_tabela_opcoes(menu, colunas)

    print(titulos[0])
    inserir_dados_tabela_opcoes(menu, 2, larguras)