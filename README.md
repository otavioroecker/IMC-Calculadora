# ImcCalculadora (Python)

API de cálculo de IMC, convertida do projeto original em C#/.NET para Python usando **FastAPI**.

## Estrutura

```
imc-calculadora-python/
├── app/
│   ├── main.py       # Ponto de entrada (equivalente a Program.cs)
│   ├── routes.py      # Rotas (equivalente a ImcController.cs)
│   ├── services.py    # Lógica de cálculo (equivalente a ImcService.cs)
│   └── models.py      # Modelos Pydantic (equivalente a ImcRequest/ImcResponse)
├── tests/
│   └── test_imc_service.py  # Testes (equivalente a ImcServiceTests.cs)
└── requirements.txt
```

## Instalação

```bash
pip install -r requirements.txt
```

## Executando a API

```bash
uvicorn app.main:app --reload
```

A documentação interativa (equivalente ao Swagger do .NET) fica disponível em:
`http://localhost:8000/docs`

## Endpoint

`POST /api/imc`

Body:
```json
{
  "peso": 70,
  "altura": 1.75
}
```

Resposta:
```json
{
  "peso": 70,
  "altura": 1.75,
  "imc": 22.86,
  "classificacao": "Peso normal"
}
```

## Rodando os testes

```bash
pytest tests/ -v
```
