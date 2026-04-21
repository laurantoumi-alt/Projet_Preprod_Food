import requests
import csv

BASE_URL = "https://world.openfoodfacts.org/cgi/search.pl"
FAT_THRESHOLD = 20.0


class Food:
    """ class food """
    __name = None
    __calories = None
    __fat = None
    __carbs = None
    __proteins = None

    def get_name(self):
        """ function : get the food name """
        return self.__name

    def set_name(self, name):
        """ function : set the food name """
        self.__name = name

    def get_calories(self):
        """ function : get the property named calories of the food """
        return self.__calories

    def set_calories(self, calories):
        """ function : set the property named calories of the food """
        self.__calories = calories

    def get_fat(self):
        """ function : get the property named fat of the food """
        return self.__fat

    def set_fat(self, fat):
        """ function : set the property named fat of the food """
        self.__fat = fat

    def get_carbs(self):
        """ function : get the property named carbs of the food """
        return self.__carbs

    def set_carbs(self, carbs):
        """ function : set the property named carbs of the food """
        self.__carbs = carbs

    def get_proteins(self):
        """ function : get the property named proteins of the food """
        return self.__proteins

    def set_proteins(self, proteins):
        """ function : set the property named proteins of the food """
        self.__proteins = proteins

    def retrieve_food_infos(self, food_name):
        """ function : scrap the properties of the food from a website given its name """
        params = {
            "search_terms": food_name,
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "page_size": 1,
            "fields": "product_name,nutriments"
        }

        response = requests.get(BASE_URL, params=params)

        if not response.ok:
            raise ConnectionError(
                f"Request failed with status code {response.status_code}"
            )

        data = response.json()
        products = data.get("products", [])

        if not products:
            raise ValueError(f"No product found for '{food_name}'")

        product = products[0]
        nutriments = product.get("nutriments", {})

        self.set_name(food_name)
        self.set_calories(nutriments.get("energy-kcal_100g", 0.0))
        self.set_fat(nutriments.get("fat_100g", 0.0))
        self.set_carbs(nutriments.get("carbohydrates_100g", 0.0))
        self.set_proteins(nutriments.get("proteins_100g", 0.0))

    def display_food_infos(self):
        """ function : display the properties of the food """
        separator = "-" * 48
        print(separator)
        print(f"{'name':<12}{'calories':<12}{'fat':<8}{'carbs':<8}{'proteins':<8}")
        print(
            f"{self.__name:<12}"
            f"{self.__calories:<12}"
            f"{self.__fat:<8}"
            f"{self.__carbs:<8}"
            f"{self.__proteins:<8}"
        )
        print(separator)

    def save_to_csv_file(self, file_name):
        """ function : save the properties of the food in a csv file """
        with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
