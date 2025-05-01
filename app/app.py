from swagger.swagger_config import configure_swagger
import pytest
import sys
import os
from config import app, db
from alunos.routeAluno import alunos_blueprint
from professores.routeProfessor import professores_blueprint
from turmas.routeTurma import turmas_blueprint


app = Flask(__name__)
app.register_blueprint(aluno_bp) 
app.register_blueprint(turma_bp) 
app.register_blueprint(professor_bp)

configure_swagger(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)






