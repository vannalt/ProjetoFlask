from flask import Flask
from app.controllers.aluno_controller import aluno_bp

app = Flask(__name__)
app.register_blueprint(aluno_bp)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# class Professor:
#     def __init__(self, id, nome, disciplina, idade, observacoes):
#         self.id = id
#         self.nome = nome
#         self.disciplina = disciplina
#         self.idade = idade
#         self.observacoes = observacoes


# class Turma:
#     def __init__(self, id, nome, professor_id):
#         self.id = id
#         self.nome = nome
#         self.professor_id = professor_id

# #---PROFESSORES--------------------------------------------------

# @app.route("/professores", methods=['GET'])
# def get_professores():
#     return jsonify([vars(p) for p in db["professores"]])

# @app.route("/professores/<int:id>", methods=['GET'])
# def get_professor(id):
#     professor = next((p for p in db["professores"] if p.id == id), None)
#     if not professor:
#         return jsonify({"error": "Professor não encontrado"})
#     return jsonify(vars(professor))

# @app.route("/professores", methods=['POST'])
# def create_professor():
#     data = request.json
#     professor = Professor(**data)
#     db["professores"].append(professor)
#     return jsonify({"msg": "Professor adicionado", "data": vars(professor)})

# @app.route("/professores/<int:id>", methods=['PUT'])
# def update_professor(id):
#     professor = next((p for p in db["professores"] if p.id == id), None)
#     if not professor:
#         return jsonify({"error": "Professor não encontrado"})
#     data = request.json
#     professor.nome = data.get('nome', professor.nome)
#     professor.disciplina = data.get('disciplina', professor.disciplina)
#     professor.idade = data.get('idade', professor.idade)
#     professor.observacoes = data.get('observacoes', professor.observacoes)
#     return jsonify({"msg": "Professor atualizado", "data": vars(professor)})

# @app.route("/professores/<int:id>", methods=['DELETE'])
# def delete_professor(id):
#     professor = next((p for p in db["professores"] if p.id == id), None)
#     if not professor:
#         return jsonify({"error": "Professor não encontrado"})
#     db["professores"].remove(professor)
#     return jsonify({"msg": "Professor removido"})


# #---TURMAS-------------------------------------------------------

# @app.route("/turmas", methods=['GET'])
# def get_turmas():
#     return jsonify([vars(t) for t in db["turmas"]])

# @app.route("/turmas/<int:id>", methods=['GET'])
# def get_turma(id):
#     turma = next((t for t in db["turmas"] if t.id == id), None)
#     if not turma:
#         return jsonify({"error": "Turma não encontrada"})
#     return jsonify(vars(turma))

# @app.route("/turmas", methods=['POST'])
# def create_turma():
#     data = request.json
#     professor = next((p for p in db["professores"] if p.id == data["professor_id"]), None)
#     if not professor:
#         return jsonify({"error": "Professor não encontrado"})
#     turma = Turma(**data)
#     db["turmas"].append(turma)
#     return jsonify({"msg": "Turma adicionada", "data": vars(turma)})

# @app.route("/turmas/<int:id>", methods=['PUT'])
# def update_turma(id):
#     turma = next((t for t in db["turmas"] if t.id == id), None)
#     if not turma:
#         return jsonify({"error": "Turma não encontrada"})
#     data = request.json
#     turma.nome = data.get('nome', turma.nome)
#     turma.professor_id = data.get('professor_id', turma.professor_id)
#     return jsonify({"msg": "Turma atualizada", "data": vars(turma)})

# @app.route("/turmas/<int:id>", methods=['DELETE'])
# def delete_turma(id):
#     turma = next((t for t in db["turmas"] if t.id == id), None)
#     if not turma:
#         return jsonify({"error": "Turma não encontrada"})
#     db["turmas"].remove(turma)
#     return jsonify({"msg": "Turma removida"}) #

# #---MAIN---DEBUG-------------------------------------------------

