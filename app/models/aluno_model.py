
from turma.turma_model import Turma
from datetime import datetime, date
from config import db


class Aluno(db.Model):
  __tablename__ = "alunos"

   
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100), nullable=False)
  idade = db.Column(db.Integer, nullable=False)
  data_nascimento = db.Column(db.Date, nullable=False)
  nota_primeiro_semestre = db.Column(db.Float, nullable=False)
  nota_segundo_semestre = db.Column(db.Float, nullable=False)
  media_final = db.Column(db.Float, nullable=False)
  
  turma = db.relationship("Turma", back_populates="alunos")
  turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)

  def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id,media_final):
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.nota_primeiro_semestre = nota_primeiro_semestre
    self.nota_segundo_semestre = nota_segundo_semestre
    self.turma_id = turma_id
    self.media_final = media_final
    self.idade = self.calcular_idade()
        





   


