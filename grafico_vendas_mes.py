from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

CSV_PATH = Path(__file__).parent / "base_vendas_willian_de_sousa_ribeiro.csv"
OUT_PATH = Path(__file__).parent / "grafico_vendas_mes.png"

df = pd.read_csv(CSV_PATH)
df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
df = df.dropna(subset=["data_venda"])
df["mes_ref"] = df["data_venda"].dt.to_period("M").dt.to_timestamp()

vendas_mes = df.groupby("mes_ref")["valor_total"].sum().sort_index()
rotulos = vendas_mes.index.strftime("%b/%Y")

fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor("#0f1419")
ax.set_facecolor("#1a2332")

barras = ax.bar(rotulos, vendas_mes.values, color="#3d9cf5", edgecolor="#1a2332")

ax.set_title("Evolução das vendas por mês", color="#e8eef6", fontsize=14, weight="bold", pad=14)
ax.set_xlabel("Mês de referência", color="#8b9cb3")
ax.set_ylabel("Soma de valor_total (R$)", color="#8b9cb3")
ax.tick_params(colors="#8b9cb3")
ax.yaxis.set_major_formatter(mtick.FuncFormatter(
    lambda x, _: f"R$ {x/1_000_000:.1f}M" if x >= 1_000_000 else f"R$ {x/1_000:.0f}k"
))
ax.grid(axis="y", color="#2d3a4f", linestyle="--", alpha=0.6)
for spine in ax.spines.values():
    spine.set_color("#2d3a4f")
plt.xticks(rotation=45, ha="right")

for barra, valor in zip(barras, vendas_mes.values):
    ax.text(barra.get_x() + barra.get_width() / 2, valor,
            f"{valor/1_000_000:.1f}M", ha="center", va="bottom",
            color="#e8eef6", fontsize=8)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=120, facecolor=fig.get_facecolor())
print(f"Período: {vendas_mes.index.min():%Y-%m} a {vendas_mes.index.max():%Y-%m}")
print(f"Meses agregados: {len(vendas_mes)}")
print(f"Gráfico salvo em: {OUT_PATH}")
