from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_post_imc_retorna_200_e_classificacao():
    resposta = client.post("/api/imc", json={"peso": 70, "altura": 1.75})
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["imc"] == 22.86
    assert corpo["classificacao"] == "Peso normal"


def test_post_imc_altura_invalida_retorna_400():
    resposta = client.post("/api/imc", json={"peso": 70, "altura": 0})
    assert resposta.status_code == 400
    assert "erro" in resposta.json()


def test_post_imc_corpo_invalido_retorna_422():
    resposta = client.post("/api/imc", json={"peso": "abc"})
    assert resposta.status_code == 422


def test_docs_disponivel():
    assert client.get("/docs").status_code == 200
