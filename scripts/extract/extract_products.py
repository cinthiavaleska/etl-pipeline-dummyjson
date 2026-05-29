import requests
import json

url = "https://dummyjson.com/products"

response = requests.get(url)

dados = response.json()

with open("data/raw/products.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Dados salvos com sucesso!")
