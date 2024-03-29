from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados de exemplo (substitua isso com uma base de dados real)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('success'))
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Login bem sucedido!"

if __name__ == '__main__':
    app.run(debug=True)
