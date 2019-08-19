import requests


class ApOpen:

    def __init__(self):

        pass

    def get_products_list(self):

        products_list = []

        foods = ["Soda",
                 "Fromages",
                 "Desserts",
                 "Viandes",
                 "Fruits"]

        for category in foods:

            payload = {'action': 'process',  # dictionnaire va rapatrier tout les criteres indiques
                       'countries': 'France',  # cherche uniquement pour la france fonctione
                       'page_size': '150',
                       'tagtype_0': 'categories',
                       'tag_contains_0': 'contains',
                       'tag_0': category,
                       'json': 1
                       }
            url_check = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
            data = url_check.json()
            products_section = data['products']
            for product in products_section:
                product['main_category'] = category
            products_list.extend(products_section)  # join list

        return products_list

    def result_the_data(self, words, products_cat):
        for key in words:
            if key not in products_cat or not products_cat[key]:
                return False
        return True

    def resultdata(self, products_list):

        result = []
        words = ['id', 'product_name_fr', 'nutrition_grade_fr',
                 'url', 'categories', 'main_category', 'stores']
        #print(len(products_list))  # combiens elements dans liste
        for product in products_list:
            if self.result_the_data(words, product):
                product_id = product['id']
                url_product = product['url']
                product_name = product['product_name_fr'].replace('\'', ' ')
                description = product['categories'].replace('\'', ' ')
                nutri_score = product['nutrition_grade_fr']
                main_category = product['main_category'].upper()
                store = product['stores'].replace('\'', ' ')
                key = (product_id, product_name, description, store, nutri_score, url_product, main_category)
                if self.check_duplicate(product_id, result):
                    result.append(key)

                # print(' produit: ', name.upper(), '\n',
                #       'dispo', [len(stores)],
                #       'magasin(s): = ', stores, '\n',
                #       'présent', [sub_category], [len(categories)],
                #       'categories: = ', categories, '\n',
                #       '\n' * 2)

        return result

    def check_duplicate(self, product_id, keys):
        for key in keys:
            if key[0] == product_id:
                return False
        return True



 # format result voir exemple 3w school tableau de tupple

# def main():
#     """ Initialize the data collect """
#
#     # Download the response
#     data_api = ApOpen()
#     products_lists = data_api.get_products_list()  # recup toute les donnees
#     data_api.resultdata(products_lists)  # recup les donnees parses



