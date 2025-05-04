from flask_restx import Namespace, Resource, fields
from models.professor_model import listar_professores, adicionar_professor, professor_por_id, atualizar_professor, excluir_professor, ProfessorNaoEncontrado

api_professores = Namespace('Professor', description="Operações relacionadas aos professores")

professor_input_model = api_professores.model("ProfessorInput", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "disciplina": fields.String(required=True, description="Disciplina lecionada"),
    "idade": fields.Integer(required=True, description="Idade do professor"),
    "observacoes": fields.String(required=False, description="Observações adicionais"),
})

professor_output_model = api_professores.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "disciplina": fields.String(description="Disciplina lecionada"),
    "idade": fields.Integer(description="Idade do professor"),
    "observacoes": fields.String(description="Observações adicionais"),
})

@api_professores.route("/")
class ProfessoresResource(Resource):
    @api_professores.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return listar_professores()

    @api_professores.expect(professor_input_model)
    def post(self):
        """Adiciona um novo professor"""
        data = api_professores.payload
        response, status_code = adicionar_professor(data)
        return response, status_code

@api_professores.route("/<int:id_professor>")
class ProfessorIdResource(Resource):
    @api_professores.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        try:
            return professor_por_id(id_professor)
        except ProfessorNaoEncontrado as e:
            return {"message": str(e)}, 404

    @api_professores.expect(professor_input_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = api_professores.payload
        try:
            return atualizar_professor(id_professor, data)
        except ProfessorNaoEncontrado:
            return {"message": "Professor não encontrado."}, 404

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        try:
            return excluir_professor(id_professor)
        except ProfessorNaoEncontrado as e:
            return {"message": str(e)}, 404

