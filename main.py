import requests

r = requests.get("https://fr.openfoodfacts.org/api/v0/produit/3029330003533.json")
print(r.text)
