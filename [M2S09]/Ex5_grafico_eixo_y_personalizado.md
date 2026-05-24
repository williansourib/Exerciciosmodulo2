# Ex. 5 — Gráfico de linhas/barras com eixo Y personalizado

Gráfico de evolução das vendas com escala do eixo Y definida manualmente, sobre `base_vendas_geral.csv`.

## Escolha: Gráfico de linhas

Tipo: **Série temporal (Time series)** — linhas mostrando `SUM(valor_total)` por mês.

| Parâmetro | Valor |
| --- | --- |
| Tipo | Série temporal — linha suavizada |
| Dimensão de tempo | `data_venda` (granularidade: Mês) |
| Métrica | `SUM(valor_total)` |
| Divisão (opcional) | `categoria` (2 linhas: Eletrônicos / Acessórios) |

## Eixo Y personalizado

Na guia **Estilo** do gráfico:

| Configuração | Valor |
| --- | --- |
| Eixo Y esquerdo → **Escala automática** | **Desativada** |
| Mínimo (Min) | `0` |
| Máximo (Max) | `700000000` (R$ 700 mi — folga sobre o pico mensal) |
| Eixo Y → Mostrar título | Ativado — "Vendas (R$)" |
| Formato dos números | Compacto (`R$ 500M`, `R$ 700M`) ou Moeda completa |
| Linhas de grade | Ativadas (cor #2d3a4f, suaves) |
| Eixo Y direito | Desativado |

## Por que fixar a escala manualmente

- **Comparabilidade entre filtros**: ao mudar período/estado, a escala não "respira" e o leitor vê o impacto real do filtro.
- **Evita distorção visual**: escala automática pode exagerar pequenas variações quando o range é pequeno.
- **Ancoragem no zero**: começar em 0 evita o viés de "linha que parece despencar".

## Passo a passo

1. Inserir → **Série temporal** → linha.
2. Dados: dimensão `data_venda` (Mês), métrica `valor_total` (Soma).
3. Aba **Estilo** → seção *Eixo Y esquerdo*:
   - Desmarcar **Escala automática**.
   - Min = `0`, Max = `700000000`.
   - Marcar **Mostrar título do eixo** → digitar `Vendas (R$)`.
4. Em **Formato do número**: Moeda → BRL, compactar para milhões.
5. Aplicar os controles do Ex. 2 ao gráfico.

## Alternativa em barras

Caso prefira barras (mesma personalização):

- Tipo: **Gráfico de colunas**
- Dimensão: `data_venda` (Mês)
- Métrica: `SUM(valor_total)`
- Estilo do eixo Y: idêntico à configuração acima (Min 0, Max 700M, título fixo).
