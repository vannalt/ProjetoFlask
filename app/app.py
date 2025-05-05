import pytest
import os
import sys
from flask import Flask
from flask_jwt_extended import JWTManager
from config import db
from app.controllers.aluno_controller import alunos_bp
from controllers.turma_controller import turmas_bp
from controllers.professor_controller import professores_bp
from ..swagger.swagger_config import configure_swagger

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'GZ5!iQ98yV6p^kz#2A1tq$hFg2zL4bE+HW'
app.config['HOST'] = 'localhost'
app.config['PORT'] = 5000
app.config['DEBUG'] = True

jwt = JWTManager(app)

app.register_blueprint(alunos_bp, url_prefix='/api')
app.register_blueprint(turmas_bp, url_prefix='/api')
app.register_blueprint(professores_bp, url_prefix='/api')

configure_swagger(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
