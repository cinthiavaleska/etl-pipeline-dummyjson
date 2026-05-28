# %%
import pandas as pd
import json


# =========================================================
# EXTRAÇÃO DOS DADOS
# =========================================================

# Abrindo arquivo products.json
with open("data/raw/products.json", "r") as arquivo:
    dados = json.load(arquivo)


# Transformando lista de produtos em DataFrame
df = pd.DataFrame(dados["products"])


# =========================================================
# TRANSFORMAÇÃO DOS DADOS
# =========================================================

# Selecionando apenas colunas relevantes
colunas = [
    "id",
    "title",
    "category",
    "price",
    "stock",
    "brand",
    "rating"
]

df = df[colunas]


# Preenchendo marcas nulas
df["brand"] = df["brand"].fillna(
    "sem marca"
)


# Padronizando colunas de texto
# removendo espaços e deixando minúsculo
colunas_texto = df.select_dtypes(
    include="object"
).columns

for coluna in colunas_texto:
    df[coluna] = (
        df[coluna]
        .str.lower()
        .str.strip()
    )


# =========================================================
# VALIDAÇÃO DOS DADOS
# =========================================================

# Verificando estrutura do DataFrame
print(df.info())


# Verificando valores nulos
print(df.isnull().sum())


# Verificando marcas ainda nulas
print(df[df["brand"].isnull()])


# Verificando linhas duplicadas
print(df.duplicated().sum())

# =========================================================
# SALVANDO ARQUIVO TRATADO
# =========================================================

df.to_csv(
    "data/silver/products_clean.csv",
    index=False
)