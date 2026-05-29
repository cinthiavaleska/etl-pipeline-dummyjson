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
# TABELAS DA CAMADA GOLD
# =========================================================

tabelas = [
    "fact_cart_items",
    "dim_products",
    "dim_users",
    "dim_address"
]


# =========================================================
# LOOP DE CARGA
# =========================================================

for tabela in tabelas:

    caminho_arquivo = f"data/gold/{tabela}.csv"

    print(f"Carregando tabela: {tabela}")

    df = pd.read_csv(caminho_arquivo)

    df.to_sql(
        name=tabela,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Tabela {tabela} carregada com sucesso!\n")