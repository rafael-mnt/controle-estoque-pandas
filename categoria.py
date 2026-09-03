from crud import alterar_dados, cadastrar_categoria, excluir_dado
from functions import extrair_id, validar_duplicidade, validar_exclusao, validar_nulo
from menu import criar_menu_id_unico, criar_menu_opcoes, criar_menu_tabela
from table import criar_tabela, criar_tabela_opcoes


def opcao_categorias(conexao, cursor):

    while True:
                
        tabela = "categoria"
        print(validar_nulo(cursor, tabela ))
        categorias = criar_menu_tabela(cursor, tabela)
        menu_categorias = criar_menu_opcoes('menu_categorias')
        print("\n==== MENU DE CATEGORIAS ====")
        criar_tabela(cursor, categorias, tabela)
        criar_tabela_opcoes(menu_categorias)
        opcao_categoria = input("Escolha: ")

        if opcao_categoria == "1":
            print("\n---- CADASTRAR CATEGORIA ----")
            nome = validar_duplicidade("Nome da Categoria", cursor, tabela, "nome").upper()
            cadastrar_categoria(conexao, cursor, nome)

        elif opcao_categoria == "2":

            if validar_nulo(cursor, tabela):
                print("# Aviso: Não é possível alterar tabela sem dados!\nCadastre uma categoria para realizar essa ação.")
            else:
                print("\n---- ALTERAR CATEGORIA ----")
                print("Insira o nome da categoria:")
                id = extrair_id("Nome da categoria", cursor, tabela)

                while True:
                    print("\n== INFORMAÇÕES DA CATEGORIA ==")
                    menu_item = criar_menu_id_unico(cursor, tabela, id)
                    criar_tabela(cursor, menu_item, tabela)
                    opcoes = criar_menu_opcoes("opcoes_alterar_categoria")
                    criar_tabela_opcoes(opcoes)
                    opcao = input("Escolha: ")

                    if opcao == "1":
                        print("Informe o novo nome da categoria!")
                        nome_novo = validar_duplicidade("Nome da Categoria", cursor, tabela, "nome").upper()
                        alterar_dados(conexao, cursor, tabela, "nome", id, nome_novo)

                    elif opcao == "0":
                        opcao_categoria = "0"
                        break

                    else:
                        print("Opção Inválida!")

        
        elif opcao_categoria == "3":

            if validar_nulo(cursor, tabela):
                print("# Aviso: Não é possível excluir tabela sem dados!\nCadastre uma categoria para realizar essa ação.")
            else:
                print("\n---- EXCLUIR CATEGORIA ----")
                print("Insira o nome da categoria:")
                id = extrair_id("Nome da categoria", cursor, tabela)
                menu_item = criar_menu_id_unico(cursor, tabela, id)
                print("\n== INFORMAÇÕES DA CATEGORIA ==")
                criar_tabela(cursor, menu_item, tabela)

                if validar_exclusao(cursor, "categoria_id", id):
                    excluir_dado(conexao, cursor, tabela, id)
                else:
                    print("# Aviso: Categoria cadastrada na tabela produto!\nAltere a categoria no produto cadastrado para excluí-la.")

        elif opcao_categoria == "0":
            return

        else:
            print("Opção Inválida!")