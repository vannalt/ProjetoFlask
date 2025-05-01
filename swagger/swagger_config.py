from swagger import api
from swagger.namespaces.aluno_namespace import api_alunos
from swagger.namespaces.professor_namespace import professores_ns
from swagger.namespaces.turma_namespace import turmas_ns

def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(api_alunos, path="/alunos")
    api.add_namespace(professores_ns, path="/professores")
    api.add_namespace(turmas_ns, path="/turmas")
    api.mask_swagger = False
