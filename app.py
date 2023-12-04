from flask import Flask, render_template, request
import pandas as pd
from graficos import visualizacao_dados
import joblib
data = pd.read_csv('data/proUni2017_tratados.csv', index_col=0)
vis = visualizacao_dados(data)
vis.count_plot_target()
vis.count_plot_df()



# Carregar modelo com joblib
modelo = joblib.load('modelo_arvore_decisao.pkl')


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

@app.route('/minhasmetricas', methods=['POST','GET'])
def minhasmetricas():  
    nome_instituicao = int(request.form['NOME_IES_BOLSA'])
    modalidade_ensino = int(request.form['MODALIDADE_ENSINO_BOLSA'])
    deficiencia = int(request.form['BENEFICIARIO_DEFICIENTE_FISICO'])
    nome_curso = int(request.form['NOME_CURSO_BOLSA'])
    turno = int(request.form['NOME_TURNO_CURSO_BOLSA'])
    sexo = int(request.form['SEXO_BENEFICIARIO_BOLSA'])
    raca_cor = int(request.form['RACA_BENEFICIARIO_BOLSA'])
    regiao = int(request.form['REGIAO_BENEFICIARIO_BOLSA'])
    uf = int(request.form['SIGLA_UF_BENEFICIARIO_BOLSA'])

    # Compile os dados em um dicionário
    dados_para_ia = {
        'NOME_IES_BOLSA': nome_instituicao,
        'MODALIDADE_ENSINO_BOLSA': modalidade_ensino,
        'NOME_CURSO_BOLSA': nome_curso,
        'NOME_TURNO_CURSO_BOLSA': turno,
        'SEXO_BENEFICIARIO_BOLSA': sexo,
        'RACA_BENEFICIARIO_BOLSA': raca_cor,
        'BENEFICIARIO_DEFICIENTE_FISICO': deficiencia,
        'REGIAO_BENEFICIARIO_BOLSA':regiao,
        'SIGLA_UF_BENEFICIARIO_BOLSA':uf
        
        
    }

    dados_formatados = [list(dados_para_ia.values())]

    # Faça a previsão usando o modelo
    resultado_previsao = modelo.predict(dados_formatados)
    if resultado_previsao == 0:
        tipo_bolsa = 'BOLSA PARCIAL 50%'
    else:
        tipo_bolsa = 'BOLSA INTEGRAL'

    return render_template('minhasmetricas.html',resultado = tipo_bolsa)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/iniciarsessao')
def iniciarsessao():
    return render_template('iniciarsessao.html')







if __name__ == '__main__':
    app.run(debug=True)