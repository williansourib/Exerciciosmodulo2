# Ex. 3 — Gráfico de mapa (calor ou balão)

Mapa geográfico do Brasil mostrando a distribuição das vendas por estado, usando a base `base_vendas_geral.csv`.

## Escolha: Mapa de balão (Bubble map)

Justificativa: com apenas 6 UFs na base (MG, PR, RJ, RS, SC, SP), o mapa de balão dá leitura imediata de **localização + magnitude** (tamanho do balão proporcional ao valor), enquanto o de calor exigiria gradação contínua e ficaria visualmente similar a um simples preenchimento de polígono.

## Configuração no Looker Studio

| Parâmetro | Valor |
| --- | --- |
| Tipo de gráfico | **Mapa de bolhas** (Google Maps → Bubble map) |
| Campo de localização | `estado` (tipo: Região → Brasil — Estado/UF) |
| Métrica (tamanho do balão) | `SUM(valor_total)` |
| Métrica de cor (opcional) | `SUM(quantidade)` ou `AVG(valor_unitario)` |
| Zoom inicial | Centralizado no Brasil (zoom ≈ 4) |
| Cor das bolhas | Gradiente azul (#3d9cf5 → #0b3d6e) |
| Tooltip | estado · total vendas (R$) · qtd vendas |

## Passo a passo no Looker Studio

1. Inserir → **Mapa de bolhas do Google Maps**.
2. Em **Localização**, definir o campo `estado` como tipo geográfico **País subdivisão (nv. 1)** → Brasil.
3. Em **Tamanho**, escolher `valor_total` (agregação: Soma).
4. Em **Cor**, opcionalmente adicionar `quantidade` (Soma).
5. Estilo → fonte do mapa: Light (cinza claro) para destacar as bolhas.
6. Garantir que os controles do Ex. 2 (período, estado, cidade, categoria, responsável) afetam o mapa.

## Alternativa: Mapa de calor (Heatmap)

Caso prefira o heatmap:

- Tipo: **Heatmap do Google Maps**
- Peso: `SUM(valor_total)`
- Raio: 30
- Opacidade: 0.7

Funciona melhor com pontos por **cidade** (não por UF) — usar `cidade` como localização (tipo: Cidade) para ver concentrações urbanas.
