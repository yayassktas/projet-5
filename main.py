import requests

product_list = ['']
allergenss = ['']
brandss = ['Nesquik']
stores = ['']
search_terms = ['nesquik']

def loadp():
	for i in range(0,4):   # va liste 2 pages
		payload = {'action': 'process', # dictionnaire va rapatrier tout les criteres indiques		
		'countries': 'France', # cherche uniquement pour la france fonctione
		'page_size': '1000', 
		#'stores' : stores[i], # cherche sur les stores ayant comme nom carrefour
		#'brands': brandss[i],
		#'additives' : 'e319',	
		'search_terms2' : 'nesquik', # cherche sur le mot soda
		#'allergens' : '', # cherche les allergens exemple gluten
		'additives' : 'E319',
		'json': 1
		} 
		reponse = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
		# fait la recherche sur l url indique avec les parametres indique dans le dico
		data = reponse.json() 
		print(data)


loadp()

#categories_tags