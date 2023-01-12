from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

#pagina_inicial! carrega ao entrar no sistema
@app.route('/')
def pagina_inicial():
  return render_template('inicio.html')

#Carrega a tela para realizar o login inserindo usuario e senha
  
@app.route('/entrar/')
def admin_index():
  return render_template('login.html')

#Efetua o teste que a rota entrar forneceu, redirecinando para a Tota de admin ou se acesso errado redireciona para entrar novamente
  
@app.route('/login/', methods=['POST', 'GET'])
def login():

  if request.method == 'POST':
    usuario = request.form['c_usuario']
    senha = request.form['c_senha']

    if usuario == "luana" and senha == "luana":
      return redirect(url_for('admin', nome=usuario, senha=senha))

    else:
      return redirect(url_for('entrar'))
    
  else:
    usuario = request.args.get('c_usuario')
    senha = request.args.get('c_senha')
    
    if usuario == "luana" and senha == "luana":
      return redirect(url_for('admin', nome=usuario, senha=senha))
      
    else:
      return redirect(url_for('entrar'))

#rota apenas para usuarios logados, chega aqui após percorrer a rota de login anterior e o acesso for concedido
      
@app.route('/admin/<nome>/<senha>')
def admin(nome, senha):
  frase = "<b>bem vindo</b>" + nome + "sua senha é:<i>" + senha + "</i>"
  return frase


if __name__ == '__main__':
  app.run('0.0.0.0')
