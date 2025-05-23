from flask_restx import Namespace, Resource, fields
from models.aluno_model import listar_alunos, adicionar_aluno, aluno_por_id, atualizar_aluno, excluir_aluno

api_alunos = Namespace('Pessoa', description="Operações relacionadas aos alunos")

aluno_input_model = api_alunos.model("AlunoInput", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
})

aluno_output_model = api_alunos.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(description="Nota do segundo semestre"),
    "media_final": fields.Float(description="Média final do aluno"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@api_alunos.route("/")
class AlunosResource(Resource):
    @api_alunos.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista de todos os alunos"""
        return listar_alunos()

    @api_alunos.expect(aluno_input_model)
    def post(self):
        """Cria um novo aluno"""
        data = api_alunos.payload
        response, status_code = adicionar_aluno(data)
        return response, status_code

@api_alunos.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @api_alunos.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        """Obtém um aluno pelo ID"""
        return aluno_por_id(id_aluno)

    @api_alunos.expect(aluno_input_model)
    def put(self, id_aluno):
        """Atualiza um aluno pelo ID"""
        data = api_alunos.payload
        atualizar_aluno(id_aluno, data)
        return data, 200

    def delete(self, id_aluno):
        """Exclui um aluno pelo ID"""
        excluir_aluno(id_aluno)
        return {"message": "Aluno excluído com sucesso"}, 200
