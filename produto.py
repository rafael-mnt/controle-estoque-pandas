from crud import alterar_dados, cadastrar_produto, excluir_dado
from functions import extrair_id, validar_atributo, validar_duplicidade, validar_nulo
from menu import (
    criar_menu_consulta,
    criar_menu_id_unico,
    criar_menu_opcoes,
    criar_menu_tabela,
)
from table import criar_tabela, criar_tabela_opcoes


def opcao_produtos(conexao, cursor):

    while True:

        tabela = "produto"

        print("\n==== MENU DE PRODUTOS ====")

        produtos = criar_menu_tabela(cursor, tabela)
        criar_tabela(cursor, produtos, tabela)

        menu_produtos = criar_menu_opcoes("menu_produtos")
        criar_tabela_opcoes(menu_produtos)
        opcao_produto = input("Escolha: ")

        if opcao_produto == "1":

            if validar_nulo(cursor, 'categoria') and validar_nulo(cursor, 'fornecedor'):
                print("# Aviso: Não é possível cadastrar produto sem dados nas tabelas Categoria e Fornecedor!\nCadastre uma categoria e um fornecedor para realizar essa ação.")
            elif validar_nulo(cursor, 'categoria'):
                print("# Aviso: Não é possível cadastrar produto sem dados na tabela Categoria!\nCadastre uma categoria para realizar essa ação.")
            elif validar_nulo(cursor, 'fornecedor'):
                print("# Aviso: Não é possível cadastrar produto sem dados na tabela Fornecedor!\nCadastre um fornecedor para realizar essa ação.")
            else:
                print("\n---- CADASTRAR PRODUTO ----")
                nome = validar_duplicidade("Nome do Produto", cursor, tabela, 'nome').upper()
                categoria_id = extrair_id("Nome da Categoria", cursor, 'categoria')
                fornecedor_id = extrair_id("Nome do Fornecedor", cursor, 'fornecedor')
                preco = validar_atributo("Preço do Produto: ", float)
                estoque_minimo = validar_atributo("Estoque Mínimo: ", int)

                cadastrar_produto(conexao, cursor, nome, categoria_id, fornecedor_id, preco, estoque_minimo)

        elif opcao_produto == "2":

            if validar_nulo(cursor, tabela):
                print("# Aviso: Não é possível alterar tabela sem dados!\nCadastre um produto para realizar essa ação.")
            else:
                print("\n---- ALTERAR PRODUTO ----")
                print("Insira o nome do produto:")
                id = extrair_id("Nome do produto", cursor, tabela)
                
                while True:

                    print("\n== INFORMAÇÕES DO PRODUTO ==")

                    menu_item = criar_menu_id_unico(cursor, tabela, id)
                    criar_tabela(cursor, menu_item, tabela)

                    opcoes = criar_menu_opcoes("opcoes_alterar_produto")
                    criar_tabela_opcoes(opcoes)
                    opcao = input("Escolha: ")

                    if opcao == "1":

                        print("Informe o novo nome do produto!")
                        nome_novo = validar_duplicidade("Nome do Produto", cursor, tabela, "nome").upper()

                        alterar_dados(conexao, cursor, tabela, "nome", id, nome_novo)

                    elif opcao == "2":
                        
                        print('-- CATEGORIAS CADASTRADAS --')
                        categoria_consulta = criar_menu_consulta(cursor, 'categoria')
                        criar_tabela(cursor, categoria_consulta, 'categoria')

                        print("Informe a nova categoria!")
                        id_categoria_nova = extrair_id("Nome da Categoria", cursor, "categoria")

                        alterar_dados(conexao, cursor, tabela, "categoria_id", id, id_categoria_nova)
                        
                    elif opcao == "3":

                        print('-- FORNECEDORES CADASTRADOS --')
                        fornecedor_consulta = criar_menu_consulta(cursor, 'fornecedor')
                        criar_tabela(cursor, fornecedor_consulta, 'fornecedor')

                        print("Informe o novo fornecedor!")
                        id_fornecedor_novo = extrair_id("Nome do Fornecedor", cursor, "fornecedor")

                        alterar_dados(conexao, cursor, tabela, "fornecedor_id", id, id_fornecedor_novo)
 
                    elif opcao == "4":

                        print("Informe o novo preço do produto!")
                        preco_novo = validar_atributo("Preço do Produto: ", float)

                        alterar_dados(conexao, cursor, tabela, "preco", id, preco_novo)

                    elif opcao == "5":

                        print("Informe o novo estoque mínimo do produto!")
                        estoque_novo = validar_atributo("Estoque mínimo do Produto: ", int)

                        alterar_dados(conexao, cursor, tabela, "estoque_minimo", id, estoque_novo)

                    elif opcao == "0":
                        opcao_produto = "0"
                        break

                    else:
                        print("Opção Inválida!")
        
        elif opcao_produto == "3":

            if validar_nulo(cursor, tabela):
                print("# Aviso: Não é possível excluir tabela sem dados!\nCadastre um produto para realizar essa ação.")
            else:
                print("\n---- EXCLUIR PRODUTO ----")
                print("Insira o nome do produto:")
                id = extrair_id("Nome do produto", cursor, tabela)

                print("\n== INFORMAÇÕES DO PRODUTO ==")
                menu_item = criar_menu_id_unico(cursor, tabela, id)
                criar_tabela(cursor, menu_item, tabela)

                excluir_dado(conexao, cursor, tabela, id)

        elif opcao_produto == "0":
            return

        else:
            print("Opção Inválida!")