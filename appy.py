from flask import Flask, request, jsonify
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

# Conexão com o banco
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Rota para cadastrar aluno (POST)
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    matricula = data.get('matricula')
    senha = data.get('senha')

    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO aluno (nome, email, matricula, senha) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, email, matricula, senha))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensagem': 'Aluno cadastrado com sucesso'}), 201

# Rota para listar alunos (GET)
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(alunos), 200

if __name__ == '__main__':
    app.run(debug=True)
