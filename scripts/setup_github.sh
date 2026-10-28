#!/usr/bin/env bash
# Configura no GitHub os controles de GCS exigidos pela atividade:
#   - proteção da main (sem push direto, PR + 1 aprovação + CI verde, vale para admin)
#   - revisor par com acesso de escrita
#   - environments "staging" e "production" (production com revisor obrigatório)
#
# Pré-requisitos: GitHub CLI autenticado como DONO do repositório (gh auth login)
# Uso: ./scripts/setup_github.sh <usuario-do-colega-revisor>
set -euo pipefail

REPO="${REPO:-otavioroecker/IMC-Calculadora}"
OWNER_USER="${REPO%%/*}"
REVISOR="${1:?Informe o usuário GitHub do colega revisor. Ex.: ./scripts/setup_github.sh fulano}"

echo "==> 1/4 Convidando $REVISOR com permissão de escrita (push)"
gh api -X PUT "repos/$REPO/collaborators/$REVISOR" -f permission=push --silent
echo "    Convite enviado: o colega precisa ACEITAR em https://github.com/$REPO/invitations"

echo "==> 2/4 Protegendo a branch main"
gh api -X PUT "repos/$REPO/branches/main/protection" --input - <<JSON
{
  "required_status_checks": { "strict": true, "contexts": ["Qualidade e testes"] },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": false
  },
  "restrictions": null,
  "required_linear_history": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "required_conversation_resolution": true
}
JSON

echo "==> 3/4 Criando environment staging"
gh api -X PUT "repos/$REPO/environments/staging" --silent

echo "==> 4/4 Criando environment production (revisor obrigatório: $OWNER_USER)"
OWNER_ID=$(gh api "users/$OWNER_USER" --jq .id)
gh api -X PUT "repos/$REPO/environments/production" --input - <<JSON
{
  "reviewers": [ { "type": "User", "id": $OWNER_ID } ],
  "prevent_self_review": false,
  "deployment_branch_policy": { "protected_branches": true, "custom_branch_policies": false }
}
JSON

echo
echo "Configuração concluída. Confira em:"
echo "  https://github.com/$REPO/settings/branches"
echo "  https://github.com/$REPO/settings/environments"
echo "  https://github.com/$REPO/settings/access"
