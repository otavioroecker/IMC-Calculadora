from app.models import ImcRequest, ImcResponse


class ImcService:
    def calcular(self, request: ImcRequest) -> ImcResponse:
        if request.peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")

        if request.altura <= 0:
            raise ValueError("A altura deve ser maior que zero.")

        if request.altura > 3:
            raise ValueError(
                "Altura deve ser informada em metros (ex.: 1.90), não em centímetros."
            )

        imc = request.peso / (request.altura**2)

        return ImcResponse(
            peso=request.peso,
            altura=request.altura,
            imc=round(imc, 2),
            classificacao=self._classificar(imc),
        )

    @staticmethod
    def _classificar(imc: float) -> str:
        if imc < 18.5:
            return "Abaixo do peso"
        if imc < 25:
            return "Peso normal"
        if imc < 30:
            return "Sobrepeso"
        if imc < 35:
            return "Obesidade Grau I"
        if imc < 40:
            return "Obesidade Grau II"
        return "Obesidade Grau III"
