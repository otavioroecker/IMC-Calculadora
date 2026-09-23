import pytest

from app.models import ImcRequest
from app.services import ImcService

service = ImcService()


@pytest.mark.parametrize(
    "peso,altura,classificacao_esperada",
    [
        (50, 1.70, "Abaixo do peso"),
        (65, 1.70, "Peso normal"),
        (80, 1.70, "Sobrepeso"),
        (95, 1.70, "Obesidade Grau I"),
        (105, 1.70, "Obesidade Grau II"),
        (120, 1.70, "Obesidade Grau III"),
    ],
)
def test_calcular_deve_classificar_corretamente(peso, altura, classificacao_esperada):
    resultado = service.calcular(ImcRequest(peso=peso, altura=altura))
    assert resultado.classificacao == classificacao_esperada


def test_calcular_deve_retornar_imc_correto():
    resultado = service.calcular(ImcRequest(peso=70, altura=1.75))
    assert resultado.imc == pytest.approx(22.86, abs=0.01)


def test_calcular_peso_zero_deve_lancar_excecao():
    with pytest.raises(ValueError):
        service.calcular(ImcRequest(peso=0, altura=1.70))


def test_calcular_peso_negativo_deve_lancar_excecao():
    with pytest.raises(ValueError):
        service.calcular(ImcRequest(peso=-10, altura=1.70))


def test_calcular_altura_zero_deve_lancar_excecao():
    with pytest.raises(ValueError):
        service.calcular(ImcRequest(peso=70, altura=0))


def test_calcular_altura_em_centimetros_deve_lancar_excecao():
    # Erro comum: usuário digita 190 (cm) em vez de 1.90 (m)
    with pytest.raises(ValueError):
        service.calcular(ImcRequest(peso=100, altura=190))
