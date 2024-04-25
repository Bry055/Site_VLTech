from flask import Flask, render_template, request

import mysql.connector

app = Flask(__name__, template_folder='C:/Users/bryan/OneDrive/Área de Trabalho/Vltech_site/template', static_folder='C:/Users/bryan/OneDrive/Área de Trabalho/Vltech_site/static')


@app.route('/')
def index():
    return render_template('Front_site.html')

@app.route('/inserir_dado', methods=['POST'])
def inserir_dado():
    opcao = request.form['opcao']

    # Conectar ao banco de dados MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vltech123",
        database="vltech"
    )
    cursor = db.cursor()

    # Executar a inserção no banco de dados
    #idtype do tipo 1 é para reparo em computadores e do tipo 2 é para reparo em celulares
    if opcao == '1':
        cursor.execute("INSERT INTO servico (idtype, tipoServico) VALUES (1,1)")
    elif opcao == '2':
        cursor.execute("INSERT INTO servico(idtype, tipoServico) VALUES (1,2)")
    else:
        return 'Opção inválida.'

    # Fechar a conexão com o banco de dados
    cursor.close()
    db.close()

    return 'Dado inserido com sucesso.'


if __name__ == '__main__':
    app.run(debug=True)
