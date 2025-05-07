# Projeto Flask API - Alunos

API REST criada com Python (Flask) e MySQL para cadastrar e listar alunos.

---

# Requisitos

- Python 3.10+
- MySQL Server
- Postman ou Insomnia (para testes)
- Bibliotecas do `requirements.txt`

---

# Estrutura do Projeto


---

# Como usar

# 1 Crie o banco de dados

Abra seu MySQL e execute o script SQL em `db/aluno.sql`:

```sql
CREATE DATABASE escola;

USE escola;

CREATE TABLE aluno (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  matricula VARCHAR(50),
  senha VARCHAR(100)
);


