# %%
import pandas as pd
from sqlalchemy import create_engine


# =========================================================
# CONEXÃO POSTGRESQL
# =========================================================

usuario = "admin"
senha = "admin"
host = "localhost"
porta = "5432"
banco = "pipeline_db"

engine = create_engine(
    f"postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}"
)


# =========================================================
# LEITURA DA CAMADA GOLD
# =========================================================

df_fact_cart_items = pd.read_csv(
    "data/gold/fact_cart_items.csv"
)


# =========================================================
# LOAD POSTGRESQL
# =========================================================

df_fact_cart_items.to_sql(
    name="fact_cart_items",
    con=engine,
    if_exists="replace",
    index=False
)

print("Tabela fact_cart_items carregada com sucesso!")