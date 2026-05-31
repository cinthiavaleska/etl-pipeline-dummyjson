import pandas as pd

from config.database import engine


# =========================================================
# LEITURA DO ARQUIVO GOLD
# =========================================================

df = pd.read_csv(
    "data/gold/dim_users.csv"
)


# =========================================================
# CARGA NO POSTGRESQL
# =========================================================

df.to_sql(
    name="dim_users",
    con=engine,
    if_exists="replace",
    index=False
)


# =========================================================
# LOG
# =========================================================

print("Tabela dim_users carregada com sucesso!")