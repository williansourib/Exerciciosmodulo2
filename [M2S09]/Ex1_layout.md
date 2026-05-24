# Ex. 1 — Layout de uma página dentro do Looker Studio

Referência de organização da página do relatório construído sobre `base_vendas_geral.csv`.

## Estrutura visual

```
┌─────────────────────────────────────────────────────┐
│           Relatório de Vendas — 2025/2026           │  ← Cabeçalho
├──────────────────┬──────────────────────────────────┤
│ Filtros (esq)    │  Scorecards (3 cards no topo)    │
│ - Período        │  Total | Qtd vendas | Ticket méd │
│ - Categoria      ├──────────────────────────────────┤
│ - Estado         │  Gráfico de barras: vendas/mês   │
│ - Responsável    ├──────────────────────────────────┤
│                  │  Mapa BR + Top produtos          │
└──────────────────┴──────────────────────────────────┘
```

## Configurações da página

- **Tamanho:** Custom 1200×900 (ou US Letter)
- **Tema:** Simple Dark ou Constellation
- **Grid:** Snap to grid 8px ligado
- **Margens:** 24px nas bordas

## Componentes

| Área | Componente | Métrica/Dimensão |
| --- | --- | --- |
| Cabeçalho | Retângulo + texto fixo | "Relatório de Vendas — 2025/2026" |
| Filtros (sidebar) | Date range, drop-downs | data_venda, categoria, estado, responsavel |
| Scorecards | 3 cards | SUM(valor_total) · COUNT(id_venda) · AVG(valor_total) |
| Gráfico de barras | Barras verticais | mes_ref × SUM(valor_total) |
| Mapa | Geo chart (Brasil) | estado × SUM(valor_total) |
| Tabela top produtos | Tabela ordenada | produto × SUM(valor_total) — TOP 10 |

## Perfil da base

- Linhas: 510.000
- Período: 2025-03-18 → 2026-03-18
- Categorias: Eletrônicos, Acessórios
- Estados: MG, PR, RJ, RS, SC, SP
- Responsáveis: 51
- Total geral: R$ 7.072.641.970,81
