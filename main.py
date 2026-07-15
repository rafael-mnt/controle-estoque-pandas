from database import conectar
from categoria import opcao_categorias
from produto import opcao_produtos
from fornecedor import opcao_fornecedores
from menu import criar_menu_opcoes
from table import criar_tabela_opcoes

conexao = conectar()
cursor = conexao.cursor()

while True:
    
    print("\n==== SISTEMA DE ESTOQUE ====")
    menu_principal = criar_menu_opcoes("menu_principal")
    criar_tabela_opcoes(menu_principal)
    opcao_principal = input("Escolha: ")

    # MENU CATEGORIA
    if opcao_principal == "1":
        opcao_categorias()

    # MENU PRODUTO
    elif opcao_principal == "2":
        opcao_produtos()

    # MENU FORNECEDOR
    elif opcao_principal == "3":
        opcao_fornecedores()
        
    # SAIR DO SISTEMA
    elif opcao_principal == "0":
        print("Sistema Encerrado!")
        conexao.close()
        break

    else:
        print("Opção Inválida!")
