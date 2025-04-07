from flask import Blueprint, request, jsonify

aluno_bp = Blueprint('aluno_bp', __name__)
alunos = []

@aluno_bp.route("/alunos", methods=["POST"])
def criar_aluno():
    dados = request.json
    aluno = {
        "id": dados["id"],
        "nome": dados["nome"],
        "turma_id": dados["turma_id"],
        "data_de_nascimento": dados["data_de_nascimento"]
    }
    alunos.append(aluno)
    return jsonify({"msg": "Aluno criado com sucesso", "data": aluno}), 201

@aluno_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({'erro': 'Aluno não encontrado'}), 404

@aluno_bp.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    dados = request.json
    for aluno in alunos:
        if aluno["id"] == id:
            aluno.update(dados)
            return jsonify({"data": aluno}), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404

@aluno_bp.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    for i, aluno in enumerate(alunos):
        if aluno["id"] == id:
            del alunos[i]
            return jsonify({"msg": "Aluno removido"}), 200
    return jsonify({"erro": "Aluno não encontrado"}), 404