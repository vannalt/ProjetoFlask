class Aluno:
    def __init__(self, nome, data_de_nascimento, turma_id, id=None):
        self.id = id
        self.nome = nome
        self.turma_id = turma_id
        self.data_de_nascimento = data_de_nascimento

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_de_nascimento": self.data_de_nascimento,
            "turma_id": self.turma_id
        }
