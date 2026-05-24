import locale
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import streamlit as st

CSV_PATH = Path(__file__).parent / "base_vendas_willian_de_sousa_ribeiro.csv"


def formatar_brl(valor: float) -> str:
    for loc in ("pt_BR.UTF-8", "pt_BR.utf8", "Portuguese_Brazil.1252"):
        try:
            locale.setlocale(locale.LC_ALL, loc)
            return locale.currency(valor, grouping=True, symbol=True)
        except locale.Error:
            continue
    inteiro, _, decimal = f"{valor:,.2f}".partition(".")
    return f"R$ {inteiro.replace(',', '.')},{decimal}"


@st.cache_data
def carregar_dados() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH)
    df["data_venda"] = pd.to_datetime(df["data_venda"], errors="coerce")
    df = df.dropna(subset=["data_venda"])
    df["mes_ref"] = df["data_venda"].dt.to_period("M").dt.to_timestamp()
    return df


st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("Relatório de vendas")
st.caption("Scorecard + evolução mensal com dois filtros (base e controle)")

df = carregar_dados()

st.sidebar.header("Filtros")

st.sidebar.subheader("Filtro na base de dados")
st.sidebar.caption("Restringe o conjunto que entra nas agregações (como se a consulta já viesse filtrada).")
categorias = ["Todas"] + sorted(df["categoria"].dropna().unique().tolist())
categoria_sel = st.sidebar.selectbox("Categoria", categorias)

df_base = df if categoria_sel == "Todas" else df[df["categoria"] == categoria_sel]

st.sidebar.subheader("Filtro de controle do relatório")
st.sidebar.caption("Refina a visualização sobre o conjunto já filtrado pela base.")
estados = ["Todos"] + sorted(df_base["estado"].dropna().unique().tolist())
estado_sel = st.sidebar.selectbox("Estado (UF)", estados)

df_view = df_base if estado_sel == "Todos" else df_base[df_base["estado"] == estado_sel]

total = float(df_view["valor_total"].sum())
qtd = len(df_view)

col1, col2, col3 = st.columns(3)
col1.metric("Total de vendas", formatar_brl(total))
col2.metric("Linhas filtradas", f"{qtd}")
col3.metric("Filtros ativos", f"{categoria_sel} / {estado_sel}")

st.subheader("Evolução das vendas por mês")

if df_view.empty:
    st.warning("Nenhum dado para os filtros selecionados.")
else:
    vendas_mes = df_view.groupby("mes_ref")["valor_total"].sum().sort_index()
    rotulos = vendas_mes.index.strftime("%b/%Y")

    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor("#0f1419")
    ax.set_facecolor("#1a2332")
    ax.bar(rotulos, vendas_mes.values, color="#3d9cf5", edgecolor="#1a2332")
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
    plt.tight_layout()
    st.pyplot(fig)
