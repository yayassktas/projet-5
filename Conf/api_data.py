"""file allowing to reconcile the API data"""
import requests
from .constantes import CATEGORY_LIST, PAGE_SIZE


class ApOpen:
    """creation of the class allowing the import of openfood data"""
    def __init__(self):
        pass

    def get_products_list(self):
        """method for retrieving data from the openfood API"""
        products_list = []

        for category in CATEGORY_LIST:

            payload = {'action': 'process',
                       'countries': 'France',
                       'page_size': PAGE_SIZE,
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
        """method for formatting the request on openfood"""
        for key in words:
            if key not in products_cat or not products_cat[key]:
                return False
        return True


    def resultdata(self, products_list):
        """method for formatting data"""
        result = []
        words = ['product_name_fr', 'nutrition_grade_fr',
                 'url', 'categories', 'main_category', 'stores']
        # print(len(products_list))  # combiens elements dans liste
        for product in products_list:
            if self.result_the_data(words, product):
                url_product = product['url']
                for url in url_product:
                    if url == product['url']:
                        return True

                product_name = product['product_name_fr'].replace('\'', ' ')
                description = product['categories'].replace('\'', ' ')
                nutri_score = product['nutrition_grade_fr']
                main_category = product['main_category'].lower()
                store = product['stores'].replace('\'', ' ')
                key = (product_name, description, store, nutri_score, url_product, main_category)
                # if self.check_duplicate(result):
                result.append(key)

        return result

    def check_duplicate(self, product_id, keys):
        """method for formatting data for insertion into the db"""
        for key in keys:
            if key[0] == product_id:
                return False
        return True


if __name__ == "__main__":
    main()
