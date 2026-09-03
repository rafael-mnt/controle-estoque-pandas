from categoria import opcao_categorias
from database import obter_conexao_valida
from estoque import opcao_estoque
from fornecedor import opcao_fornecedores
from menu import criar_menu_opcoes
from produto import opcao_produtos
from table import criar_tabela_opcoes

conexao = None

while True:

    conexao, cursor = obter_conexao_valida(conexao)
    
    print("\n==== SISTEMA DE ESTOQUE ====")
    menu_principal = criar_menu_opcoes("menu_principal")
    criar_tabela_opcoes(menu_principal)
    opcao_principal = input("Escolha: ")

    if opcao_principal == "1":
        opcao_categorias(conexao, cursor)

    elif opcao_principal == "2":
        opcao_produtos(conexao, cursor)

    elif opcao_principal == "3":
        opcao_fornecedores(conexao, cursor)

    elif opcao_principal == "4":
        opcao_estoque(conexao, cursor)
        
    elif opcao_principal == "0":
        print("Sistema Encerrado!")
        conexao.close()
        break

    else:
        print("Opção Inválida!")
