from tkinter import *
from math import log10
import Pmw            # logarithmes en base 10
import config as c

class Application:
    def __init__(self):
        """Constructeur de la fenêtre principale"""
        self.root = Pmw.initialise()
        self.root.title('Open Food Facts')
        self.display_cat()
        Label(self.root, text ="Selectionner un des catégories sur la liste").grid(row =2)
        Button(self.root, text ='Favoris',
              command =self.changeCouleurs).grid(row =3, sticky = W)
        Button(self.root, text ='Catégories',
              command =self.changeCouleurs).grid(row =3, sticky = E)
        Button(self.root, text ='Quitter',
              command =self.root.quit).grid(row =4, sticky = S)
        # Code des couleurs pour les valeurs de zéro à neuf :
        self.cc = ['black','brown','red','orange','yellow',
                  'green','blue','purple','grey','white']
        self.root.mainloop()

    def display_cat(self):
        """Canevas avec un modèle de résistance à trois lignes colorées"""
        self.can = Canvas(self.root, width=850, height =600, bg ='ivory')
        self.can.grid(row =1, pady =5, padx =5)
        self.categories = Listbox(self.can)
        for cat in c.CATEGORIES_TO_USE:
            self.categories.insert(END, cat)
        self.categories.grid(row=3, column=0, sticky='NSEW')
        self.categories.configure(bg='white', fg='black',
                                  relief='solid')
        #self.categories.bind('<<ListboxSelect>>', self.display_food)

    def display_food_box(self):
        """ display food titles and listbox """
        self.title_food = tk.Label(self, text='FOODS')
        self.title_food.grid(row=2, column=2, sticky='NSEW', pady=(60, 0))
        self.title_food.configure(font=self.font_button, bg='white')

    def changeCouleurs(self):
       """Affichage des couleurs correspondant à la valeur entrée"""
       self.v1ch = self.entree.get()       # la méthode get() renvoie une chaîne
       try:
           v = float(self.v1ch)            # conversion en valeur numérique
       except:
           err =1                          # erreur : entrée non numérique
       else:
           err =0
       if err ==1 or v < 10 or v > 1e11 :
           self.signaleErreur()            # entrée incorrecte ou hors limites
       else:
           li =[0]*3                       # liste des 3 codes à afficher
           logv = int(log10(v))            # partie entière du logarithme
           ordgr = 10**logv                # ordre de grandeur
           # extraction du premier chiffre significatif :
           li[0] = int(v/ordgr)            # partie entière
           decim = v/ordgr - li[0]         # partie décimale
           # extraction du second chiffre significatif :
           li[1] = int(decim*10 +.5)           # +.5 pour arrondir correctement
           # nombre de zéros à accoler aux 2 chiffres significatifs :
           li[2] = logv -1
           # Coloration des 3 lignes :
           for n in range(3):
               self.can.itemconfigure(self.ligne[n], fill =self.cc[li[n]])

    def signaleErreur(self):
       pass

    def videEntree(self):
      pass

# Programme principal :
              # logarithmes en base 10
f = Application()

def sub_menu(self, product_code):
        "Method used to display the selected healthy product.""
        manager = ProdManager(self.db)
        print("\n**********PRODUIT*DE*SUBSTITUT*MENU**********\n")
        print("Pour ce produit de substitution, que souhaitez-vous faire ?\n")
        index_sub_list = []
        for i, prod in enumerate(manager.sub_description(product_code)):
            print("{}=> Produit: {} \n    Note nutritionnelle: {}".format(i+1, prod['product_name'],
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

def fav_menu(self, product_code):
        """Method used to display the selected favorite product."""
        manager = ProdManager(self.db)
        print("\n**********PRODUIT*FAVORI*MENU**********\n")
        print("Pour ce favori, que souhaitez-vous faire ?\n")
        index_sub_list = []
        for i, prod in enumerate(manager.sub_description(product_code)):
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
