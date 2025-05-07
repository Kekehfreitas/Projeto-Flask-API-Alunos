CREATE DATABASE escola;

USE escola;

CREATE TABLE aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    matricula VARCHAR(50),
    senha VARCHAR(100)
);
