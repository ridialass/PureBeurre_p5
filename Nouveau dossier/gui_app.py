import tkinter as tk
import webbrowser
from database_management import DbManagement
import config as c
from tkinter.font import Font
from connexion import Connexion
from time import sleep


class GuiInterface(tk.Tk):
    """ tkinter interface """

    def __init__(self):
        """ init window size, font, title """
        tk.Tk.__init__(self)
        self.window_height = 450
        self.window_width = 450
        self.geometry('{}x{}+2200+0'.format(self.window_width,
                                            self.window_height))
        self.resizable(0, 0)
        self.title("OpenFoodFacts")
        self.font_warn = Font(family='Zekton', size=8)
        self.font_title = Font(family='Capture it', size=32)
        self.font = Font(family='Zekton', size=12)
        self.font_button = Font(family='Capture it', size=18)
        self.grid_columnconfigure(0, weight=2)
        # INIT CATEGORY LIST FROM FILE
        DbManagement().init_cat_list()

    def display_background(self):
        """ display background """
        self.c = tk.Canvas(self, height=450, width=450)
        self.img_path = tk.PhotoImage(file='background.png')
        self.image = tk.Label(self, image=self.img_path)
        self.image.place(x=0, y=0, relwidth=1, relheight=1)


    def display_button(self):
        """ display buttons log in , sign up , update, quit """
        """self.update_button = tk.Button(self, text='Update',
                                                               command=self.update_window)
                                self.update_button.grid(row=6, column=0, sticky='NSEW', ipady=15)
                                self.update_button.configure(font=self.font_button, bg='white',
                                                             relief='solid')"""
        self.quit_b = tk.Button(self, text='Quit',
                                command=self.quit_app)
        self.quit_b.grid(row=6, column=2, sticky='NSEW', ipady=15)
        self.quit_b.configure(font=self.font_button, relief='solid')# bg=self.color_signup,


    def update_window(self):
        """ new window, update window """
        self.up_window = tk.Toplevel()
        self.up_window.title("OpenFoodFacts")
        self.up_window.geometry('450x450+1600+0')
        self.up_window.resizable(0, 0)
        self.up_window.configure(background='white')
        self.up_window.title_up = tk.Label(self.up_window, text="update")
        self.up_window.title_up.grid(row=0, columnspan=2, sticky='NSEW',
                                     ipadx=150)
        self.up_window.title_up.configure(font=self.font_title, bg='white')
                                          #fg=self.color_signup)
        self.up_window.categories = tk.Label(self.up_window, text="Categories")
        self.up_window.categories.grid(row=1, columnspan=2, sticky='NSEW',
                                       pady=5)
        self.up_window.categories.configure(font=self.font_button, bg='white')
                                            #fg=self.color_signup)
        self.cat_ug = CAT_UG
        x = 2
        for element in self.cat_ug:
            self.up_window.c_one = tk.Label(self.up_window,
                                            text='{}'.format(element))
            self.up_window.c_one.grid(row=x, columnspan=2, sticky='NSEW')
            self.up_window.c_one.configure(font=self.font, bg='white',
                                           fg='black')
            x += 1

        self.up_window.button_update = tk.Button(self.up_window,
                                                 text='Update ALL',
                                                 command=self.update_all_cat)
        self.up_window.button_update.grid(row=12, columnspan=2, sticky='NSEW',
                                          ipady=28)
        self.up_window.button_update.configure(font=self.font_button,
                                                fg='black', relief='solid')
                                               # bg=self.color_signup

    """def update_all_cat(self):
    update all contents , display a new button disabled 'wait'
    self.up_window.button_update.destroy()
    self.up_window.button_wait = tk.Button(self.up_window, text='WAIT..',
                                           command=self.update_all_cat,
                                           state='disabled')
    self.up_window.button_wait.grid(row=12, columnspan=2, sticky='NSEW',
                                    ipady=28)
    self.up_window.button_wait.configure(font=self.font_button,
                                         bg='red',
                                         fg='black', relief='solid')
    self.up_window.update()
    DbManagement().update_all()
    self.up_window.destroy()"""

    def back_menu(self):
        """ back action , destroy elements """
        try:
            self.warning_error.destroy()
        except AttributeError:
            pass
        try:
            self.enter_valid.destroy()
        except AttributeError:
            pass
        self.back_button.destroy()
        self.display_button()

    def logged(self):
        """ display when you are log """
        #self.login_label.destroy()
        #self.login_entry.destroy()
        #self.pwd_label.destroy()
        #self.password_entry.destroy()
        #self.button_login.destroy()
        #self.button_signup.destroy()
        #self.update_button.destroy()
        #self.quit_b.destroy()

        self.display_categories()
        self.display_food_box()

        self.button_history = tk.Button(self, text='Favories',
                                        command=self.favories)
        self.button_history.grid(row=5, column=0, sticky='NSEW')
        self.button_history.configure(font=self.font_button, bg='white',
                                      relief='solid')

        self.button_start = tk.Button(self, text='Find a substitute',
                                      command=self.start)
        self.button_start.grid(row=4, columnspan=3, sticky='NSEW',
                               pady=(10, 0))
        self.button_start.configure(font=self.font_button, bg='white',
                                    relief='solid')
        self.quit_button = tk.Button(self, text='Quit',
                                     command=self.quit_app)
        self.quit_button.grid(row=6, columnspan=3, sticky='NSEW')
        self.quit_button.configure(font=self.font_button,# bg=self.color_signup,
                                   relief='solid')

    def quit_app(self):
        """ quit action """
        self.destroy()

    def display_categories(self):
        """ display categories titles and listbox """
        self.title_categorie = tk.Label(self, text='CATEGORIES')
        self.title_categorie.grid(row=2, column=0, sticky='NSEW', pady=(60, 0))
        self.title_categorie.configure(font=self.font_button, bg='white')
                                       #fg=self.color_signup)
        self.categories = tk.Listbox(self)
        for cat in c.CATEGORIES_TO_USE:
            self.categories.insert(tk.END, cat)
        self.categories.grid(row=3, column=0, sticky='NSEW')
        self.categories.configure(font=self.font, bg='white', fg='black',
                                  relief='solid')
        self.categories.bind('<<ListboxSelect>>', self.display_food)

        self.arrow = tk.Label(self, text='->')
        self.arrow.grid(row=3, column=1)
        self.arrow.configure(font=self.font_button,# bg=self.color_signup,
                             fg='white')

    def display_food_box(self):
        """ display food titles and listbox """
        self.title_food = tk.Label(self, text='FOODS')
        self.title_food.grid(row=2, column=2, sticky='NSEW', pady=(60, 0))
        self.title_food.configure(font=self.font_button, bg='white')
                                  #fg=self.color_signup)
        self.food = tk.Listbox(self)
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=3, column=2, sticky='NSE')
        self.food.grid(row=3, column=2, sticky='E')
        self.food.configure(font=self.font,
                            yscrollcommand=self.scrollbar.set, relief='solid')
        self.scrollbar.configure(command=self.food.yview, relief='solid')

    def display_food(self, entries={}):
        """ display food corresponding with categories"""
        #product_manager = DbManagement()
        app = DbManagement()
        self.select_cat = self.categories.curselection()
        try:
            if self.select_cat[0] == 0:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('1')
                self.sub, self.url, self.store, self.note = app.find_sub('1')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 1:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('2')
                self.sub, self.url, self.store, self.note = app.find_sub('2')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 2:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('3')
                self.sub, self.url, self.store, self.note = app.find_sub('3')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 3:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('4')
                self.sub, self.url, self.store, self.note = app.find_sub('4')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 4:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('5')
                self.sub, self.url, self.store, self.note = app.find_sub('5')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 5:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('6')
                self.sub, self.url, self.store, self.note = app.find_sub('6')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 6:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('7')
                self.sub, self.url, self.store, self.note = app.find_sub('7')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 7:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('8')
                self.sub, self.url, self.store, self.note = app.find_sub('8')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 8:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('9')
                self.sub, self.url, self.store, self.note = app.find_sub('9')
                for element in self.list:
                    self.food.insert(tk.END, element)
            elif self.select_cat[0] == 9:
                self.food.delete(0, tk.END)
                self.list = app.display_list_food('10')
                self.sub, self.url, self.store, self.note = app.find_sub('10')
                for element in self.list:
                    self.food.insert(tk.END, element)
        except IndexError:
            pass

    def favories(self):
        """ favories window """
        self.fav_window = tk.Toplevel()
        self.fav_window.title("OpenFoodFacts")
        self.fav_window.geometry('850x500+1600+0')
        self.fav_window.configure(background='white')
        self.fav_window.title_up = tk.Label(self.fav_window, text="Favories")
        self.fav_window.title_up.grid(row=0, columnspan=4, sticky='NSEW',
                                      ipadx=140)
        self.fav_window.title_up.configure(font=self.font_title, bg='white')
                                           #fg=self.color_signup)
        self.fav_window.categories = tk.Label(self.fav_window, text="Product")
        self.fav_window.categories.grid(row=1, column=0, sticky='W', pady=5)
        self.fav_window.categories.configure(font=self.font_button, bg='white')
                                             #fg=self.color_signup)
        self.fav_window.categories = tk.Label(self.fav_window, text="Url")
        self.fav_window.categories.grid(row=1, column=1, sticky='W', pady=5)
        self.fav_window.categories.configure(font=self.font_button, bg='white')
                                             #fg=self.color_signup)
        self.fav_window.categories = tk.Label(self.fav_window,
                                              text="SCORE")
        self.fav_window.categories.grid(row=1, column=2, sticky='W', pady=5)
        self.fav_window.categories.configure(font=self.font_button, bg='white')
                                             #fg=self.color_signup)
        self.fav_window.categories = tk.Label(self.fav_window, text="Stores")
        self.fav_window.categories.grid(row=1, column=3, sticky='E', pady=5,
                                        padx=40)
        self.fav_window.categories.configure(font=self.font_button, bg='white')
                                             #fg=self.color_signup)
        self.display_fav()

    def start(self):
        """ find a substitute , display new window with results"""
        self.sub_window = tk.Toplevel()
        self.sub_window.title("OpenFoodFacts")
        self.sub_window.geometry('450x450+1600+0')
        self.sub_window.resizable(0, 0)
        self.sub_window.configure(background='white')
        self.sub_window.title_up = tk.Label(self.sub_window, text="SUBSTITUTE")
        self.sub_window.title_up.grid(row=0, columnspan=2, sticky='W',
                                      ipadx=115)
        self.sub_window.title_up.configure(font=self.font_title, bg='white')
                                           #fg=self.color_signup)
        self.sub_window.categories = tk.Label(self.sub_window,
                                            text="Product Healthy")
        self.sub_window.categories.grid(row=1, column=0, sticky='W', pady=5)
        self.sub_window.categories.configure(font=self.font_button, bg='white')
                                            #fg=self.color_signup)
        self.sub_window.categories = tk.Label(self.sub_window, text="URL")
        self.sub_window.categories.grid(row=5, column=0, sticky='W', pady=5)
        self.sub_window.categories.configure(font=self.font_button, bg='white')
                                             #fg=self.color_signup)
        self.sub_window.categories = tk.Label(self.sub_window,
                                              text="{}".format(self.sub[0]))
        self.sub_window.categories.grid(row=2, column=0, sticky='W', pady=5)
        self.sub_window.categories.configure(font=self.font, bg='white',
                                             fg='black')
        self.sub_window.url = tk.Label(self.sub_window,
                                       text="{}".format(self.url[0]),
                                       cursor="hand2")
        self.sub_window.url.grid(row=6, column=0, sticky='W', pady=5)
        self.sub_window.url.configure(font=self.font, bg='white',
                                      fg='blue', wrap=440)
        self.sub_window.url.bind("<Button-1>", self.call_link)
        self.sub_window.categories = tk.Label(self.sub_window, text="STORES")
        self.sub_window.categories.grid(row=7, column=0, sticky='W', pady=5)
        self.sub_window.categories.configure(font=self.font_button, bg='white')
                                             #fg=self.color_signup)
        self.sub_window.categories = tk.Label(self.sub_window,
                                              text="{}".format(self.store[0]))
        self.sub_window.categories.grid(row=8, column=0, sticky='W', pady=5)
        self.sub_window.categories.configure(font=self.font, bg='white',
                                             fg='black')
        self.sub_window.add_to_fav = tk.Button(self.sub_window,
                                               text='ADD TO FAVORIES',
                                               command=self.add_to_fav)
        self.sub_window.add_to_fav.grid(row=9, columnspan=1,
                                        pady=(40, 0))
        self.sub_window.add_to_fav.configure(font=self.font_button, relief='solid')
                                             #bg=self.color_signup,

        self.sub_window.nutri_score = tk.Label(self.sub_window,
                                               text='NUTRISCORE')
        self.sub_window.nutri_score.grid(row=3, column=0, sticky='W')
        self.sub_window.nutri_score.configure(font=self.font_button,
                                              bg='white')#, fg=self.color_signup)
        self.sub_window.nutri_score = tk.Label(self.sub_window, text='{}'
                                               .format(self.note[0]))
        self.sub_window.nutri_score.grid(row=4, column=0, sticky='W')
        self.sub_window.nutri_score.configure(font=self.font, bg='white',
                                              fg='black')

    def display_fav(self):
        """ display favories in the window favourite """
        self.nf, self.uf, self.nsf, self.sf = DbManagement().get_favourite()
        x = 2
        y = 0
        for n in self.nf:
            self.fav_window.label = tk.Label(self.fav_window,
                                             text='{}'.format(n))
            self.fav_window.label.grid(row=x, column=y, sticky='W')
            self.fav_window.label.configure(font=self.font, bg='white',
                                            fg='black', wrap=300,
                                            justify='left')
            x += 1
        x = 2
        for u in self.uf:
            self.fav_window.url = tk.Label(self.fav_window,
                                           text='{}'.format(u))
            self.fav_window.url.grid(row=x, column=y+1, sticky='W')
            self.fav_window.url.configure(font=self.font, bg='white',
                                          fg='blue', wrap=300,
                                          justify='left')
            x += 1
        x = 2
        for ns in self.nsf:
            self.fav_window.label = tk.Label(self.fav_window,
                                             text='{}'.format(ns))
            self.fav_window.label.grid(row=x, column=y+2, sticky='NSEW')
            self.fav_window.label.configure(font=self.font, bg='white',
                                            fg='black')
            x += 1
        x = 2
        for s in self.sf:
            self.fav_window.label = tk.Label(self.fav_window,
                                             text='{}'.format(s))
            self.fav_window.label.grid(row=x, column=y+3, sticky='NSEW')
            self.fav_window.label.configure(font=self.font, bg='white',
                                            fg='black')
            x += 1

    def call_link(self, event):
        """ open a webbrowser page when you click on the link"""
        webbrowser.open_new("{}".format(self.url[0]))

    def add_to_fav(self):
        """ add to favourite """
        DbManagement().add_to_favories(self.sub[0], self.url[0], self.note[0],
                                       self.store[0])
        self.sub_window.destroy()

    """def logout(self):
    logout """
    """try:
        self.warning_error.destroy()
    except AttributeError:
        pass
    try:
        self.enter_valid.destroy()
    except AttributeError:
        pass
    self.title_food.destroy()
    self.title_categorie.destroy()
    self.categories.destroy()
    self.arrow.destroy()
    self.food.destroy()
    self.scrollbar.destroy()
    self.button_history.destroy()
    self.button_start.destroy()
    self.button_logout.destroy()
    ID_USER.clear()
    self.run()"""

    def run(self):
        """ display main page """
        #self.display_background()
        #self.display_login()
        self.logged()
        self.display_button()


if __name__ == '__main__':
    app = GuiInterface()
    app.run()
    app.mainloop()
