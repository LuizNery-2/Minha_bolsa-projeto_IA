from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina/<nome_pagina>')
def pagina(nome_pagina):
    return render_template(f'{nome_pagina}.html')

if __name__ == '__main__':
    app.run(debug=True)