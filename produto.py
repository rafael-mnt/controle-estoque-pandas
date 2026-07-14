from database import conectar
from menu import criar_menu_tabela, criar_menu_opcoes, criar_menu_id_unico, criar_menu_consulta
from table import criar_tabela, criar_tabela_opcoes
from functions import validar_duplicidade, extrair_id, validar_atributo
from crud import cadastrar_produto, alterar_dados, excluir_dado

conexao = conectar()
cursor = conexao.cursor()

def opcao_produtos():

    while True:

        tabela = "produto"

        print("\n==== MENU DE PRODUTOS ====")

        produtos = criar_menu_tabela(cursor, tabela)
        criar_tabela(produtos, tabela)

        menu_produtos = criar_menu_opcoes("menu_produtos")
        criar_tabela_opcoes(menu_produtos)
        opcao_produto = input("Escolha: ")

        # MENU CADASTRAR PRODUTO
        if opcao_produto == "1":

            print("\n---- ALTERAR PRODUTO ----")
            nome = validar_duplicidade("Nome do Produto", cursor, tabela, 'nome').upper()
            categoria_id = extrair_id("Nome da Categoria", cursor, 'categoria')
            fornecedor_id = extrair_id("Nome do Fornecedor", cursor, 'fornecedor')
            preco = validar_atributo("Preço do Produto: ", float)
            estoque_atual = validar_atributo("Estoque Atual: ", int)
            estoque_minimo = validar_atributo("Estoque Mínimo: ", int)

            cadastrar_produto(conexao, cursor, nome, categoria_id, fornecedor_id, preco, estoque_atual, estoque_minimo)
            print("Produto Cadastrado!\n")

        # MENU ALTERAR PRODUTO
        elif opcao_produto == "2":

            print("\n---- ALTERAR PRODUTO ----")
            print("Insira o nome do produto:")
            id = extrair_id("Nome do produto", cursor, tabela)
            
            while True:

                print("\n== INFORMAÇÕES DO PRODUTO ==")

                menu_item = criar_menu_id_unico(cursor, tabela, id)
                criar_tabela(menu_item, tabela)

                opcoes = criar_menu_opcoes("opcoes_alterar_produto")
                criar_tabela_opcoes(opcoes)
                opcao = input("Escolha: ")

                # Alterar nome produto
                if opcao == "1":

                    print("Informe o novo nome do produto!")
                    nome_novo = validar_duplicidade("Nome do Produto", cursor, tabela, "nome").upper()

                    alterar_dados(conexao, cursor, tabela, "nome", id, nome_novo)

                # Alterar categoria
                elif opcao == "2":
                    
                    print('-- CATEGORIAS CADASTRADAS --')
                    categoria_consulta = criar_menu_consulta(cursor, 'categoria')
                    criar_tabela(categoria_consulta, 'categoria')

                    print("Informe a nova categoria!")
                    id_categoria_nova = extrair_id("Nome da Categoria", cursor, "categoria")

                    alterar_dados(conexao, cursor, tabela, "categoria_id", id, id_categoria_nova)
                    
                # Alterar fornecedor
                elif opcao == "3":

                    print('-- FORNECEDORES CADASTRADOS --')
                    fornecedor_consulta = criar_menu_consulta(cursor, 'fornecedor')
                    criar_tabela(fornecedor_consulta, 'fornecedor')

                    print("Informe o novo fornecedor!")
                    id_fornecedor_novo = extrair_id("Nome do Fornecedor", cursor, "fornecedor")

                    alterar_dados(conexao, cursor, tabela, "fornecedor_id", id, id_fornecedor_novo)

                # Alterar preço
                elif opcao == "4":

                    print("Informe o novo preço do produto!")
                    preco_novo = validar_atributo("Preço do Produto: ", float)

                    alterar_dados(conexao, cursor, tabela, "preco", id, preco_novo)

                # Alterar estoque mínimo
                elif opcao == "5":

                    print("Informe o novo estoque mínimo do produto!")
                    estoque_novo = validar_atributo("Estoque mínimo do Produto: ", int)

                    alterar_dados(conexao, cursor, tabela, "estoque_minimo", id, estoque_novo)

                elif opcao == "0":
                    opcao_produto = 0
                    break
        
        # MENU EXCLUIR PRODUTO
        elif opcao_produto == "3":

            print("\n---- EXCLUIR PRODUTO ----")
            print("Insira o nome do produto:")
            id = extrair_id("Nome do produto", cursor, tabela)

            print("\n== INFORMAÇÕES DO PRODUTO ==")
            menu_item = criar_menu_id_unico(cursor, tabela, id)
            criar_tabela(menu_item, tabela)

            excluir_dado(conexao, cursor, tabela, id)

        elif opcao_produto == "0":
            return conexao.close()

        else:
            print("Opção Inválida!")