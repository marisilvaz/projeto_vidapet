import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("localhost"),
        user=os.getenv("root"),
        password=os.getenv("2510"),
        database=os.getenv("vidapet")
    )

    return conexao