import locale
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

CSV_PATH = Path(__file__).parent / "base_vendas_willian_de_sousa_ribeiro.csv"
OUT_PATH = Path(__file__).parent / "scorecard_vendas.png"


def formatar_brl(valor: float) -> str:
    for loc in ("pt_BR.UTF-8", "pt_BR.utf8", "Portuguese_Brazil.1252"):
        try:
            locale.setlocale(locale.LC_ALL, loc)
            return locale.currency(valor, grouping=True, symbol=True)
        except locale.Error:
            continue
    inteiro, _, decimal = f"{valor:,.2f}".partition(".")
    inteiro = inteiro.replace(",", ".")
    return f"R$ {inteiro},{decimal}"


df = pd.read_csv(CSV_PATH)
total = df["valor_total"].sum()
qtd_vendas = len(df)
total_fmt = formatar_brl(total)

fig, ax = plt.subplots(figsize=(8, 4.5))
fig.patch.set_facecolor("#0f1419")
ax.set_facecolor("#1a2332")
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_color("#2d3a4f")

ax.text(0.5, 0.78, "TOTAL DE VENDAS", ha="center", va="center",
        fontsize=14, color="#8b9cb3", weight="bold", transform=ax.transAxes)
ax.text(0.5, 0.48, total_fmt, ha="center", va="center",
        fontsize=36, color="#e8eef6", weight="bold", transform=ax.transAxes)
ax.text(0.5, 0.18, f"{qtd_vendas} vendas registradas",
        ha="center", va="center", fontsize=12, color="#34d399",
        transform=ax.transAxes)

plt.tight_layout()
plt.savefig(OUT_PATH, dpi=120, facecolor=fig.get_facecolor())
print(f"Total de vendas: {total_fmt}")
print(f"Scorecard salvo em: {OUT_PATH}")
