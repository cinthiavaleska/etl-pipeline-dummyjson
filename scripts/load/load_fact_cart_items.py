import pandas as pd

from config.database import engine


# =========================================================
# LEITURA DO ARQUIVO GOLD
# =========================================================

df = pd.read_csv(
    "data/gold/fact_cart_items.csv"
)


# =========================================================
# CARGA NO POSTGRESQL
# =========================================================

df.to_sql(
    name="fact_cart_items",
    con=engine,
    if_exists="replace",
    index=False
)


# =========================================================
# LOG
# =========================================================

print("Tabela fact_cart_items carregada com sucesso!")