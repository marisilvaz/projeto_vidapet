import mysql.connector
import os
from dotenv import load_dotenv


def conectar():
    conexao = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="2510",
        database="vidapet"
    )
    return conexao
