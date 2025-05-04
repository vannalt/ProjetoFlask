from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app import db
from models.professor_model import (
    ProfessorNaoEncontrado,
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor,
    Professor
)

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return jsonify(professores)

@professores_bp.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404

@professores_bp.route('/professores', methods=['POST'])
def create_professor():
    try:
        data = request.json
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')

        if not nome or not email or not senha:
            return jsonify({"error": "Nome, email e senha são obrigatórios"}), 400

        if Professor.query.filter_by(email=email).first():
            return jsonify({"error": "Email já cadastrado"}), 400

        novo_professor = Professor(nome=nome, email=email)
        novo_professor.set_senha(senha)

        db.session.add(novo_professor)
        db.session.commit()

        access_token = create_access_token(identity=novo_professor.id)

        return jsonify({
            "msg": "Professor cadastrado com sucesso",
            "token": access_token
        }), 201

    except Exception as e:
        print(f"Erro ao criar professor: {str(e)}")
        return jsonify({"error": "Erro interno ao criar professor"}), 500

@professores_bp.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    try:
        data = request.json
        atualizar_professor(id_professor, data)
        return jsonify({'message': 'Professor atualizado com sucesso'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'Erro interno ao atualizar professor: {str(e)}'}), 500

@professores_bp.route('/professores/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    try:
        excluir_professor(id_professor)
        return jsonify({'message': 'Professor excluído com sucesso'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'message': 'Professor não encontrado'}), 404

@professores_bp.route('/login', methods=['POST'])
def login_professor():
    try:
        data = request.json
        email = data.get('email')
        senha = data.get('senha')

        professor = Professor.query.filter_by(email=email).first()

        if not professor or not professor.verificar_senha(senha):
            return jsonify({"error": "Credenciais inválidas"}), 401

        token = create_access_token(identity=professor.id)
        return jsonify({"token": token}), 200

    except Exception as e:
        print(f"Erro no login: {str(e)}")
        return jsonify({"error": "Erro interno no servidor"}), 500
