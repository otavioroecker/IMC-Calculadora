from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models import ImcRequest
from app.services import ImcService

router = APIRouter(prefix="/api/imc", tags=["Imc"])
imc_service = ImcService()


@router.post("")
def calcular(request: ImcRequest):
    """Calcula o IMC a partir do peso (kg) e altura (m) informados."""
    try:
        resultado = imc_service.calcular(request)
        return resultado
    except ValueError as ex:
        return JSONResponse(status_code=400, content={"erro": str(ex)})
