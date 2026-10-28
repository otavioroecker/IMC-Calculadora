#!/bin/sh
# Smoke test pós-deploy: /docs responde e uma chamada de exemplo a /api/imc funciona.
set -e
BASE="${1:-http://localhost:8000}"

echo "Aguardando a API em $BASE ..."
for i in $(seq 1 30); do
  if curl -fs "$BASE/docs" > /dev/null; then break; fi
  sleep 1
  [ "$i" = "30" ] && { echo "API não subiu"; exit 1; }
done

curl -fs "$BASE/docs" > /dev/null && echo "OK /docs"
RESP=$(curl -fs -X POST "$BASE/api/imc" -H "Content-Type: application/json" \
  -d '{"peso": 70, "altura": 1.75}')
echo "$RESP"
echo "$RESP" | grep -q '"classificacao":"Peso normal"' && echo "OK /api/imc"
