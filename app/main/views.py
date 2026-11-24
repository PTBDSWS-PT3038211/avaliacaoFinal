from datetime import datetime, timezone
from flask import render_template, redirect, url_for, flash, current_app
from .. import db
from ..models import Disciplina
from . import main
from .forms import DisciplinaForm


def agora_utc():
    # Flask-Moment espera um datetime "ingênuo" em UTC
    return datetime.now(timezone.utc).replace(tzinfo=None)


@main.route('/')
def index():
    return render_template('index.html',
                           nome=current_app.config['ALUNO_NOME'],
                           prontuario=current_app.config['ALUNO_PRONTUARIO'],
                           current_time=agora_utc())


@main.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    form = DisciplinaForm()
    if form.validate_on_submit():
        nome = form.name.data.strip()
        if Disciplina.query.filter_by(name=nome).first() is None:
            db.session.add(Disciplina(name=nome, semestre=form.semester.data))
            db.session.commit()
            flash('Disciplina cadastrada com sucesso!')
        else:
            flash('Disciplina já cadastrada.')
        return redirect(url_for('.disciplinas'))
    if form.is_submitted():
        flash('Informe o nome da disciplina e selecione o semestre.')
    lista = Disciplina.query.order_by(Disciplina.id).all()
    return render_template('disciplinas.html', form=form, disciplinas=lista)


# Módulos não desenvolvidos: apenas informam "Não disponível"
@main.route('/professores')
@main.route('/alunos')
@main.route('/cursos')
@main.route('/ocorrencias')
def nao_disponivel():
    return render_template('nao_disponivel.html', current_time=agora_utc())
