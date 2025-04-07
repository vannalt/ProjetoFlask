from flask import Blueprint, request, jsonify

turma_bp = Blueprint('turma_bp', __name__)
turmas = []
professores = []

@turma_bp.route("/turmas", methods=["POST"])
def criar_turma():
    dados = request.json
    professor_id = dados.get("professor_id")
    professor = next((p for p in professores if p["id"] == professor_id), None)
    if not professor:
        return jsonify({"msg": "Professor não encontrado"}), 404

    turma = {
        "id": dados["id"],
        "nome": dados["nome"],
        "professor_id": professor_id
    }
    turmas.append(turma)
    return jsonify({"msg": "Turma criada com sucesso", "data": turma}), 201

@turma_bp.route("/turmas", methods=["GET"])
def listar_turmas():
    return jsonify({"data": turmas}), 200

@turma_bp.route("/turmas/<int:id>", methods=["GET"])
def buscar_turma(id):
    turma = next((t for t in turmas if t["id"] == id), None)
    if turma:
        return jsonify({"data": turma}), 200
    return jsonify({"msg": "Turma não encontrada"}), 404

@turma_bp.route("/turmas/<int:id>", methods=["PUT"])
def atualizar_turma(id):
    dados = request.json
    for turma in turmas:
        if turma["id"] == id:
            turma.update(dados)
            return jsonify({"msg": "Turma atualizada", "data": turma}), 200
    return jsonify({"msg": "Turma não encontrada"}), 404

@turma_bp.route("/turmas/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    for i, turma in enumerate(turmas):
        if turma["id"] == id:
            del turmas[i]
            return jsonify({"msg": "Turma removida"}), 200
    return jsonify({"msg": "Turma não encontrada"}), 404
