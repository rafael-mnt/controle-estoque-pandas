from database import conectar
from menu import criar_menu_tabela, criar_menu_opcoes
from table import criar_tabela, criar_tabela_opcoes
from functions import extrair_id, validar_quantidade, validar_nulo
from inventory import registrar_movimento

conexao = conectar()
cursor = conexao.cursor()

def opcao_estoque():

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