import pytest
import os
import sys

from ..swagger.swagger_config import configure_swagger
from config import app, db
from controllers.aluno_controller import alunos_bp
from controllers.turma_controller import turmas_bp
from controllers.professor_controller import professores_bp
from ..swagger.swagger_config import configure_swagger
from flask import Flask
from flask_jwt_extended import JWTManager

app.register_blueprint(alunos_bp, url_prefix='/api')
app.register_blueprint(turmas_bp, url_prefix='/api')
app.register_blueprint(professores_bp, url_prefix='/api')

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_segura_aqui'
jwt = JWTManager(app)

configure_swagger(app)

with app.app_context():
    db.create_all()



if __name__ == '__main__':  
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])





