from functions import Estoque

def pedir_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Entrada inválida")


def pedir_float(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Entrada inválida")


estoque = Estoque()

# dados iniciais
estoque.cadastrar_produto("Notebook Asus", 3500.0, 32)
estoque.cadastrar_produto("Notebook Positivo", 1500.0, 55)
estoque.cadastrar_produto("Celular Xiaomi", 1950.0, 26)
estoque.cadastrar_produto("Carregador Samsung", 35.0, 14)


while True:
    print("\n== SISTEMA DE ESTOQUE ==")
    print("1 - Cadastrar Produto")
    print("2 - Excluir Produto")
    print("3 - Entrada de Estoque")
    print("4 - Saída de Estoque")
    print("5 - Visualizar Estoque")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        preco = pedir_float("Preço: ")
        quantidade = pedir_int("Quantidade: ")

        id_produto = estoque.cadastrar_produto(nome, preco, quantidade)
        print(f"Produto cadastrado com ID: {id_produto}")

    elif opcao == "2":
        id_produto = input("ID: ")
        if estoque.excluir_produto(id_produto):
            print("Produto excluído")
        else:
            print("Produto não encontrado")

    elif opcao == "3":
        id_produto = input("ID: ")
        quantidade = pedir_int("Quantidade de entrada: ")

        if estoque.entrada_estoque(id_produto, quantidade):
            print("Entrada realizada")
        else:
            print("Erro na operação")

    elif opcao == "4":
        id_produto = input("ID: ")
        quantidade = pedir_int("Quantidade de saída: ")

        if estoque.saida_estoque(id_produto, quantidade):
            print("Saída realizada")
        else:
            print("Erro na operação")

    elif opcao == "5":
        for p in estoque.listar_produtos().values():
            print(f"{p.id} | {p.nome} | R${p.preco:.2f} | Qtd: {p.quantidade}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida")

print("Sistema encerrado")
