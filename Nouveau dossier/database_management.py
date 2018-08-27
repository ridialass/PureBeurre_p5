import records
import requests
import config as c
from constants import CAT_UG


class DbManagement:
    """ This class search and manipulate database content"""

    def __init__(self):
        """ init username , password and connect to the database"""
        self.db_username = c.DB_USER
        self.db_password = c.DB_PASS
        self.db_name = c.DB_NAME
        self.db = records.Database('mysql://{}:{}@localhost/{}?charset=utf8mb4'
                                   .format(self.db_username, self.db_password,self.db_name))

    def init_cat_list(self):
        """ get list of categories from categories.txt """
        for cat in c.CATEGORIES_TO_USE.keys():
            CAT_UG.append(cat.strip())

    def get_data(self, category):
        """ get data from openfoodfacts api with paramas """
        pass

    def init_products(self, category):
        """ add one category to product table """
        self.get_data(category)
        self.id_index = CAT_UG.index(category)
        self.id_cat = self.id_index + 1
        for product in self.products:
            try:
                pass
            except KeyError:
                pass

            except UnicodeEncodeError:
                pass

    def init_all_category(self):
        """ add all category to the product table"""
        for element in CAT_UG:
            self.init_products(element)

    def display_list_food(self, category, n=c.LIMIT_BAD_PRODUCTS):
        """ display food list with bad nutriscore """
        self.list_food = []
        self.data_elem = self.db.query(f"""SELECT DISTINCT
                                    product_name, code FROM product
                                    JOIN product_category ON product_category.product_code =
                                    product.code
                                    JOIN category ON product_category.category_id = category.id
                                    WHERE nutrition_grade_fr IN ('c', 'd', 'e')
                                    AND category.name LIKE :catname
                                    ORDER BY RAND() LIMIT :n;""", catname=category, n=n)
        """return unhealthy_result.all(as_dict=True)
                                    for element in self.data_elem:
                                        self.list_food.append(element[0])
                                        return self.list_food
                                unhealthy_result = self.db.query(f""SELECT DISTINCT
                                    product_name, code FROM product
                                    JOIN product_category ON product_category.product_code =
                                    product.code
                                    JOIN category ON product_category.category_id = category.id
                                    WHERE nutrition_grade_fr IN ('c', 'd', 'e')
                                    AND category.name LIKE :catname
                                    ORDER BY RAND() LIMIT :n;", catname=category, n=n)
                                return unhealthy_result.all(as_dict=True)"""

    def find_sub(self, category, n=c.LIMIT_SUBSTITUDE_FOOD):
        """ find a substitute to the food """
        """self.sub_list = []
                                self.url_list = []
                                self.store_list = []
                                self.note = []
                                self.sub_data = self.db.query("SELECT name, stores, url, nutri_score\
                                                              FROM Product\
                                                              WHERE category_id={} and nutri_score='a'\
                                                              OR category_id={} and nutri_score='b'\
                                                              OR category_id={} and nutri_score='c'\
                                                              ORDER BY RAND() LIMIT 1"
                                                              .format(category, category, category))
                                for element in self.sub_data:
                                    self.sub_list.append(element[0])
                                    self.url_list.append(element[1])
                                    self.store_list.append(element[2])
                                    self.note.append(element[3])

                                return self.sub_list, self.store_list, self.url_list, self.note"""
        healthy_result = self.db.query(f"""SELECT DISTINCT product_name,
            code, url_link, nutrition_grade_fr, brand FROM product
            JOIN product_category ON product_category.product_code =
            product.code
            JOIN category ON product_category.category_id = category.id
            WHERE nutrition_grade_fr IN ('a', 'b')
            AND category.name = :catname
            ORDER BY RAND() LIMIT :n;""",
            catname=category, n=n)
        return healthy_result.all(as_dict=True)

    def add_to_favories(self, product_code, substitute_code):
        """ add contents to the Favourite table """
        self.db.query(f"""INSERT INTO favorite (product_id, substitute_id)
            VALUES (:product_code, :substitute_code)""",
            product_code=product_code, substitute_code=substitute_code)

    def find_product_description(self, product_code):
        """This function shows the description of a selected product.
        """
        description = self.db.query(f"""SELECT * FROM product
            WHERE product.code = :code""",
            code=product_code)
        return description.all(as_dict=True)

    def find_stores_by_product_code(self, product_code):
        """ The function is called when the user wants to know
        where he can buy a product.
        """
        stores = self.db.query(f"""SELECT store.name FROM store
            JOIN product_store ON product_store.store_id = store.id
            JOIN product ON product_store.product_code = code
            WHERE product.code = :code""", code=product_code)
        return stores.all(as_dict=True)

    def get_favourite(self, product_code):
        """ get contents from Favourite table """
        """self.name_fav = []
                                self.url_fav = []
                                self.nutri_fav = []
                                self.store_fav = []
                                self.fav_data = self.db.query("SELECT name, url, nutri_score, stores\
                                                               FROM Favourite WHERE user_id={};"
                                                              .format(self.id))
                                for element in self.fav_data:
                                    self.name_fav.append(element[0])
                                    self.url_fav.append(element[1])
                                    self.nutri_fav.append(element[2])
                                    self.store_fav.append(element[3])

                                return self.name_fav, self.url_fav, self.nutri_fav, self.store_fav"""
        favorites = self.db.query(f"""SELECT substitute.code as sub_code,
            substitute.product_name as sub_prod_name,
            original.code as origin_code,
            original.product_name as origin_prod_name,
            original.nutrition_grade_fr as origin_nutri,
            favorite.substitute_id FROM favorite
            JOIN product AS substitute ON favorite.substitute_id = substitute.code
            JOIN product AS original ON favorite.product_id = original.code""")
        return favorites.all(as_dict=True)

    def add_to_favories(self, product_code, substitute_code):
        """ The function is called when the user wants to add a
        product into the table favorite.
        """
        self.db.query(f"""INSERT INTO favorite (product_id, substitute_id)
            VALUES (:product_code, :substitute_code)""",
            product_code=product_code, substitute_code=substitute_code)

    def delete_from_favorite(self, product_code):
        """ The function is called when the user wants to delete one of the
        favorites from the favorite list.
        """
        self.db.query(f"""DELETE FROM favorite WHERE product_id =
            :product_code""", product_code=product_code)

    def find_favorite_description(self, product_code):
        """This function shows the description of a selected product.
        """
        description = self.db.query(f"""SELECT * FROM product JOIN favorite
            ON product.code = favorite.product_id""",
            product_code=product_code)
        return description.all(as_dict=True)

    """def update_all(self):
    update all contents, delete and reput data """
    """self.db.query(""DELETE FROM Product;"")
    self.init_cat_list()
    self.init_all_category()"""


if __name__ == '__main__':
    app = DbManagement()
    app.init_cat_list()
    app.init_all_category()
