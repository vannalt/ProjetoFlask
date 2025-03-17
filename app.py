from flask import Flask, jsonify

app = Flask(__name__)

db = {
    "professores": [],
    "turmas": [],
    "alunos": []
}

class Professor:
    def __init__(self, id, nome, disciplina):
        self.id = id
        self.nome = nome
        self.disciplina = disciplina

class Aluno:
    def __init__(self, id, nome, turma):
        self.id = id
        self.nome = nome
        self.turma = turma

class Turma:
    def __init__(self, id, nome, professor):
        self.id = id
        self.nome = nome
        self.professor = professor
#----------------------------------------------------------------
@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify(db["professores"])

@app.route("/professores", methods=['POST'])
def create_professor():
    data = request.json
    db["professores"].append(data)
    return jsonify({"msg": "Professor adicionado", "data": data})

@app.route("/professores/<int:index>", methods=['PUT'])
def update_professor(id):
    if id >= len(db["professores"]):
        return jsonify({"error": "Professor não encontrado"})
    db["professores"][id] = request.json
    return jsonify({"msg": "Professor atualizado", "data": db["professores"][id]})

@app.route("/alunos/<int:index>", methods=['DELETE'])
def delete_professor(id):
    if id >= len(db["profssores"]):
        return jsonify({"error": "Professor não encontrado"})
    db["professores"].pop(id)
    return jsonify({"msg": "Professor removido"})


#-------------------------------------------------------------------------------

@app.route("/alunos", methods=['GET'])
def get_alunos():
    return jsonify(db["alunos"])

@app.route("/alunos", methods=['POST'])
def create_aluno():
    data = request.json
    db["alunos"].append(data)
    return jsonify({"msg": "Aluno adicionado", "data": data})

@app.route("/alunos/<int:index>", methods=['PUT'])
def update_aluno(id):
    if id >= len(db["alunos"]):
        return jsonify({"error": "Aluno não encontrado"})
    db["alunos"][id] = request.json
    return jsonify({"msg": "Aluno atualizado", "data": db["alunos"][id]})

@app.route("/alunos/<int:index>", methods=['DELETE'])
def delete_aluno(id):
    if id >= len(db["alunos"]):
        return jsonify({"error": "Aluno não encontrado"})
    db["alunos"].pop(id)
    return jsonify({"msg": "Aluno removido"})

#----------------------------------------------------------------

@app.route("/turmas", methods=['GET'])
def get_turmas():
    return jsonify(db["turmas"])

@app.route("/turmas", methods=['POST'])
def create_turma():
    data = request.json
    db["turmas"].append(data)
    return jsonify({"msg": "Turma adicionada", "data": data})

@app.route("/turmas/<int:index>", methods=['PUT'])
def update_turma(id):
    if id >= len(db["turmas"]):
        return jsonify({"error": "Turma não encontrada"})
    db["turmas"][id] = request.json
    return jsonify({"msg": "Turma atualizada", "data": db["turmas"][id]})

@app.route("/turmas/<int:index>", methods=['DELETE'])
def delete_turma(id):
    if id >= len(db["turmas"]):
        return jsonify({"error": "Turma não encontrada"}), 
    db["turmas"].pop(id)
    return jsonify({"msg": "Turma removida"})


if __name__ == "__main__":
    app.run(debug=True)

