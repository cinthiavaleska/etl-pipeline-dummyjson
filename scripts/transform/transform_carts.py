# %%
import pandas as pd
import json

with open("data/raw/carts.json", "r") as arquivo:
    dados = json.load(arquivo)

df_carts = pd.DataFrame(dados["carts"])

df_cart_items = df_carts.explode("products")


df_products = pd.DataFrame(
    df_cart_items["products"].tolist()
) 

df_products["cart_id"] = df_cart_items["id"].values

df_products["user_id"] = df_cart_items["userId"].values

df_products = df_products.rename(columns={
    "id": "product_id"
})

# =========================================================
# TRANSFORMAÇÃO - CARTS
# =========================================================

# Selecionando apenas colunas relevantes
colunas = [
    "product_id",
    "price",
    "quantity",
    "discountedTotal",
    "cart_id",
    "user_id"
]
df_products = df_products[colunas]

# Renomeando colunas para padrão snake_case
df_products = df_products.rename(columns={
     "discountedTotal" : "discounted_total" 
})

# tratamento de duplicatas
duplicados = df_products[
    df_products.duplicated(
        subset=["cart_id", "product_id"]
    )
]

print(duplicados)

# verificando produto específico que aparece mais de uma vez no mesmo carrinho

df_products[(df_products["cart_id"] == 7) & (df_products["product_id"] == 56)]

#removendo duplicatas

df_products = df_products.drop_duplicates()

#verificando nulos

print(df_products.isnull().sum())

#salvando arquivos transformados

df_products.to_csv("data/silver/cart_items_clean.csv", index=False)
