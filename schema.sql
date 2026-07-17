CREATE TABLE categoria (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE fornecedor (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) UNIQUE NOT NULL,
	cpf_cnpj VARCHAR(18) UNIQUE NOT NULL,
	telefone VARCHAR(20),
	email VARCHAR(100)
);

CREATE TABLE produto (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	categoria_id INTEGER NOT NULL,
	fornecedor_id INTEGER NOT NULL,
	preco NUMERIC(10,2) NOT NULL,
	estoque_minimo INTEGER NOT NULL DEFAULT 0 CHECK (estoque_minimo >= 0),
	estoque_atual INTEGER NOT NULL DEFAULT 0 CHECK (estoque_atual >= 0),
	data_de_cadastro DATE DEFAULT CURRENT_DATE,

	FOREIGN KEY (categoria_id) REFERENCES categoria(id),
	FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
);

CREATE TABLE movimentacao (
	id SERIAL PRIMARY KEY,
	produto_id INTEGER NOT NULL,
	tipo VARCHAR(10) NOT NULL CHECK (tipo in ('Entrada', 'Saída')),
	quantidade INTEGER NOT NULL,
	data_movimentacao DATE DEFAULT CURRENT_DATE,
	observacao TEXT,

	FOREIGN KEY (produto_id) REFERENCES produto(id)
);