from flask import Flask, json, render_template, redirect, request, flash, send_from_directory, url_for
import json
import ast
import os
from pathlib import Path
import mysql.connector


app = Flask(__name__)
app.config['SECRET_KEY'] = 'JOAOHCA'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    global logado
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    conect_BD = mysql.connector.connect(host='localhost', database='usuarios', user='root', password='projetoapp01@')
    cont = 0
    if conect_BD.is_connected():
        print('conectado')
        cursor = conect_BD.cursor()
        cursor.execute('select * from usuario;')
        usuariosBD = cursor.fetchall()

        for usuario in usuariosBD:
            cont += 1
            usuarioNome = str(usuario[1])
            usuarioSenha = str(usuario[2])

            if usuarioNome == nome and usuarioSenha == senha:
                return render_template('home.html')
            
            if cont >= len(usuariosBD):
                flash('USUARIO INVALIDO')
                return redirect("/")
            
@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    user = []
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    conect_BD = mysql.connector.connect(host='localhost', database='usuarios',
     user='root', password='projetoapp01@')
    
    if conect_BD.is_connected():
        cursor = conect_BD.cursor()
        cursor.execute(f"insert into usuario values (default, '{nome}', '{senha}');")
    if conect_BD.is_connected():
            cursor.close()
            conect_BD.close()
    
    return render_template("home.html")        

if __name__ in "__main__":
    app.run(debug=True)   