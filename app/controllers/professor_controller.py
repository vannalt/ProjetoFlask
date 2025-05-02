from flask import Blueprint, request, jsonify
from .professor_model import (
    ProfessorNaoEncontrado,
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor
)

professores_bp = Blueprint('professores', __name__)

# GET /professores — Lista todos os professores
@professores_bp.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return jsonify(professores)


# GET /professores/<id> — Retorna professor por ID
@professores_bp.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404


# POST /professores — Cria um novo professor
@professores_bp.route('/professores', methods=['POST'])
def create_professor():
    try:
        data = request.json
        response, status_code = adicionar_professor(data)
        return jsonify(response), status_code
    except Exception as e:
        print(f"Erro ao criar professor: {str(e)}")
        return jsonify({"error": "Erro interno"}), 500


# PUT /professores/<id> — Atualiza um professor existente
@professores_bp.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    try:
        data = request.json
        atualizar_professor(id_professor, data)
        return jsonify({'message': 'Professor atualizado com sucesso'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': 'Erro interno ao atualizar professor'}), 500


# DELETE /professores/<id> — Exclui um professor
@professores_bp.route('/professores/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return jsonify({'message': 'Professor excluído com sucesso'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
