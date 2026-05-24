# Ex. 2 — Controles do relatório (mínimo 5)

Controles a inserir na sidebar do relatório no Looker Studio sobre `base_vendas_geral.csv`.

## Lista de controles

| # | Controle | Tipo no Looker Studio | Campo | Observação |
| --- | --- | --- | --- | --- |
| 1 | Período | Controle de período (Date range) | `data_venda` | Padrão: últimos 12 meses |
| 2 | Estado | Lista suspensa (Drop-down) | `estado` | Obrigatório — seleção múltipla |
| 3 | Cidade | Lista suspensa (Drop-down) | `cidade` | Obrigatório — depende do estado |
| 4 | Categoria | Caixas de seleção (Checkbox) | `categoria` | Escolha — 2 opções (Eletrônicos / Acessórios) |
| 5 | Responsável | Lista suspensa com busca | `responsavel` | Escolha — 51 valores, ativar campo de pesquisa |

## Posicionamento

- Todos agrupados na **sidebar esquerda**, alinhados verticalmente.
- Largura uniforme (≈ 200px), espaçamento de 12px entre controles.
- Período no topo, seguido de Estado → Cidade (hierarquia geográfica), depois Categoria e Responsável.

## Configurações importantes

- **Estilo:** mesmo tema (cor de fundo, fonte) para todos os controles.
- **Aplicar a:** todos os gráficos da página (escopo de página, não de relatório, salvo se houver outras páginas).
- **Valor padrão:**
  - Período → últimos 12 meses
  - Demais controles → "Todos" (sem filtro inicial)
- **Cidade depende de Estado:** ativar "Filtrar lista por opções selecionadas" no controle de Cidade para mostrar apenas cidades do estado selecionado.
