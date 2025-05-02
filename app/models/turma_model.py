from config import db
from professor_model import Professor

class Turma(db.Model):
    __tablename__ = "turma"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)

    # Relacionamento com Professor
    professor = db.relationship("Professor", back_populates="turmas")

    def __init__(self, nome, professor_id):
        self.nome = nome
        self.professor_id = professor_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "professor_id": self.professor_id
        }

# Exceção personalizada
class TurmaNaoEncontrada(Exception):
    pass

# Funções CRUD

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada("Turma não encontrada.")
    return turma.to_dict()

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(novos_dados):
    professor = Professor.query.get(novos_dados['professor_id'])
    if not professor:
        return {"message": "Professor não encontrado"}, 404

    nova_turma = Turma(
        nome=novos_dados['nome'],
        professor_id=novos_dados['professor_id']
    )

    db.session.add(nova_turma)
    db.session.commit()
    return {"message": "Turma adicionada com sucesso!"}, 201

def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada("Turma não encontrada.")

    professor = Professor.query.get(novos_dados['professor_id'])
    if not professor:
        return {"message": "Professor não encontrado"}, 404

    turma.nome = novos_dados['nome']
    turma.professor_id = novos_dados['professor_id']

    db.session.commit()
    return {"message": "Turma atualizada com sucesso!"}, 200

def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada("Turma não encontrada.")

    db.session.delete(turma)
    db.session.commit()
    return {"message": "Turma excluida!"}, 200