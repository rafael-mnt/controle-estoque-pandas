from database import conectar
from menu import criar_menu_tabela, criar_menu_opcoes, criar_menu_id_unico
from table import criar_tabela, criar_tabela_opcoes
from functions import validar_duplicidade, extrair_id, validar_exclusao
from crud import cadastrar_fornecedor, alterar_dados, excluir_dado

conexao = conectar()
cursor = conexao.cursor()

def opcao_fornecedores():
    
    while True:

        tabela = "fornecedor"
        fornecedores = criar_menu_tabela(cursor, tabela)
        print("\n==== MENU DE FORNECEDORES ====")
        criar_tabela(fornecedores, tabela)
        menu_fornecedores = criar_menu_opcoes("menu_fornecedores")
        criar_tabela_opcoes(menu_fornecedores)
        opcao_fornecedor = input("Escolha: ")

        # MENU CADASTRAR FORNECEDOR
        if opcao_fornecedor == "1":
            print("\n---- CADASTRAR FORNECEDOR ----")
            nome = validar_duplicidade("Nome do Fornecedor", cursor, tabela, "nome").upper()
            cpf_cnpj = validar_duplicidade("CPF/CNPJ", cursor, tabela, "cpf_cnpj")
            telefone = input("Telefone: ")
            email = input("E-mail: ").upper()
            cadastrar_fornecedor(conexao, cursor, nome, cpf_cnpj, telefone, email)
            print("Fornecedor Cadastrado!\n")

        # MENU ALTERAR FORNECEDOR
        elif opcao_fornecedor == "2":
            print("\n---- ALTERAR FORNECEDOR ----")
            print("Insira o nome do fornecedor:")
            id = extrair_id("Nome do fornecedor", cursor, tabela)
            
            while True:
                menu_item = criar_menu_id_unico(cursor, tabela, id)
                print("\n== INFORMAÇÕES DO FORNECEDOR ==")
                criar_tabela(menu_item, tabela)
                opcoes = criar_menu_opcoes("opcoes_alterar_fornecedor")
                criar_tabela_opcoes(opcoes)
                opcao = input("Escolha: ")

                # Alterar nome fornecedor
                if opcao == "1":
                    print("Informe o novo nome do fornecedor")
                    nome_novo = validar_duplicidade("Nome do Fornecedor", cursor, tabela, "nome").upper()
                    alterar_dados(conexao, cursor, tabela, "nome", id, nome_novo)

                # Alterar CPF / CNPJ fornecedor
                elif opcao == "2":
                    print("Informe o novo CPF/CNPJ do fornecedor")
                    cpf_cnpj_novo = validar_duplicidade("CPF/CNPJ do Fornecedor", cursor, tabela, "cpf_cnpj")
                    alterar_dados(conexao, cursor, tabela, "cpf_cnpj", id, cpf_cnpj_novo)

                # Alterar telefone fornecedor
                elif opcao == "3":
                    print("Informe o novo telefone do fornecedor")
                    telefone_novo = validar_duplicidade("Telefone do Fornecedor", cursor, tabela, "telefone")
                    alterar_dados(conexao, cursor, tabela, "telefone", id,telefone_novo)

                # Alterar e-mail fornecedor
                elif opcao == "4":
                    print("Informe o novo E-mail do fornecedor")
                    email_novo = validar_duplicidade("E-mail do Fornecedor", cursor, tabela, "email").upper()
                    alterar_dados(conexao, cursor, tabela, "email", id, email_novo)

                elif opcao == "0":
                    opcao_fornecedor = 0
                    break

                else:
                    print("Opção Inválida!")
        
        # MENU EXCLUIR FORNECEDOR
        elif opcao_fornecedor == "3":
            print("\n---- EXCLUIR FORNECEDOR ----")
            print("Insira o nome do fornecedor:")
            id = extrair_id("Nome do fornecedor", cursor, tabela)
            menu_item = criar_menu_id_unico(cursor, tabela, id)
            print("\n== INFORMAÇÕES DO FORNECEDOR ==")
            criar_tabela(menu_item, tabela)

            if validar_exclusao(cursor, "fornecedor_id", id):
                excluir_dado(conexao, cursor, tabela, id)
            else:
                print("# Aviso: Forcenedor cadastrado na tabela produto!\nAltere o fornecedor no produto cadastrado para excluí-lo.")

        elif opcao_fornecedor == "0":
            return

        else:
            print("Opção Inválida!")