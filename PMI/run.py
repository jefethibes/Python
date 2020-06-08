from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import CSRFProtect
from conexao import Conexao
from forms import Chamados, Login, CriarUsuario
from datetime import date
from functools import wraps


app = Flask(__name__)
app.secret_key = 'não_me_hackeia_plz'
csrf = CSRFProtect(app)

conexao = Conexao()


def date_format():
    data_atual = date.today()
    data_str = data_atual.strftime('%d/%m/%Y')
    return data_str


def login_required(run):
	@wraps(run)
	def wrap(*args, **kwargs):
		if 'usuario' in session:
			return run(*args, **kwargs)
		else:
			flash('Por favor! Efetue o login primeiro')
			return redirect(url_for('login'))
	return wrap


@app.route('/index')
@login_required
def index():
    permissao = conexao.valida_permissao(session['usuario'])
    return render_template('index.html', permissao=permissao)


@app.route('/ti', methods=['GET', 'POST'])
@login_required
def ti():
    field = Chamados(request.form)
    title = 'Chamado TI!'
    setores = conexao.busca_administracao({'id': 0})['setores']
    permissao = conexao.valida_permissao(session['usuario'])
    if request.method == 'POST' and field.validate():
        status = 'Aberto'
        tipo = 'TI'
        setor = request.form['setor']
        titulo = request.form['titulo']
        urgencia = request.form['urgencia']
        comentario = request.form['comentario']
        data = date_format()
        usuario = session['usuario']
        json = {'status': status, 'tipo': tipo, 'setor': setor, 'urgencia': urgencia, 'titulo': titulo, 'comentario': comentario, 'data_abertura': data, 'usuario': usuario}
        conexao.chamados('chamados', json)
        mensagem = 'Chamado cadastrado com sucesso!'
        flash(mensagem)
        return redirect(url_for('meus_chamados'))
    return render_template('chamados.html', field=field, title=title, setores=setores, permissao=permissao)


@app.route('/impressoras', methods=['GET', 'POST'])
@login_required
def impressoras():
    field = Chamados(request.form)
    setores = conexao.busca_administracao({'id': 0})['setores']
    modelos = conexao.busca_administracao({'id': 1})['impressoras']
    permissao = conexao.valida_permissao(session['usuario'])
    if request.method == 'POST' and field.validate():
        status = 'Aberto'
        tipo = 'Impressoras'
        titulo = request.form['titulo']
        setor = request.form['setor']
        modelo = request.form['modelo']
        comentario = request.form['comentario']
        data = date_format()
        usuario = session['usuario']
        json = {'status': status, 'tipo': tipo, 'setor': setor, 'modelo': modelo, 'titulo': titulo, 'comentario': comentario, 'data_abertura': data, 'usuario': usuario}
        conexao.chamados('chamados', json)
        mensagem = 'Chamado cadastrado com sucesso!'
        flash(mensagem)
        return redirect(url_for('meus_chamados'))
    return render_template('chamados_impressoras.html', field=field, setores=setores, modelos=modelos, permissao=permissao)


@app.route('/manutencao', methods=['GET', 'POST'])
@login_required
def manutencao():
    field = Chamados(request.form)
    title = 'Chamado Manutenção!'
    setores = conexao.busca_administracao({'id': 0})['setores']
    permissao = conexao.valida_permissao(session['usuario'])
    if request.method == 'POST' and field.validate():
        status = 'Aberto'
        tipo = 'Manutencao'
        setor = request.form['setor']
        titulo = request.form['titulo']
        urgencia = request.form['urgencia']
        comentario = request.form['comentario']
        data = date_format()
        usuario = session['usuario']
        json = {'status': status, 'tipo': tipo, 'setor': setor, 'urgencia': urgencia, 'titulo': titulo, 'comentario': comentario, 'data_abertura': data, 'usuario': usuario}
        conexao.chamados('chamados', json)
        mensagem = 'Chamado cadastrado com sucesso!'
        flash(mensagem)
        return redirect(url_for('meus_chamados'))
    return render_template('chamados.html', field=field, title=title, setores=setores, permissao=permissao)


@app.route('/meus_chamados/', methods=['GET', 'POST'])
@login_required
def meus_chamados():
    chamados = conexao.meus_chamados('chamados')
    usuario = session['usuario']
    itens = []
    permissao = conexao.valida_permissao(session['usuario'])
    for i in chamados:
        if i['usuario'] == usuario:
            itens.append(i)
    return render_template('lista_chamados.html', itens=itens, permissao=permissao)


@app.route('/chamados_ti/', methods=['GET', 'POST'])
@login_required
def chamados_ti():
    chamados = conexao.meus_chamados('chamados')
    itens = []
    permissao = conexao.valida_permissao(session['usuario'])
    for i in chamados:
        if i['tipo'] == 'Impressoras' or i['tipo'] == 'TI':
            itens.append(i)
    return render_template('lista_chamados.html', itens=itens, permissao=permissao)


@app.route('/chamados_manutencao/', methods=['GET', 'POST'])
@login_required
def chamados_manutencao():
    chamados = conexao.meus_chamados('chamados')
    itens = []
    permissao = conexao.valida_permissao(session['usuario'])
    for i in chamados:
        if i['tipo'] == 'Manutencao':
            itens.append(i)
    return render_template('lista_chamados.html', itens=itens, permissao=permissao)


