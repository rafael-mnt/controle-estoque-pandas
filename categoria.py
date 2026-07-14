from database import conectar
from menu import criar_menu_tabela, criar_menu_opcoes, criar_menu_id_unico
from table import criar_tabela, criar_tabela_opcoes
from functions import validar_duplicidade, extrair_id
from crud import cadastrar_categoria, alterar_dados, excluir_dado

conexao = conectar()
cursor = conexao.cursor()

def opcao_categorias():

    while True:
                
        tabela = "categoria"
        categorias = criar_menu_tabela(cursor, tabela)
        menu_categorias = criar_menu_opcoes('menu_categorias')
        print("\n==== MENU DE CATEGORIAS ====")
        criar_tabela(categorias, tabela)
        criar_tabela_opcoes(menu_categorias)
        opcao_categoria = input("Escolha: ")

        # MENU CADASTRAR CATEGORIA
        if opcao_categoria == "1":
            print("\n---- CADASTRAR CATEGORIA ----")
            nome = validar_duplicidade("Nome da Categoria", cursor, tabela, "nome").upper()
            cadastrar_categoria(conexao, cursor, nome)
            print("# - Categoria Cadastrada!\n")

        # MENU ALTERAR CATEGORIA
        elif opcao_categoria == "2":
            print("\n---- ALTERAR CATEGORIA ----")
            print("Insira o nome da categoria:")
            id = extrair_id("Nome da categoria", cursor, tabela)

            while True:
                print("\n== INFORMAÇÕES DA CATEGORIA ==")
                menu_item = criar_menu_id_unico(cursor, tabela, id)
                criar_tabela(menu_item, tabela)
                opcoes = criar_menu_opcoes("opcoes_alterar_categoria")
                criar_tabela_opcoes(opcoes)
                opcao = input("Escolha: ")

                # Alterar nome categoria
                if opcao == "1":
                    print("Informe o novo nome da categoria!")
                    nome_novo = validar_duplicidade("Nome da Categoria", cursor, tabela, "nome").upper()
                    alterar_dados(conexao, cursor, tabela, "nome", id, nome_novo)

                elif opcao == "0":
                    opcao_categoria = 0
                    break
        
        # MENU EXCLUIR CATEGORIA
        elif opcao_categoria == "3":
            print("\n---- EXCLUIR CATEGORIA ----")
            print("Insira o nome da categoria:")
            id = extrair_id("Nome da categoria", cursor, tabela)
            menu_item = criar_menu_id_unico(cursor, tabela, id)
            print("\n== INFORMAÇÕES DA CATEGORIA ==")
            criar_tabela(menu_item, tabela)
            excluir_dado(conexao, cursor, tabela, id)

        elif opcao_categoria == "0":
            return conexao.close()

        else:
            print("Opção Inválida!")