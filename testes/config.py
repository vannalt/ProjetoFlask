import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestFlaskAPI(unittest.TestCase):
    
    # Testes para a rota /professores
    def test_create_professor(self):
        professor = {"nome": "Carlos", "disciplina": "Matemática", "idade": 40, "observacoes": "PHD em álgebra"}
        response = requests.post(f"{BASE_URL}/professores", json=professor)
        self.assertEqual(response.status_code, 200)
    
    def test_get_professores(self):
        response = requests.get(f"{BASE_URL}/professores")
        self.assertEqual(response.status_code, 200)
    
    def test_update_professor(self):
        updated_professor = {"nome": "Carlos Almeida", "disciplina": "Física", "idade": 41, "observacoes": "PHD em mecânica quântica"}
        response = requests.put(f"{BASE_URL}/professores/0", json=updated_professor)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_professor(self):
        response = requests.delete(f"{BASE_URL}/professores/0")
        self.assertEqual(response.status_code, 200)

    # Testes para a rota /alunos
    def test_create_aluno(self):
        aluno = {"nome": "Ana", "turma_id": 0, "data_de_nascimento": "2005-09-12"}
        response = requests.post(f"{BASE_URL}/alunos", json=aluno)
        self.assertEqual(response.status_code, 200)
    
    def test_get_alunos(self):
        response = requests.get(f"{BASE_URL}/alunos")
        self.assertEqual(response.status_code, 200)
    
    def test_update_aluno(self):
        updated_aluno = {"nome": "Ana Maria", "turma_id": 0, "data_de_nascimento": "2005-09-12"}
        response = requests.put(f"{BASE_URL}/alunos/0", json=updated_aluno)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_aluno(self):
        response = requests.delete(f"{BASE_URL}/alunos/0")
        self.assertEqual(response.status_code, 200)

    # Testes para a rota /turmas
    def test_create_turma(self):
        turma = {"nome": "Turma A", "professor": 0}
        response = requests.post(f"{BASE_URL}/turmas", json=turma)
        self.assertEqual(response.status_code, 200)
    
    def test_get_turmas(self):
        response = requests.get(f"{BASE_URL}/turmas")
        self.assertEqual(response.status_code, 200)
    
    def test_update_turma(self):
        updated_turma = {"nome": "Turma Avançada", "professor": 0}
        response = requests.put(f"{BASE_URL}/turmas/0", json=updated_turma)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_turma(self):
        response = requests.delete(f"{BASE_URL}/turmas/0")
        self.assertEqual(response.status_code, 200)

    # Testes para combinar várias operações
    def test_create_professor_and_turma(self):
        professor = {"nome": "Maria", "disciplina": "Química", "idade": 45, "observacoes": "PHD em Química Orgânica"}
        turma = {"nome": "Turma B", "professor": 1}
        response_professor = requests.post(f"{BASE_URL}/professores", json=professor)
        response_turma = requests.post(f"{BASE_URL}/turmas", json=turma)
        self.assertEqual(response_professor.status_code, 200)
        self.assertEqual(response_turma.status_code, 200)

    def test_create_aluno_with_turma(self):
        aluno = {"nome": "João", "turma_id": 1, "data_de_nascimento": "2004-05-20"}
        response = requests.post(f"{BASE_URL}/alunos", json=aluno)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_aluno_with_turma(self):
        response_aluno = requests.delete(f"{BASE_URL}/alunos/1")
        response_turma = requests.delete(f"{BASE_URL}/turmas/1")
        self.assertEqual(response_aluno.status_code, 200)
        self.assertEqual(response_turma.status_code, 200)

    # Testes para verificar respostas vazias
    def test_get_empty_professores(self):
        response = requests.get(f"{BASE_URL}/professores")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)
    
    def test_get_empty_alunos(self):
        response = requests.get(f"{BASE_URL}/alunos")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)
    
    def test_get_empty_turmas(self):
        response = requests.get(f"{BASE_URL}/turmas")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)

if __name__ == "__main__":
    unittest.main()