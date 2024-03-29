from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aqui você pode adicionar a lógica para verificar o username e password

        # Exemplo de verificação simples
        if username == 'admin' and password == 'admin':
            return 'Login bem-sucedido!'
        else:
            return 'Login falhou!'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
