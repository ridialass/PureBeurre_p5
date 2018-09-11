#! /usr/bin/env python3
# coding: utf-8

import config as c
import records

class ProdManager:
    """
    """
    def __init__(self, db):
        """Inialization of the Client class."""
        self.db = db

    def lesshealthy_product_by_cat(self, category, n = c.LIMIT_BAD_PRODUCTS):
        """Method to get product-list of a selected category from DB."""
        lesshealthy = self.db.query(f"""SELECT DISTINCT
                product_name, code FROM product
                JOIN product_category ON product_category.product_code = product.code
                JOIN category ON product_category.category_id = category.id
                WHERE nutrition_grade_fr IN ('c', 'd', 'e')
                AND category.name LIKE :catname
                ORDER BY RAND() LIMIT :n;""",
                catname=category, n=n)
        return lesshealthy.all(as_dict=True)

    def healthy_product_by_cat(self, category, n = c.LIMIT_SUBSTITUDE_FOOD):
        """Method to get healthy-product-list from DB."""
        healthy = self.db.query(f"""SELECT DISTINCT product_name,
                code, url_link, nutrition_grade_fr, brand FROM product
                JOIN product_category ON product_category.product_code = product.code
                JOIN category ON product_category.category_id = category.id
                WHERE nutrition_grade_fr IN ('a', 'b')
                AND category.name LIKE :catname
                ORDER BY RAND() LIMIT :n;""",
                catname=category, n=n)
        return healthy.all(as_dict=True)

    def sub_description(self, product_code):
        """Method to get infos of selected product from DB."""
        description = self.db.query(f"""SELECT * FROM product
                        WHERE code = :code""", code = product_code)
        return description.all(as_dict=True)

class FavManager:
    """
    """
    def __init__(self, db):
        """Inialization of the Client class."""
        self.db = db

    def addfav_insert(self, product_code, sub_code):
        """Method to insert a new favorite product into DB."""
        self.db.query(f"""INSERT INTO favorite (product_id, substitute_id)
            VALUES (:product_code, :sub_code)""",
            product_code=product_code, sub_code=sub_code)



    def get_favs_list(self):
        """Method to get all favorite products from DB."""
        favorites = self.db.query(f"""SELECT substitute.code as sub_code,
            substitute.product_name as sub_prod_name,
            original.code as origin_code,
            original.product_name as origin_prod_name,
            original.nutrition_grade_fr as origin_nutri,
            favorite.substitute_id FROM favorite
            JOIN product AS substitute ON favorite.substitute_id = substitute.code
            JOIN product AS original ON favorite.product_id = original.code""")
        return favorites.all(as_dict=True)

    def dellfav_from_list(self, product_code):
        """Method to delete a selected favorite from DB."""
        self.db.query(f"""DELETE FROM favorite WHERE product_id =
            :product_code""", product_code=product_code)

class StoreManager:
    """
    """
    def __init__(self, db):
        """Inialization of the Client class."""
        self.db = db

    def get_store(self, product_code):
        """Method to get store info for a selected product from DB."""
        stores = self.db.query(f"""SELECT store.name FROM store
            JOIN product_store ON product_store.store_id = store.id
            JOIN product ON product_store.product_code = code
            WHERE product.code = :code""", code=product_code)
        return stores.all(as_dict=True)


if __name__ == "__main__":
    db = records.Database(c.DATABASE_URL)
