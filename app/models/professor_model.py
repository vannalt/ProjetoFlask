from turma.turma_model import Turma
from config import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    turmas = db.relationship("Turma", back_populates="professor")  # Um professor pode ter várias turmas

    def __init__(self, nome, disciplina, idade, observacoes=None):
        self.nome = nome
        self.disciplina = disciplina
        self.idade = idade
        self.observacoes = observacoes

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'disciplina': self.disciplina,
            'idade': self.idade,
            'observacoes': self.observacoes
        }


class ProfessorNaoEncontrado(Exception):
    pass


def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado.")
    return professor.to_dict()


def listar_professores():
    professores = Professor.query.all()
    return [prof.to_dict() for prof in professores]


def adicionar_professor(novos_dados):
    novo_professor = Professor(
        nome=novos_dados['nome'],
        disciplina=novos_dados['disciplina'],
        idade=int(novos_dados['idade']),
        observacoes=novos_dados.get('observacoes')
    )

    db.session.add(novo_professor)
    db.session.commit()
    return {"message": "Professor adicionado com sucesso!"}, 201


def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado()

    professor.nome = novos_dados['nome']
    professor.disciplina = novos_dados['disciplina']
    professor.idade = int(novos_dados['idade'])
    professor.observacoes = novos_dados.get('observacoes')

    db.session.commit()
    return {"message": "Professor atualizado com sucesso!"}, 200


def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado.")

    db.session.delete(professor)
    db.session.commit()
    return {"message": "Professor excluído com sucesso!"}, 200
