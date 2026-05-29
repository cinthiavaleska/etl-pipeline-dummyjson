import pandas as pd
import json


# =========================================================
# EXTRAÇÃO
# =========================================================

# Abre o arquivo JSON bruto vindo da API
with open("data/raw/users.json", "r") as arquivo:
    dados = json.load(arquivo)

# Cria DataFrame principal de usuários
df_users = pd.DataFrame(dados["users"])


# =========================================================
# NORMALIZAÇÃO DA TABELA ADDRESS
# =========================================================

# A coluna "address" possui dicionários aninhados.
# Aqui transformamos esses dicionários em uma tabela separada.
df_address = pd.DataFrame(df_users["address"].tolist())

# Criando chave primária da tabela address
df_address["address_id"] = df_address.index + 1

# Adicionando chave estrangeira na tabela users
df_users["address_id"] = df_address["address_id"]

# Removendo coluna nested original
df_users = df_users.drop(columns=["address"])


# =========================================================
# TRANSFORMAÇÃO - USERS
# =========================================================

# Selecionando apenas colunas importantes
colunas_users = [
    "id",
    "firstName",
    "lastName",
    "age",
    "gender",
    "email",
    "phone",
    "address_id"
]

df_users = df_users[colunas_users]

# Renomeando colunas para padrão snake_case
df_users = df_users.rename(columns={
    "id": "user_id",
    "firstName": "first_name",
    "lastName": "last_name"
})

# Selecionando colunas texto automaticamente
colunas_texto_users = df_users.select_dtypes(include="object").columns

# Padronizando texto:
# - minúsculo
# - removendo espaços extras
for coluna in colunas_texto_users:
    df_users[coluna] = (
        df_users[coluna]
        .str.lower()
        .str.strip()
    )

# Padronizando telefone:
# remove tudo que não for número
df_users["phone"] = df_users["phone"].str.replace(
    r"\D",
    "",
    regex=True
)

# Salvando camada silver users
df_users.to_csv(
    "data/silver/users_clean.csv",
    index=False
)


# =========================================================
# TRANSFORMAÇÃO - ADDRESS
# =========================================================

# Selecionando colunas relevantes
colunas_address = [
    "address_id",
    "city",
    "state",
    "country"
]

df_address = df_address[colunas_address]

# Selecionando colunas texto
colunas_texto_address = (
    df_address
    .select_dtypes(include="object")
    .columns
)

# Padronizando textos
for coluna in colunas_texto_address:
    df_address[coluna] = (
        df_address[coluna]
        .str.lower()
        .str.strip()
    )

# Salvando camada silver address
df_address.to_csv(
    "data/silver/address_clean.csv",
    index=False
)


# =========================================================
# FINALIZAÇÃO
# =========================================================

print("Transformação concluída com sucesso!")
print(df_users.head())
print(df_address.head())