#!/bin/sh
# Testes de aceitação do endpoint POST /api/imc contra um ambiente em execução.
set -e
BASE="${1:-http://localhost:8000}"
sh "$(dirname "$0")/smoke_test.sh" "$BASE"

code=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE/api/imc" \
  -H "Content-Type: application/json" -d '{"peso": 70, "altura": 0}')
[ "$code" = "400" ] && echo "OK altura inválida -> 400"

code=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$BASE/api/imc" \
  -H "Content-Type: application/json" -d '{"peso": "abc"}')
[ "$code" = "422" ] && echo "OK corpo inválido -> 422"

echo "Aceitação concluída"
