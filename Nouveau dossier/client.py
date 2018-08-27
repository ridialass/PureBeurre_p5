#!/usr/bin/env python3
# -*- coding: Utf-8 -*
import config as c
import sys
import records
import requests

class Client:
    """This class constructs and displays the different menus
    during the life of the application.
    """
    def __init__(self, db):
        """Inialization of the Client class."""
        self.db = db
        self.prod_code = None

    def welcome_menu(self):
        """Method used to display the welcome menu"""
        print("**********BIENVENUE*MENU**********\n")
        print('Veuillez choisir une option et appuyez sur Entrée :\n')
        print('Pour choisir un aliment à remplacer appuyer la touche: 1')
        print('Pour retrouver mes substituts favoris appuyer la touche: 2')
        print("Pour quitter l'application appuyer la touche: q\n")
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix == "1":
            self.cat_menu()
        elif choix == "2":
            self.favs_menu()
        elif choix == "q":
            self.quit()
        else:
            print("Choix non pris en charge\n")
            self.welcome_menu()

    def cat_menu(self):
        """Method used to display the list of several categories."""
        index_cat_list = []
        print("\n**********CATEGORIE*MENU**********\n")
        for i, cat in enumerate(c.CATEGORIES_TO_USE):
            print("{}: Catégorie des {}.".format(i+1, cat))
            index_cat_list.append(str(i+1))
        print('\nSélectionnez la catégorie en entrant son numéro :')
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m\n')
        choix_cat = input("Saisissez votre choix : ").strip().lower()
        if choix_cat in index_cat_list:
            cat_index = int(choix_cat)
            self.prod_menu(list(c.CATEGORIES_TO_USE.values())[cat_index-1])
        elif choix_cat == "q":
            self.quit()
        elif choix_cat == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.cat_menu()

    def quit(self):
        """Method to end app."""
        pass

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

    def prod_menu(self, category):
        """Method used to display some products from the selected category"""
        index_prod_list = []
        prod_code_list = []
        print("\n**********PRODUITS*A*REMPLACER*MENU**********\n")
        for i, prod in enumerate(self.lesshealthy_product_by_cat(category)):
            print("{}=> {}.".format(i+1, prod['product_name']))
            index_prod_list.append(str(i + 1))
            prod_code_list.append(prod['code'])
        print('\nSélectionnez le produit à remplacer en entrant son numéro.')
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m\n')
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix in index_prod_list:
            prod_index = int(choix)
            self.prod_code = prod_code_list[prod_index - 1]
            self.subs_menu(category)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.prod_menu(category)

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

    def subs_menu(self, category):
        """Method used to display healthier products of the same category"""
        print("\n**********PRODUITS*SUBSTITUTS*MENU**********\n")
        print("Nous vous proposons ces produits de substitution, "
                "lequel choisissez-vous ?\n")
        index_subs_list = []
        subs_code_list = []
        for i, prod in enumerate(self.healthy_product_by_cat(category)):
            print("{}=> Produit: {} \n    Note nutritionnelle: {}\n".format(i+1,
                prod['product_name'], prod['nutrition_grade_fr'].capitalize()))
            index_subs_list.append(str(i + 1))
            subs_code_list.append(prod['code'])
        print('\nSélectionnez le produit choisi en entrant son numéro :')
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m\n')
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix in index_subs_list:
            subs_index = int(choix)
            self.sub_menu(subs_code_list[subs_index - 1])
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.subs_menu(category)

    def sub_description(self, product_code):
        """Method to get infos of selected product from DB."""
        description = self.db.query(f"""SELECT * FROM product
                        WHERE code = :code""", code = product_code)
        return description.all(as_dict=True)

    def sub_menu(self, product_code):
        """Method used to display the selected healthy product."""
        print("\n**********PRODUIT*DE*SUBSTITUT*MENU**********\n")
        print("Pour ce produit de substitution, que souhaitez-vous faire ?\n")
        index_sub_list = []
        for i, prod in enumerate(self.sub_description(product_code)):
            print("{}=> Produit: {} \n    Grade nutritionnelle: {}".format(i+1, prod['product_name'],
                prod['nutrition_grade_fr'].capitalize()))
            index_sub_list.append(str(i + 1))
        print('\nConsulter la description détaillée du substitut en appuyant sur la touche: i')
        print('Enregister le substitut dans les favoris en appuyant sur la touche: s')
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m')
        choix = input("Saisissez votre choix : ")
        if choix == "i":
            self.detail_prod_menu(product_code)
        elif choix == "s":
            self.addfav_menu(product_code, self.prod_code)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.sub_menu(product_code)

    def addfav_insert(self, product_code, sub_code):
        """Method to insert a new favorite product into DB."""
        self.db.query(f"""INSERT INTO favorite (product_id, substitute_id)
            VALUES (:product_code, :sub_code)""",
            product_code=product_code, sub_code=sub_code)

    def addfav_menu(self, product_code, sub_code):
        """Method used to save a new favorite product."""
        print("\n**********AJOUT*FAVORI*MENU**********\n")
        self.addfav_insert(product_code, sub_code)
        print("Votre choix a été sauvegardé dans les favoris.\n")
        self.favs_menu()

    def get_store(self, product_code):
        """Method to get store info for a selected product from DB."""
        stores = self.db.query(f"""SELECT store.name FROM store
            JOIN product_store ON product_store.store_id = store.id
            JOIN product ON product_store.product_code = code
            WHERE product.code = :code""", code=product_code)
        return stores.all(as_dict=True)

    def detail_prod_menu(self, product_code):
        """Method used to display a product's details."""
        print("\n**********DETAILS*PRODUIT*MENU**********\n")
        print("Que souhaitez-vous faire du produit ?\n")
        for i, prod in enumerate(self.sub_description(product_code)):
            print(" Produit: {}\n Code_barre: {}\n Marque: {}\n Lien_web: {}\n Grade nutritionnelle: {}"
                .format(prod['product_name'], prod['code'], prod['brand'],
                    prod['url_link'], prod['nutrition_grade_fr'].capitalize()))
            for i, score in enumerate(self.get_store(product_code)):
                print(" Magasin de vente: {}".format(score['name']))
        print('\nEnregister le produit dans les favoris en appuyant sur la touche: s')
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m\n')
        choix = input("Saisissez votre choix : ")
        if choix == "s":
            self.addfav_menu(product_code, self.prod_code)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.detail_prod_menu(product_code)

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

    def favs_menu(self):
        """Method used to display the saved favorites list."""
        print("\n**********LISTE*FAVORIS*MENU**********\n")
        index_favs_list = []
        favs_code_list = list()
        for i, fav in enumerate(self.get_favs_list()):
            print("{}=> {} remplace le produit : {}".format(i+1, fav['origin_prod_name'],
                fav['sub_prod_name']))
            index_favs_list.append(str(i + 1))
            favs_code_list.append(fav['origin_code'])
        print("\nSélectionnez un des favoris en entrant son numéro :")
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m\n')
        choix = input("Saisissez votre choix : ")
        if choix in index_favs_list:
            favs_index = int(choix)
            self.fav_menu(favs_code_list[favs_index - 1])
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.favs_menu()

    def fav_menu(self, product_code):
        """Method used to display the selected favorite product."""
        print("\n**********PRODUIT*FAVORI*MENU**********\n")
        print("Pour ce favori, que souhaitez-vous faire ?\n")
        index_sub_list = []
        for i, prod in enumerate(self.sub_description(product_code)):
            print("{}=> Produit: {} \n    Grade nutritionnelle: {}".format(i+1, prod['product_name'],
                prod['nutrition_grade_fr'].capitalize()))
            index_sub_list.append(str(i + 1))
        print('\nConsulter la description détaillée du favori en appuyant sur la touche: i')
        print('Supprimer le favori en appuyant sur la touche: x')
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m')
        choix = input("Saisissez votre choix : ")
        if choix == "i":
            self.detail_fav_menu(product_code)
        elif choix == "x":
            self.dellfav_menu(product_code)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.fav_menu(product_code)

    def dellfav_from_list(self, product_code):
        """Method to delete a selected favorite from DB."""
        self.db.query(f"""DELETE FROM favorite WHERE product_id =
            :product_code""", product_code=product_code)

    def dellfav_menu(self, product_code):
        """Method used to delete a product from favorites list."""
        print("\n**********SUPPRIME*MENU**********\n")
        self.dellfav_from_list(product_code)
        print('Votre choix a été supprimé des favoris.\n')
        self.favs_menu()

    def detail_fav_menu(self, product_code):
        """Method used to display the slected favorite's details."""
        print("\n**********DETAIL*FAVORI*MENU**********\n")
        print("Que souhaitez-vous faire de ce favori ?\n")
        for i, prod in enumerate(self.sub_description(product_code)):
            print(" Produit: {}\n Code_barre: {}\n Lien_web: {}\n Marque: {}\n Grade nutritionnelle: {}"
                .format(prod['product_name'], prod['code'], prod['brand'],
                    prod['url_link'], prod['nutrition_grade_fr'].capitalize()))
            for i, score in enumerate(self.get_store(product_code)):
                print(" Magasin de vente: {}".format(score['name']))
        print('\nSupprimer le favori en appuyant sur la touche: x')
        print("Revenir à la liste des favoris en appuyant sur la touche: r")
        print("Pour quitter l'application appuyer la touche: q")
        print('Pour revenir au menu principal appuyer la touche: m\n')
        choix = input("Saisissez votre choix : ")
        if choix == "x":
            self.dellfav_menu(product_code)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        elif choix == "r":
            self.favs_menu()
        else:
            print("Choix non pris en charge")
            self.detail_prod_menu(product_code)

def main():
    """Main entry point of the application."""
    db = records.Database(c.DATABASE_URL)
    app = Client(db)
    app.welcome_menu()

if __name__ == "__main__":
    main()
