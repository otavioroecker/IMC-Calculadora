from pydantic import BaseModel


class ImcRequest(BaseModel):
    """Dados enviados pelo usuário para o cálculo do IMC."""

    peso: float  # Peso em quilogramas (kg)
    altura: float  # Altura em metros (m). Ex.: 1.75


class ImcResponse(BaseModel):
    """Resultado do cálculo de IMC devolvido ao usuário."""

    peso: float
    altura: float
    imc: float
    classificacao: str
