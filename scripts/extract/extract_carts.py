import requests
import json

url = "https://dummyjson.com/carts"

response = requests.get(url)
dados = response.json()

with open("data/raw/carts.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Carts extraidos com sucesso!")