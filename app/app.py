import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask
from app.controllers.aluno_controller import aluno_bp
from app.controllers.turma_controller import turma_bp
from controllers.professor_controller import professor_bp

app = Flask(__name__)
app.register_blueprint(aluno_bp) 
app.register_blueprint(turma_bp) 
app.register_blueprint(professor_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)