#! /usr/bin/env python3
# coding: utf-8


class Menu:
    """This class constructs and displays the different menus."""

    def __init__(self):
        """Inialization of the Client class."""
        pass

    def menu_header(self, title):
        """Menu header."""
        print("**********{}*MENU**********\n".format(title.upper()))

    def menu_footer(self):
        """Menu footer."""
        print("Rafraichir le menu précédant en appuyant sur la touche: r")
        print('Pour revenir au menu principal appuyer la touche: m')
        print("Pour quitter l'application appuyer la touche: q\n")

    def welcome(self):
        """Method used to display the welcome menu."""
        print('Veuillez choisir une option et appuyez sur Entrée :\n')
        print('Pour choisir un aliment à remplacer appuyer la touche: 1')
        print('Pour retrouver mes substituts favoris appuyer la touche: 2')
        print("Pour quitter l'application appuyer la touche: q\n")

    def cat_options(self):
        """Cat."""
        print('\nSélectionnez la catégorie en entrant son numéro :')

    def product_options(self):
        """Prod."""
        print('\nSélectionnez le produit à remplacer en entrant le numéro.')

    def sub_options(self):
        """Substitute."""
        print('\nSélectionnez le produit choisi en entrant son numéro :')

    def detail_prod_options(self):
        """Detail product."""
        print('\nEnregister le produit dans les favoris en appuyant sur la touche: s')

    def favorite_options(self):
        """Favorite."""
        print("\nSélectionnez un des favoris en entrant son numéro :")

    def detail_fav_options(self):
        """Detail favorite."""
        print('\nSupprimer le favori en appuyant sur la touche: x')
