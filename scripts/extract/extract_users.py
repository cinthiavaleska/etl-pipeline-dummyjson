import requests
import json

url = "https://dummyjson.com/users"

response = requests.get(url)

dados = response.json()

with open("data/raw/users.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Usuarios extraidos com sucesso!")