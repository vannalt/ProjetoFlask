from flask import Blueprint, request, jsonify

professor_bp = Blueprint('professor_bp', __name__)
professores = []

@professor_bp.route("/professores", methods=["POST"])
def criar_professor():
    dados = request.json
    professor = {
        "id": dados["id"],
        "nome": dados["nome"],
        "disciplina": dados["disciplina"],
        "idade": dados["idade"],
        "observacoes": dados["observacoes"]
    }
    professores.append(professor)
    return jsonify({"msg": "Professor criado com sucesso", "data": professor}), 201

@professor_bp.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(professores)

@professor_bp.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        return jsonify(professor)
    return jsonify({'erro': 'Professor não encontrado'}), 404

@professor_bp.route("/professores/<int:id>", methods=["PUT"])
def atualizar_professor(id):
    dados = request.json
    for professor in professores:
        if professor["id"] == id:
            professor.update(dados)
            return jsonify({"data": professor}), 200
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route("/professores/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    for i, professor in enumerate(professores):
        if professor["id"] == id:
            del professores[i]
            return jsonify({"msg": "Professor removido"}), 200
    return jsonify({"erro": "Professor não encontrado"}), 404