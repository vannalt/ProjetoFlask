from flask import Blueprint, request, jsonify
from .turma_model import (
    TurmaNaoEncontrada,
    listar_turmas,
    turma_por_id,
    adicionar_turma,
    atualizar_turma,
    excluir_turma
)
from professor_model import Professor  # Para verificar professor em detalhes, se necessário

turmas_bp = Blueprint('turmas', __name__)


# GET /turmas — Lista todas as turmas
@turmas_bp.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return jsonify(turmas)


# GET /turmas/<id> — Busca uma turma por ID
@turmas_bp.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        professor = Professor.query.get(turma['professor_id'])
        if not professor:
            return jsonify({'message': 'Professor não encontrado'}), 404
        return jsonify({"turma": turma, "professor": professor.to_dict()})
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404


# POST /turmas — Cria uma nova turma
@turmas_bp.route('/turmas', methods=['POST'])
def create_turma():
    try:
        data = request.json
        response, status_code = adicionar_turma(data)
        return jsonify(response), status_code
    except Exception as e:
        print(f"Erro ao criar turma: {str(e)}")
        return jsonify({'error': 'Erro interno'}), 500


# PUT /turmas/<id> — Atualiza os dados de uma turma
@turmas_bp.route('/turmas/<int:id_turma>', methods=['PUT'])
def update_turma(id_turma):
    try:
        data = request.json
        response, status = atualizar_turma(id_turma, data)
        return jsonify(response), status
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': 'Erro ao atualizar turma'}), 500


# DELETE /turmas/<id> — Exclui uma turma
@turmas_bp.route('/turmas/<int:id_turma>', methods=['DELETE'])
def delete_turma(id_turma):
    try:
        response, status = excluir_turma(id_turma)
        return jsonify(response), status
    except TurmaNaoEncontrada:
        return jsonify({'message': 'Turma não encontrada'}), 404
