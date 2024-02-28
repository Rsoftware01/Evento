from flask import Flask, request
import pyodbc

app = Flask(__name__)

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Rafael;"
    "Database=Evento_Mulheres;"
    "Trusted_Connection=yes;"
)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    nome = request.form['starting-name']
    telefone = request.form['telefone']
    email = request.form['email']

    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()

    comando = f"""INSERT INTO Dados (nome, telefone, email) VALUES ('{nome}', '{telefone}', '{email}')"""
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

    return 'Dados inseridos com sucesso', 200

if __name__ == '__main__':
    app.run(debug=True)
