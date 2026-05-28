# %%
import pandas as pd


# =========================================================
# EXTRAÇÃO DOS DADOS - SILVER
# =========================================================

# Carregando dados tratados da camada silver
df_cart_items = pd.read_csv(
    "data/silver/cart_items_clean.csv"
)


# =========================================================
# MODELAGEM FATO - GOLD
# =========================================================

# Selecionando chaves e métricas
colunas = [
    "cart_id",
    "product_id",
    "user_id",
    "quantity",
    "price",
    "discounted_total"
]

df_fact = df_cart_items[colunas]

# =========================================================
# VALIDAÇÃO DOS DADOS
# ========================================================= 

# Verificando se há valores nulos
print(df_fact.isnull().sum())
# Verificando metricas negativas
print(df_fact[df_fact["quantity"] < 0])
print(df_fact[df_fact["price"] < 0])
print(df_fact[df_fact["discounted_total"] < 0])

# =========================================================
# SALVANDO TABELA FATO - GOLD
# =========================================================

df_fact.to_csv(
    "data/gold/fact_cart_items.csv",
    index=False
)