from flask_restx import Namespace, Resource, fields

from models.aluno_model import listar_alunos, adicionar_aluno, aluno_por_id, atualizar_aluno, excluir_aluno

api = Namespace('Pessoa',description="Operações relacionadas aos alunos")
