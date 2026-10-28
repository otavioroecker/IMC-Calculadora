# ADR 0001 — GitHub Flow, proteção da main e Environments

**Status:** aceita (28/10/2026)

**Contexto:** projeto acadêmico com 2 pessoas (autor + revisor par), sem orçamento de infraestrutura.

**Decisão:** GitHub Flow com `main` protegida (PR obrigatório, 1 aprovação, check
"Qualidade e testes", regra válida também para administradores). Promoção via *Environments*
`staging` (automático) e `production` (revisor obrigatório). Deploy simulado por container
no runner; Terraform dispensado.

**Consequências:** todo registro de mudança fica no PR/Actions; para hospedagem real basta
trocar os passos de deploy do `cd.yml`.
