# ImcCalculadora (Python)


## Estrutura

```
imc-calculadora-python/
├── .github/
│   └── workflows/
│       └── ci-cd-simples.yml
├── app/
│   ├── main.py       # Ponto de entrada (equivalente a Program.cs)
│   ├── routes.py      # Rotas (equivalente a ImcController.cs)
│   ├── services.py    # Lógica de cálculo (equivalente a ImcService.cs)
│   └── models.py      # Modelos Pydantic (equivalente a ImcRequest/ImcResponse)
├── tests/
│   └── test_imc_service.py  # Testes (equivalente a ImcServiceTests.cs)
└── requirements.txt
