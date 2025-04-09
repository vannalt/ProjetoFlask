class Professor:
    def __init__(self, id, nome, disciplina, idade, observacoes):
         self.id = id
         self.nome = nome
         self.disciplina = disciplina
         self.idade = idade
         self.observacoes = observacoes
         
    def to_dict(self):
        return {
            "professor_id": self.id,
            "nome": self.nome,
            "disciplina": self.disciplina,
            "idade": self.idade,
            "observacoes": self.observacoes
        }
