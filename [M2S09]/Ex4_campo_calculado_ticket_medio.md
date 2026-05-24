# Ex. 4 — Campo calculado: Ticket médio

Campo calculado para o ticket médio das vendas, criado no Looker Studio sobre `base_vendas_geral.csv`.

## Definição

Ticket médio = valor médio gasto por venda (linha do CSV).

```
Ticket médio = SUM(valor_total) / COUNT(id_venda)
```

## Como criar no Looker Studio

1. Painel direito → **Dados** → clique no ícone de lápis ao lado da fonte de dados (ou Recurso → Gerenciar fontes de dados → Editar).
2. Botão **+ Adicionar campo** (canto superior direito).
3. Preencher:

| Campo | Valor |
| --- | --- |
| Nome | `ticket_medio` |
| ID do campo | `ticket_medio` |
| Fórmula | `SUM(valor_total) / COUNT(id_venda)` |
| Tipo de dados | Numérico → **Moeda (BRL — R$)** |
| Agregação | Automático |

4. **Salvar** → **Concluído**.

## Uso no relatório

- **Scorecard** com `ticket_medio` ao lado dos cards de Total e Quantidade.
- **Tabela por estado/categoria** comparando o ticket médio entre cortes.
- Aplicar formatação: prefixo `R$`, 2 casas decimais, separador de milhar `.`.

## Variações úteis

| Métrica | Fórmula | O que mede |
| --- | --- | --- |
| Ticket médio por venda | `SUM(valor_total) / COUNT(id_venda)` | Valor médio de cada venda |
| Ticket médio por cliente | `SUM(valor_total) / COUNT_DISTINCT(cliente)` | Quanto cada cliente gasta em média no período |
| Preço médio por item | `SUM(valor_total) / SUM(quantidade)` | Preço médio unitário considerando volume |
