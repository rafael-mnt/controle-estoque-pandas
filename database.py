import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def obter_conexao_valida(conexao):
    if conexao is None or conexao.closed:
        nova_conexao = conectar()
        return nova_conexao, nova_conexao.cursor()

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT 1")
        return conexao, cursor
    except (psycopg.OperationalError, psycopg.InterfaceError):
        nova_conexao = conectar()
        return nova_conexao, nova_conexao.cursor()