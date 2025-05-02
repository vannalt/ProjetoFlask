from swagger.swagger_config import configure_swagger
import pytest
import os
import sys
from config import app, db
from alunos.alunos_routes import alunos_bp
from turma.turma_routes import turmas_bp
from professor.professor_routes import professores_bp


app.register_blueprint(alunos_bp, url_prefix='/api')
app.register_blueprint(turmas_bp, url_prefix='/api')
app.register_blueprint(professores_bp, url_prefix='/api')

configure_swagger(app)

with app.app_context():
    db.create_all()



if __name__ == '__main__':  
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])





