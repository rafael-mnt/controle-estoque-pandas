from functions import extrair_id, validar_nulo, validar_quantidade
from inventory import registrar_movimento
from menu import criar_menu_opcoes, criar_menu_tabela
from table import criar_tabela, criar_tabela_opcoes


def opcao_estoque(conexao, cursor):

    while True:
                
        tabela = "estoque"
        estoque = criar_menu_tabela(cursor, tabela)
        menu_estoque = criar_menu_opcoes('menu_estoque')
        print("\n==== MENU DE CATEGORIAS ====")
        criar_tabela(cursor, estoque, tabela)
        criar_tabela_opcoes(menu_estoque)
        opcao_estoque = input("Escolha: ")

        if opcao_estoque == "1":

            if validar_nulo(cursor, 'produto'):
                print("# Aviso: Não é possível registrar entrada sem produtos cadastrados!\nCadastre um produto para realizar um registro.")
            else:
                produto_id = extrair_id("Nome do Produto", cursor, "produto")
                tipo = "Entrada"
                quantidade = validar_quantidade(cursor, tipo, produto_id)
                observacao = input("Observação: ")

                registrar_movimento(conexao, cursor, produto_id, tipo, quantidade, observacao)

        elif opcao_estoque == "2":

            if validar_nulo(cursor, 'produto'):
                print("# Aviso: Não é possível registrar saída sem produtos cadastrados!\nCadastre um produto para realizar um registro.")
            else:
                produto_id = extrair_id("Nome do Produto", cursor, "produto")
                tipo = "Saída"
                quantidade = validar_quantidade(cursor, tipo, produto_id)
                observacao = input("Observação: ")

                registrar_movimento(conexao, cursor, produto_id, tipo, quantidade, observacao)

        elif opcao_estoque == "0":
            return

        else:
            print("Opção Inválida")