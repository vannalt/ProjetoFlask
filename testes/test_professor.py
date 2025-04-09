import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_criar_professor(client):
    response = client.post('/professores', json={
        "id": 1,
        "nome": "Professor A",
        "disciplina": "Matemática",
        "idade": 40,
        "observacoes": "Pós-graduado"
    }) 
    assert response.status_code == 201
    assert response.get_json()["msg"] == "Professor criado com sucesso"

def test_listar_professores(client):
    client.post('/professores', json={
        "id": 10,
        "nome": "Professor Teste",
        "disciplina": "Teste",
        "idade": 99,
        "observacoes": "Teste"
    })
    response = client.get('/professores')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    assert any(p["id"] == 10 for p in response.get_json())

def test_buscar_professor_por_id(client):
    client.post('/professores', json={
        "id": 2,
        "nome": "Professor B",
        "disciplina": "Física",
        "idade": 35,
        "observacoes": "Experiência internacional"
    })
    response = client.get('/professores/2')
    assert response.status_code == 200
    assert response.get_json()["nome"] == "Professor B"

def test_atualizar_professor(client):
    client.post('/professores', json={
        "id": 3,
        "nome": "Professor C",
        "disciplina": "Química",
        "idade": 45,
        "observacoes": "Doutor"
    })
    response = client.put('/professores/3', json={
        "nome": "Professor Carlos"
    })
    assert response.status_code == 200
    assert response.get_json()["data"]["nome"] == "Professor Carlos"

def test_deletar_professor(client):
    client.post('/professores', json={
        "id": 4,
        "nome": "Professor D",
        "disciplina": "Biologia",
        "idade": 50,
        "observacoes": "Aposentando"
    })
    response = client.delete('/professores/4')
    assert response.status_code == 200
    assert response.get_json()["msg"] == "Professor removido"
