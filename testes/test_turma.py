import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_criar_turma(client):
    response = client.post('/turmas', json={
        "id": 101,
        "nome": "Turma A",
        "professor_id": 1
    })
    assert response.status_code == 201
    assert response.get_json()["msg"] == "Turma criada com sucesso"

def test_listar_turmas(client):
    response = client.get('/turmas')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_buscar_turma_por_id(client):
    client.post('/turmas', json={
        "id": 102,
        "nome": "Turma B",
        "professor_id": 2
    })
    response = client.get('/turmas/102')
    assert response.status_code == 200
    assert response.get_json()["nome"] == "Turma B"

def test_atualizar_turma(client):
    client.post('/turmas', json={
        "id": 103,
        "nome": "Turma C",
        "professor_id": 3
    })
    response = client.put('/turmas/103', json={
        "nome": "Turma C - Atualizada"
    })
    assert response.status_code == 200
    assert response.get_json()["data"]["nome"] == "Turma C - Atualizada"

def test_deletar_turma(client):
    client.post('/turmas', json={
        "id": 104,
        "nome": "Turma D",
        "professor_id": 4
    })
    response = client.delete('/turmas/104')
    assert response.status_code == 200
    assert response.get_json()["msg"] == "Turma removida"
