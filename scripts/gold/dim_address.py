# %%
import pandas as pd


# =========================================================
# EXTRAÇÃO DOS DADOS - SILVER
# =========================================================

# Carregando dados tratados da camada silver
df_address = pd.read_csv(
    "data/silver/address_clean.csv"
)


# =========================================================
# MODELAGEM DIMENSIONAL - GOLD
# =========================================================

# Selecionando colunas relevantes
colunas = [
    "address_id",
    "city",
    "state",
    "country"
]

df_address = df_address[colunas]


# =========================================================
# VALIDAÇÃO DOS DADOS
# =========================================================

# Verificando valores nulos
print(df_address.isnull().sum())

# Verificando duplicidade da chave
print(
    df_address["address_id"]
    .duplicated()
    .sum()
)


# =========================================================
# SALVANDO DIMENSÃO GOLD
# =========================================================

df_address.to_csv(
    "data/gold/dim_address.csv",
    index=False
)