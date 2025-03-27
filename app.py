from flask import Flask, jsonify, request

app = Flask(__name__)

db = {
    "professores": [],
    "turmas": [],
    "alunos": []
}

class Professor:
    def __init__(self, id, nome, disciplina, idade, observacoes):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina
        self.idade = idade
        self.observacoes = observacoes

class Aluno:
    def __init__(self, id, nome, turma_id, data_de_nascimento):
        self.id = id
        self.nome = nome
        self.turma_id = turma_id
        self.data_de_nascimento = data_de_nascimento

class Turma:
    def __init__(self, id, nome, professor_id):
        self.id = id
        self.nome = nome
        self.professor_id = professor_id

#---PROFESSORES--------------------------------------------------

@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify([vars(p) for p in db["professores"]])

@app.route("/professores/<int:id>", methods=['GET'])
def get_professor(id):
    professor = next((p for p in db["professores"] if p.id == id), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"})
    return jsonify(vars(professor))

@app.route("/professores", methods=['POST'])
def create_professor():
    data = request.json
    professor = Professor(**data)
    db["professores"].append(professor)
    return jsonify({"msg": "Professor adicionado", "data": vars(professor)})

@app.route("/professores/<int:id>", methods=['PUT'])
def update_professor(id):
    professor = next((p for p in db["professores"] if p.id == id), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"})
    data = request.json
    professor.nome = data.get('nome', professor.nome)
    professor.disciplina = data.get('disciplina', professor.disciplina)
    professor.idade = data.get('idade', professor.idade)
    professor.observacoes = data.get('observacoes', professor.observacoes)
    return jsonify({"msg": "Professor atualizado", "data": vars(professor)})

@app.route("/professores/<int:id>", methods=['DELETE'])
def delete_professor(id):
    professor = next((p for p in db["professores"] if p.id == id), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"})
    db["professores"].remove(professor)
    return jsonify({"msg": "Professor removido"})

#---ALUNOS-------------------------------------------------------

@app.route("/alunos", methods=['GET'])
def get_alunos():
    return jsonify([vars(a) for a in db["alunos"]])

@app.route("/alunos/<int:id>", methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in db["alunos"] if a.id == id), None)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"})
    return jsonify(vars(aluno))

@app.route("/alunos", methods=['POST'])
def create_aluno():
    data = request.json
    turma = next((t for t in db["turmas"] if t.id == data["turma_id"]), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"})
    aluno = Aluno(**data)
    db["alunos"].append(aluno)
    return jsonify({"msg": "Aluno adicionado", "data": vars(aluno)})

@app.route("/alunos/<int:id>", methods=['PUT'])
def update_aluno(id):
    aluno = next((a for a in db["alunos"] if a.id == id), None)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"})
    data = request.json
    aluno.nome = data.get('nome', aluno.nome)
    aluno.turma_id = data.get('turma_id', aluno.turma_id)
    aluno.data_de_nascimento = data.get('data_de_nascimento', aluno.data_de_nascimento)
    return jsonify({"msg": "Aluno atualizado", "data": vars(aluno)})

@app.route("/alunos/<int:id>", methods=['DELETE'])
def delete_aluno(id):
    aluno = next((a for a in db["alunos"] if a.id == id), None)
    if not aluno:
        return jsonify({"error": "Aluno não encontrado"})
    db["alunos"].remove(aluno)
    return jsonify({"msg": "Aluno removido"})

#---TURMAS-------------------------------------------------------

@app.route("/turmas", methods=['GET'])
def get_turmas():
    return jsonify([vars(t) for t in db["turmas"]])

@app.route("/turmas/<int:id>", methods=['GET'])
def get_turma(id):
    turma = next((t for t in db["turmas"] if t.id == id), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"})
    return jsonify(vars(turma))

@app.route("/turmas", methods=['POST'])
def create_turma():
    data = request.json
    professor = next((p for p in db["professores"] if p.id == data["professor_id"]), None)
    if not professor:
        return jsonify({"error": "Professor não encontrado"})
    turma = Turma(**data)
    db["turmas"].append(turma)
    return jsonify({"msg": "Turma adicionada", "data": vars(turma)})

@app.route("/turmas/<int:id>", methods=['PUT'])
def update_turma(id):
    turma = next((t for t in db["turmas"] if t.id == id), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"})
    data = request.json
    turma.nome = data.get('nome', turma.nome)
    turma.professor_id = data.get('professor_id', turma.professor_id)
    return jsonify({"msg": "Turma atualizada", "data": vars(turma)})

@app.route("/turmas/<int:id>", methods=['DELETE'])
def delete_turma(id):
    turma = next((t for t in db["turmas"] if t.id == id), None)
    if not turma:
        return jsonify({"error": "Turma não encontrada"})
    db["turmas"].remove(turma)
    return jsonify({"msg": "Turma removida"})

#---MAIN---DEBUG-------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)