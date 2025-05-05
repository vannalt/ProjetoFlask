import pytest
from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client



def test_criar_aluno(client):
    response = client.post('/alunos', json={
        "id": 1,
        "nome": "João",
        "turma_id": 101,
        "data_de_nascimento": "2005-09-01"
    })
    assert response.status_code == 201
    assert response.get_json()["msg"] == "Aluno criado com sucesso"

def test_listar_alunos(client):
    response = client.get('/alunos')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_buscar_aluno_por_id(client):
    client.post('/alunos', json={
        "id": 2,
        "nome": "Maria",
        "turma_id": 102,
        "data_de_nascimento": "2006-01-15"
    })
    response = client.get('/alunos/2')
    assert response.status_code == 200
    assert response.get_json()["nome"] == "Maria"

def test_atualizar_aluno(client):
    client.post('/alunos', json={
        "id": 3,
        "nome": "Carlos",
        "turma_id": 103,
        "data_de_nascimento": "2007-04-22"
    })
    response = client.put('/alunos/3', json={
        "nome": "Carlos Silva"
    })
    assert response.status_code == 200
    assert response.get_json()["data"]["nome"] == "Carlos Silva"

def test_deletar_aluno(client):
    client.post('/alunos', json={
        "id": 4,
        "nome": "Ana",
        "turma_id": 104,
        "data_de_nascimento": "2008-12-12"
    })
    response = client.delete('/alunos/4')
    assert response.status_code == 200
    assert response.get_json()["msg"] == "Aluno removido"

