from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

SEMESTRES = ['1º semestre', '2º semestre', '3º semestre',
             '4º semestre', '5º semestre', '6º semestre']


class DisciplinaForm(FlaskForm):
    name = StringField('Cadastre a nova disciplina e o semestre associado:',
                       validators=[DataRequired()])
    semester = RadioField(choices=[(s, s) for s in SEMESTRES])
    submit = SubmitField('Cadastrar')
