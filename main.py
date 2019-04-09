import requests

product_list = ['Snacks','Alcool']
def loadp():
	for i in range(0,2):
		payload = {'action': 'process',
		'tagtype_0': 'categories',
		'tag_contains_0': 'contains',
		'tag_0': product_list[i],
		'countries': 'France',
		'page_size': '1000',
		'json': 1
		} 
		reponse = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', \
		params=payload)
		data = reponse.json() 
		print(reponse.json())


loadp()

