import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-2SNVIBI;"
    "Database=Py_SQL"
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()