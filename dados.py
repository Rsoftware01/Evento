from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Rafael;"
    "Database=Evento_Mulheres;"
    "Trusted_Connection=yes;"
)

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Parse dos dados do formulário
        data = parse_qs(post_data.decode('utf-8'))
        nome = data['nome'][0]
        telefone = data['telefone'][0]
        email = data['email'][0]

        # Exibindo os dados recebidos
        print("Dados recebidos do formulário:")
        print("Nome:", nome)
        print("Telefone:", telefone)
        print("Email:", email)

        # Conexão ao banco de dados e inserção de dados
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        comando = f"""INSERT INTO Dados (nome, telefone, email) VALUES (?, ?, ?)"""
        cursor.execute(comando, (nome, int(telefone), email))
        conexao.commit()
        conexao.close()

        # Envio da resposta de volta ao cliente
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Dados inseridos com sucesso".encode())

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
