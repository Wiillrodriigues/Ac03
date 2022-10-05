import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')


@app.route('/serializar', methods = ['POST'])
def serializar():
    pri_nome = request.form['_first_name']
    ult_nome = request.form['_last_name']
    posicao = request.form['_posicao']
    return jsonify(_first_name = pri_nome.upper(), _last_name = ult_nome.upper(), _posicao = posicao.upper())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port )