@app.route('/encerrar/<_id>', methods=['GET', 'POST'])
@login_required
def encerrar(_id):
    field = Chamados(request.form)
    itens = conexao.busca_chamado('chamados', _id)
    permissao = conexao.valida_permissao(session['usuario'])
    if request.method == 'POST':
        resolucao = request.form['comentario']
        itens['data_encerramento'] = date_format()
        itens['resolucao'] = resolucao
        itens['responsavel'] = session['usuario']
        itens['status'] = 'Encerrado'
        conexao.encerrar_chamado('chamados', _id, itens)
        return redirect(url_for('meus_chamados'))
    return render_template('encerrar_chamado.html', itens=itens, field=field, permissao=permissao)


@app.route('/administracao', methods=['GET'])
@login_required
def administracao():
    permissao = conexao.valida_permissao(session['usuario'])
    return render_template('administracao.html', permissao=permissao)


@app.route('/gerenciar_usuarios', methods=['GET', 'POST'])
@login_required
def gerenciar_usuarios():
    itens = conexao.meus_chamados('usuarios')
    permissao = conexao.valida_permissao(session['usuario'])
    return render_template('usuarios.html', itens=itens, permissao=permissao)


@app.route('/criar_usuario', methods=['GET', 'POST'])
@login_required
def criar_usuario():
    field = CriarUsuario(request.form)
    perm = conexao.valida_permissao(session['usuario'])
    setores = conexao.busca_administracao({'id': 0})['setores']
    if request.method == 'POST' and field.validate():
        usuario = request.form['usuario']
        valida_usuario = conexao.valida_login({'usuario': usuario})
        if valida_usuario is None:
            senha = request.form['senha']
            setor = request.form['setor']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            email = request.form['email']
            status = request.form['status']
            permissao = request.form['permissao']
            json = {'usuario': usuario, 'senha': senha, 'setor': setor, 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'status': status, 'permissao': permissao}
            conexao.chamados('usuarios', json)
            mensagem = 'Cadastro efetuado com sucesso!'
            flash(mensagem)
            return redirect(url_for('gerenciar_usuarios'))
        else:
            mensagem = 'Usuário já existe!'
            flash(mensagem)
            return redirect(url_for('criar_usuario'))
    return render_template('criar_usuario.html', field=field, permissao=perm, setores=setores)


@app.route('/alterar_usuario/<_id>', methods=['GET', 'POST'])
@login_required
def alterar_usuario(_id):
    itens = conexao.busca_chamado('usuarios', _id)
    permissao = conexao.valida_permissao(session['usuario'])
    setores = conexao.busca_administracao({'id': 0})['setores']
    if request.method == 'POST':
        '''usuario = request.form['usuario']
        senha = request.form['senha']
        setor = request.form['setor']
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        status = request.form['status']
        permissao = request.form['permissao']
        json = {'usuario': usuario, 'senha': senha, 'setor': setor, 'nome': nome, 'sobrenome': sobrenome,
                'email': email, 'status': status, 'permissao': permissao}
        conexao.encerrar_chamado('usuarios', _id, json)
        mensagem = 'Usuário alterado com sucesso!'
        flash(mensagem)'''
        return redirect(url_for('gerenciar_usuarios'))
    return render_template('alterar_usuario.html', itens=itens, permissao=permissao, setores=setores)


@app.route('/', methods=['GET', 'POST'])
def login():
    field = Login(request.form)
    if request.method == 'POST' and field.validate():
        usuario = request.form['usuario']
        senha = request.form['senha']
        json = {'usuario': usuario, 'senha': senha}
        valida_login = conexao.valida_login(json)
        if valida_login is None:
            mensagem = 'Usuário ou senha invalido!'
            flash(mensagem)
            return redirect(url_for('login'))
        else:
            if valida_login['status'] == 'Ativo':
                if valida_login['permissao'] == 'Administrador':
                    mensagem = 'Bem vindo Administrador!'
                    flash(mensagem)
                    session['usuario'] = field.usuario.data
                    permissao = 'Administrador'
                    return render_template('index.html', permissao=permissao)
                elif valida_login['permissao'] == 'Suporte TI':
                    mensagem = 'Bem vindo Suporte TI!'
                    flash(mensagem)
                    session['usuario'] = field.usuario.data
                    permissao = 'SuporteTI'
                    return render_template('index.html', permissao=permissao)
                elif valida_login['permissao'] == 'Suporte Manutenção':
                    mensagem = 'Bem vindo Suporte Manutenção!'
                    flash(mensagem)
                    session['usuario'] = field.usuario.data
                    permissao = 'SuporteM'
                    return render_template('index.html', permissao=permissao)
                else:
                    mensagem = 'Bem vindo Colaborador!'
                    flash(mensagem)
                    session['usuario'] = field.usuario.data
                    return redirect(url_for('index'))

            else:
                mensagem = 'Usuário Bloqueado! Favor procure o Administrador!'
                flash(mensagem)
                return redirect(url_for('login'))
    return render_template('login.html', field=field)


@app.route('/logout')
@login_required
def logout():
    if 'usuario' in session:
        session.pop('usuario')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
