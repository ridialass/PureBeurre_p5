#! /usr/bin/env python3
# coding: utf-8
"""Client's methodes to interract with the server from the terminal."""

import config as c
from menu import Menu as m
from request import ProdManager, FavManager, StoreManager, records


class Client:
    """This class constructs and displays the different menus."""

    def __init__(self, db):
        """Inialization of the Client class."""
        self.db = db
        self.prod_code = None

    def quit(self):
        """Method to end app."""
        pass

    def welcome_menu(self):
        """Method used to display the welcome m."""
        title = 'bienvenue'
        m.menu_header(self, title)
        m.welcome(self)
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
        title = 'catégorie'
        m.menu_header(self, title)
        for i, cat in enumerate(c.CATEGORIES_TO_USE):
            print("{}: Catégorie des {}.".format(i + 1, cat))
            index_cat_list.append(str(i + 1))
        m.cat_options(self)
        m.menu_footer(self)
        choix_cat = input("Saisissez votre choix : ").strip().lower()
        if choix_cat in index_cat_list:
            cat_index = int(choix_cat)
            self.prod_menu(list(c.CATEGORIES_TO_USE.values())[cat_index - 1])
        elif choix_cat == "q":
            self.quit()
        elif choix_cat == "m":
            self.welcome_menu()
        elif choix_cat == "r":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.cat_menu()

    def prod_menu(self, category):
        """Method used to display some products from the selected category."""
        index_prod_list = []
        prod_code_list = []
        manager = ProdManager(self.db)
        title = 'produit*à*remplacer'
        m.menu_header(self, title)
        for i, prod in enumerate(manager.lesshealthy_product_by_cat(category)):
            print("{}=> {}.".format(i + 1, prod['product_name']))
            index_prod_list.append(str(i + 1))
            prod_code_list.append(prod['code'])
        m.product_options(self)
        m.menu_footer(self)
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix in index_prod_list:
            prod_index = int(choix)
            self.prod_code = prod_code_list[prod_index - 1]
            self.subs_menu(category)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        elif choix == "r":
            self.cat_menu()
        else:
            print("Choix non pris en charge")
            self.prod_menu(category)

    def subs_menu(self, category):
        """Method used to display healthier products of the same category."""
        index_subs_list = []
        subs_code_list = []
        manager = ProdManager(self.db)
        title = 'produits*de*substitution'
        m.menu_header(self, title)
        print("Nous vous proposons ces produits de substitution, "
              "lequel choisissez-vous ?\n")
        for i, prod in enumerate(manager.healthy_product_by_cat(category)):
            print("{}=> Produit: {} \n    Note nutritionnelle: {}\n"
                  .format(i + 1, prod['product_name'],
                          prod['nutrition_grade_fr'].capitalize()))
            index_subs_list.append(str(i + 1))
            subs_code_list.append(prod['code'])
        m.sub_options(self)
        m.menu_footer(self)
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix in index_subs_list:
            subs_index = int(choix)
            self.detail_prod_menu(subs_code_list[subs_index - 1], category)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        elif choix == "r":
            self.prod_menu(category)
        else:
            print("Choix non pris en charge")
            self.subs_menu(category)

    def addfav_menu(self, product_code, sub_code):
        """Method used to save a new favorite product."""
        manager = FavManager(self.db)
        title = 'ajout*de*favori'
        m.menu_header(self, title)
        manager.addfav_insert(product_code, sub_code)
        print("Votre choix a été sauvegardé dans les favoris.\n")
        self.favs_menu()

    def detail_prod_menu(self, product_code, category):
        """Method used to display a product's details."""
        p_manager = ProdManager(self.db)
        s_manager = StoreManager(self.db)
        title = 'details*du*produit'
        m.menu_header(self, title)
        print("Que souhaitez-vous faire du produit ?\n")
        for i, prod in enumerate(p_manager.sub_description(product_code)):
            print(" Produit: {}\n Code_barre: {}\n Marque: {}\n Lien_web: {}\n"
                  " Grade nutritionnelle: {}"
                  .format(prod['product_name'], prod['code'], prod['brand'],
                          prod['url_link'],
                          prod['nutrition_grade_fr'].capitalize()))
            for i, score in enumerate(s_manager.get_store(product_code)):
                print(" Magasin de vente: {}".format(score['name']))
        m.detail_prod_options(self)
        m.menu_footer(self)
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix == "s":
            self.addfav_menu(product_code, self.prod_code)
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        elif choix == "r":
            self.subs_menu(category)
        else:
            print("Choix non pris en charge")
            self.detail_prod_menu(product_code)

    def favs_menu(self):
        """Method used to display the saved favorites list."""
        index_favs_list = []
        favs_code_list = []
        manager = FavManager(self.db)
        title = 'liste*de*mes*favoris'
        m.menu_header(self, title)
        for i, fav in enumerate(manager.get_favs_list()):
            print("{}=> {} remplace le produit : {}"
                  .format(i + 1, fav['origin_prod_name'],
                          fav['sub_prod_name']))
            index_favs_list.append(str(i + 1))
            favs_code_list.append(fav['origin_code'])
        m.favorite_options(self)
        m.menu_footer(self)
        choix = input("Saisissez votre choix : ").strip().lower()
        if choix in index_favs_list:
            favs_index = int(choix)
            self.detail_fav_menu(favs_code_list[favs_index - 1])
        elif choix == "q":
            self.quit()
        elif choix == "m":
            self.welcome_menu()
        elif choix == "r":
            self.welcome_menu()
        else:
            print("Choix non pris en charge")
            self.favs_menu()

    def dellfav_menu(self, product_code):
        """Method used to delete a product from favorites list."""
        manager = FavManager(self.db)
        title = 'suppression*de*favoris'
        m.menu_header(self, title)
        manager.dellfav_from_list(product_code)
        print('Votre choix a été supprimé des favoris.\n')
        self.favs_menu()

    def detail_fav_menu(self, product_code):
        """Method used to display the slected favorite's details."""
        p_manager = ProdManager(self.db)
        s_manager = StoreManager(self.db)
        title = 'details*du*favori'
        m.menu_header(self, title)
        print("Que souhaitez-vous faire de ce favori ?\n")
        for i, prod in enumerate(p_manager.sub_description(product_code)):
            print(" Produit: {}\n Code_barre: {}\n Marque: {}\n Lien_web: {}\n"
                  " Note nutritionnelle: {}"
                  .format(prod['product_name'], prod['code'], prod['brand'],
                          prod['url_link'],
                          prod['nutrition_grade_fr'].capitalize()))
            for i, score in enumerate(s_manager.get_store(product_code)):
                print(" Magasin de vente: {}".format(score['name']))
        m.detail_fav_options(self)
        m.menu_footer(self)
        choix = input("Saisissez votre choix : ").strip().lower()
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
    db_username = c.DB_USER
    db_password = c.DB_PASS
    db_name = c.DB_NAME
    db = records.Database('mysql+mysqlconnector://{}:{}@localhost:6606/{}?charset=utf8mb4'
                          .format(db_username, db_password, db_name))
    app = Client(db)
    app.welcome_menu()

if __name__ == "__main__":
    main()
