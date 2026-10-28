# IMC-Calculadora (Python / FastAPI)

API RESTful de cálculo de Índice de Massa Corporal (IMC), com pipeline CI/CD e
Gerenciamento de Configuração (GCS) com enfoque DevOps.

📄 **Plano de GCS (item de configuração):** [`docs/PGC_GCS_DevOps_IMC-CALC.pdf`](docs/PGC_GCS_DevOps_IMC-CALC.pdf)

## Estrutura do repositório

```
.
├── .github/
│   ├── workflows/ci.yml          # CI: black, flake8, pytest+cov (>=80%), bandit, pip-audit, build Docker
│   ├── workflows/cd.yml          # CD: build -> staging -> production (aprovação) -> tag/release
│   ├── workflows/rollback.yml    # Rollback manual para uma versão anterior
│   ├── dependabot.yml            # Atualização/segurança de dependências
│   ├── CODEOWNERS
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
├── app/                          # main.py, routes.py, services.py, models.py
├── tests/                        # test_imc_service.py (unitários) e test_api.py (API)
├── scripts/                      # smoke_test.sh, acceptance_test.sh, setup_github.sh
├── docs/
│   ├── PGC_GCS_DevOps_IMC-CALC.pdf
│   ├── adr/
│   └── evidencias/               # prints/logs: push recusado, environments, revisor
├── Dockerfile / docker-compose.yml
├── requirements.txt / requirements-dev.txt
└── VERSION                       # MAJOR.MINOR (o PATCH é o nº da execução do CD)
```

## Executar

```bash
pip install -r requirements-dev.txt
uvicorn app.main:app --reload        # http://localhost:8000/docs
pytest -v --cov=app                  # testes
docker compose up --build            # via container
```

`POST /api/imc` com `{"peso": 70, "altura": 1.75}` retorna
`{"peso": 70, "altura": 1.75, "imc": 22.86, "classificacao": "Peso normal"}`.

## Fluxo de contribuição

Issue → branch `feature/<n>-<descricao>` → Pull Request → CI verde + 1 aprovação do
revisor → merge → CD (staging automático → production com aprovação) → tag `vX.Y.Z`.
Push direto na `main` é recusado (ver `docs/evidencias/`).

> Nota: staging e production executam a imagem em container no runner do GitHub Actions
> (ambientes lógicos protegidos por *Environments*). Para hospedagem real, basta trocar o
> passo "Subir a imagem" por um deploy em Render/Fly.io/Cloud Run.
