from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/minhasessao')
def minhasessao():
    return render_template('minhasessao.html')

@app.route('/minhasmetricas')
def minhasmetricas():    
    return render_template('minhasmetricas.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

app.route('/iniciarsessao')
def iniciarsessao():
    return render_template('iniciarsessao.html')






if __name__ == '__main__':
    app.run(debug=True)