# %%
import pandas as pd


# =========================================================
# EXTRAÇÃO DOS DADOS - SILVER
# =========================================================

# Carregando dados tratados da camada silver
df_products = pd.read_csv(
    "data/silver/products_clean.csv"
)

# =========================================================
# TRANSFORMAÇÃO DOS DADOS - GOLD
# =========================================================

# Selecionando apenas as colunas relevantes para a camada gold

colunas = [
    "id",
    "title",
    "category",
    "brand",
    "price",
    "rating"
]
df_products = df_products[colunas]
# Renomeando colunas para padronização
df_products = df_products.rename(columns={
    "id": "product_id",
    "title": "product_title",
    "category": "product_category"
})

# =========================================================
# VALIDAÇÃO DOS DADOS
# =========================================================

#verificar se há valores nulos
print(df_products.isnull().sum())

#verificar se há valores duplicados
print(df_products["product_id"].duplicated().sum())

# =========================================================
# SALVANDO DIMENSÃO GOLD
# =========================================================

df_products.to_csv(
    "data/gold/dim_products.csv",
    index=False
)