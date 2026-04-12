import random
import string

class Produto:
    def __init__(self, id, nome, valor, quant):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.quant = quant

class Estoque:
    def __init__(self):
        self.produtos = {}


    # Gerar um ID aleatório com 3 letras maiúsculas e 4 dígitos, garantindo que seja único no sistema
    def gerar_id():

        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        numeros = ''.join(random.choices(string.digits, k=4))
        return letras + numeros


    # Gerar um ID único, verificando se o ID gerado já existe no sistema, e caso exista, gerar outro ID até encontrar um ID único
    def gerar_id_unico(self):

        while True:

            novo_id = self.gerar_id()
            if novo_id not in self.produtos:
                return novo_id
            

    # Função que recebe os dados do produto, gera um ID único e cadastra o produto no sistema, retornando o ID do produto cadastrado
    def cadastrar_produto(self, nome, preco, quant):

        novo_id = self.gerar_id_unico()
        produto = Produto(novo_id, nome, preco, quant)
        self.produtos[novo_id] = produto
        return novo_id
    

    # Função que verifica pelo ID fornecido pelo usuário se o produto está cadastrado e deleta ele do sistema caso esteja
    def excluir_produto(self, id_produto):
        if id_produto not in self.produtos:
            return False
        del self.produtos[id_produto]
        return True


    def entrada_estoque(self, id_produto, quantidade):
        if id_produto not in self.produtos or quantidade <= 0:
            return False

        self.produtos[id_produto].quantidade += quantidade
        return True
    

    def saida_estoque(self, id_produto, quantidade):
        if id_produto not in self.produtos or quantidade <= 0:
            return False

        if self.produtos[id_produto].quantidade < quantidade:
            return False

        self.produtos[id_produto].quantidade -= quantidade
        return True


    def listar_produtos(self):
        return self.produtos
    
