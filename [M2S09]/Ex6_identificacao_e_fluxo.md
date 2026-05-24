# Ex. 6 — Identificação e fluxo do relatório

Padronização de nomes, títulos e organização visual do relatório no Looker Studio para que ele seja lido de forma fluida e conectada.

## Identificação do relatório

| Elemento | Texto |
| --- | --- |
| Nome do arquivo (Looker) | `M2S09 — Relatório de Vendas` |
| Título no cabeçalho | `Relatório de Vendas — 2025/2026` |
| Subtítulo | `Base: base_vendas_geral.csv · 510.000 vendas · 6 UFs` |
| Rodapé | `Autor: Willian de Sousa Ribeiro · DevInHouse 2026 · Módulo 2 — Semana 9` |

## Títulos dos gráficos

| Gráfico | Título exibido |
| --- | --- |
| Scorecard 1 | Total de vendas (R$) |
| Scorecard 2 | Quantidade de vendas |
| Scorecard 3 | Ticket médio |
| Mapa de balão | Vendas por estado |
| Série temporal | Evolução mensal das vendas |
| Tabela | Top 10 produtos por faturamento |

## Renomear campos no Looker Studio

Na fonte de dados, abrir cada campo e ajustar o **Nome** (não o ID):

| Campo original | Nome amigável |
| --- | --- |
| `data_venda` | Data da venda |
| `valor_total` | Valor total (R$) |
| `valor_unitario` | Valor unitário (R$) |
| `quantidade` | Quantidade |
| `id_venda` | ID da venda |
| `estado` | Estado (UF) |
| `cidade` | Cidade |
| `cliente` | Cliente |
| `produto` | Produto |
| `categoria` | Categoria |
| `responsavel` | Responsável |
| `ticket_medio` (calc.) | Ticket médio |

## Padrões visuais (consistência)

- **Fonte:** Roboto / DM Sans em todo o relatório.
- **Paleta:** azul `#3d9cf5` (principal), verde `#34d399` (variações positivas), cinza `#8b9cb3` (texto secundário), fundo `#0f1419`.
- **Tamanhos:** título da página 22pt · títulos de gráficos 14pt · texto base 11pt.
- **Espaçamento:** grade de 8px; respiro mínimo de 24px nas bordas.
- **Bordas:** cantos arredondados 12px em cards e gráficos.

## Fluxo de leitura (de cima para baixo, esquerda para direita)

1. **Cabeçalho** → identifica o relatório.
2. **Sidebar esquerda (filtros)** → o leitor define o recorte primeiro.
3. **Scorecards (linha superior)** → resposta imediata ao "quanto?".
4. **Série temporal** → resposta ao "quando?" (evolução).
5. **Mapa** → resposta ao "onde?".
6. **Tabela top produtos** → resposta ao "o quê?".

Essa ordem segue a leitura natural (Z-pattern) e cria uma narrativa: filtra → resume → desdobra no tempo → desdobra no espaço → detalha por produto.

## Conexão entre os elementos

- Todos os gráficos compartilham **os mesmos controles** do Ex. 2 (escopo de página).
- Habilitar **filtragem cruzada** (Recurso → Filtragem cruzada) para que clicar em uma UF do mapa filtre os demais gráficos.
- Manter a **mesma agregação temporal** (mês) entre série temporal e tabelas dependentes.
- Usar a **mesma métrica principal** (`valor_total`) como espinha dorsal — variações (ticket médio, quantidade) entram como complementos.

## Checklist final

- [ ] Todos os gráficos têm título descritivo.
- [ ] Todos os campos foram renomeados para nomes amigáveis.
- [ ] Cabeçalho e rodapé com autor e contexto.
- [ ] Cores e fontes consistentes em toda a página.
- [ ] Filtros aplicam a todos os gráficos da página.
- [ ] Filtragem cruzada ativada.
- [ ] Eixos formatados (R$, separador de milhar, sem decimais desnecessários).
- [ ] Tooltips revisados para clareza.
