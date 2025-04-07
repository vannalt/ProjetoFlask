class Turma:
    def __init__(self, id, nome, professor_id):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "professor_id": self.professor_id
        }
