from . import db


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    semestre = db.Column(db.String(32))

    def __repr__(self):
        return '<Disciplina %r>' % self.name
