# Evidências de conformidade (atividade GCS)

Salve aqui os arquivos abaixo (prints ou logs). Nomes sugeridos:

| Item avaliado | Arquivo | Como obter |
|---|---|---|
| Push direto recusado na main | `01-push-recusado.png` / `.txt` | `git checkout main && git commit --allow-empty -m "teste" && git push origin main` — deve exibir `GH006: Protected branch update failed` (ou `GH013`). Salve o terminal. |
| Regras da main | `02-protecao-main.png` | Settings → Branches → regra da `main` |
| Revisor par com escrita | `03-colaborador-write.png` | Settings → Collaborators (papel **Write**, convite aceito) |
| PR revisado/aprovado | `04-pr-aprovado.png` | PR com 1 approval do colega + check "Qualidade e testes" verde |
| Environments | `05-environments.png` | Settings → Environments (staging e production) |
| Revisor obrigatório | `06-production-revisor.png` | Environment production → *Required reviewers* = você |
| Gate em ação | `07-deploy-aguardando-aprovacao.png` | Actions → run do CD aguardando "Review deployments" |
