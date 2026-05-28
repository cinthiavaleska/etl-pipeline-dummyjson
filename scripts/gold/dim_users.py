# %%
import pandas as pd


# =========================================================
# EXTRAÇÃO DOS DADOS - SILVER
# =========================================================

# Carregando dados tratados da camada silver
df_users = pd.read_csv(
    "data/silver/users_clean.csv"
)

# =========================================================
# TRANSFORMAÇÃO DOS DADOS - GOLD
# =========================================================

#concatenando nome e sobrenome para criar o nome completo do usuário
df_users["full_name"] = (
    df_users["first_name"]
    + " " 
    + df_users["last_name"]
)
def classificar_idade(idade):
    if idade <=25:
        return "18-25"
    elif idade <=35:
        return "26-35"
    elif idade <=45:
        return "36-45"
    else:
        return "46+"
# Criando a coluna faixa_etaria com base na idade
df_users["age_group"] = df_users["age"].apply(classificar_idade)   

# Selecionando apenas as colunas relevantes para a camada gold
colunas = [
    "user_id",
    "full_name",
    "age_group",
    "gender",
    "address_id"
]
df_users = df_users[colunas]

# =========================================================
# VALIDAÇÃO DOS DADOS
# =========================================================

#verificar se há valores nulos
print(df_users.isnull().sum())

#verificar se há valores duplicados
print(
    df_users["user_id"]
    .duplicated()
    .sum()
)

# =========================================================
# SALVANDO DIMENSÃO GOLD
# =========================================================
df_users.to_csv(
    "data/gold/dim_users.csv",
    index=False
)