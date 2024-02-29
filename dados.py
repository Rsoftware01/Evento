from flask import Flask, request

app = Flask(__name__)

@app.route('/dados', methods=['POST'])
def handle_data():
    # Parse dos dados do formulário
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']

    # Adicionando instruções print para depuração
    print("Dados do formulário recebidos:")
    print("Nome:", nome)
    print("Telefone:", telefone)
    print("Email:", email)

    # Conexão ao banco de dados e inserção de dados
    dados_conexao = "Driver={SQL Server};Server=Rafael;Database=Evento_Mulheres;Trusted_Connection=yes;"
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    comando = "INSERT INTO Dados (nome, telefone, email) VALUES (?, ?, ?)"
    cursor.execute(comando, (nome, telefone, email))
    conexao.commit()
    conexao.close()

    return "Dados inseridos com sucesso"

if __name__ == '__main__':
    app.run(debug=True)
