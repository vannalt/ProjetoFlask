from flask_restx import Namespace, Resource, fields
from models.turma_model import listar_turmas, adicionar_turma, turma_por_id, atualizar_turma, excluir_turma, TurmaNaoEncontrada

api_turmas = Namespace('Turma', description="Operações relacionadas às turmas")

turma_input_model = api_turmas.model("TurmaInput", {
    "nome": fields.String(required=True, description="Nome da turma"),
    "professor_id": fields.Integer(required=True, description="ID do professor responsável"),
})

turma_output_model = api_turmas.model("TurmaOutput", {
    "id": fields.Integer(description="ID da turma"),
    "nome": fields.String(description="Nome da turma"),
    "professor_id": fields.Integer(description="ID do professor responsável"),
})

@api_turmas.route("/")
class TurmasResource(Resource):
    @api_turmas.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return listar_turmas()

    @api_turmas.expect(turma_input_model)
    def post(self):
        """Adiciona uma nova turma"""
        data = api_turmas.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@api_turmas.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @api_turmas.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        try:
            return turma_por_id(id_turma)
        except TurmaNaoEncontrada as e:
            return {"message": str(e)}, 404

    @api_turmas.expect(turma_input_model)
    def put(self, id_turma):
        """Atualiza uma turma pelo ID"""
        data = api_turmas.payload
        try:
            return atualizar_turma(id_turma, data)
        except TurmaNaoEncontrada as e:
            return {"message": str(e)}, 404

    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        try:
            return excluir_turma(id_turma)
        except TurmaNaoEncontrada as e:
            return {"message": str(e)}, 404
