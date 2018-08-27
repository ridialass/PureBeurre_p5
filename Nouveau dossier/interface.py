#!/usr/bin/env python3
# coding: Utf-8

"""from tkinter import *

fen1 = Tk()
can1 = Canvas(fen1,bg='white', height=210, width=210)
can1.grid(row =3, column =1, padx =10, pady =10)
""background = PhotoImage(file ='background.png')
item = can1.create_image(150, 150, image = background)"
text_bienvenue = Label(can1, text='Bienvenue à mon application', fg='red')
text_bienvenue.grid(row =0, sticky = E)
tex_category = Label(can1, text='Veuillez choisir une option et appuyez sur Entrée :', fg='red')
tex_category.grid(row =1, sticky = E)
tex1 = Label(can1, text='Quel aliment souhaitez-vous remplacer ?', fg='red')
tex1.grid(row =2, sticky =E)
button_back = Button(fen1, text='Menu', command = fen1.destroy)
button_back.grid(row =0, sticky = W)
button_quit = Button(fen1, text='Quitter', command = fen1.destroy)
button_quit.grid(row =0, sticky =E)
fen1.mainloop()

import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        b = tk.Button(self, text="Done!", command=self.upload_cor)
        b.pack()
        table = tk.Frame(self)
        table.pack(side="top", fill="both", expand=True)

        data = (
            (45417, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
            (45418, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
            (45419, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
            (45420, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
            (45421, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
            (45422, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
            (45423, "rodringof", "CSP L2 Review", 0.000394, "2014-12-19 10:08:12", "2014-12-19 10:08:12"),
        )

        self.widgets = {}
        row = 0
        for rowid, reviewer, task, num_seconds, start_time, end_time in (data):
            row += 1
            self.widgets[rowid] = {
                "rowid": tk.Label(table, text=rowid),
                "reviewer": tk.Label(table, text=reviewer),
                "task": tk.Label(table, text=task),
                "num_seconds_correction": tk.Entry(table),
                "num_seconds": tk.Label(table, text=num_seconds),
                "start_time": tk.Label(table, text=start_time),
                "end_time": tk.Label(table, text=start_time)
            }

            self.widgets[rowid]["rowid"].grid(row=row, column=0, sticky="nsew")
            self.widgets[rowid]["reviewer"].grid(row=row, column=1, sticky="nsew")
            self.widgets[rowid]["task"].grid(row=row, column=2, sticky="nsew")
            self.widgets[rowid]["num_seconds_correction"].grid(row=row, column=3, sticky="nsew")
            self.widgets[rowid]["num_seconds"].grid(row=row, column=4, sticky="nsew")
            self.widgets[rowid]["start_time"].grid(row=row, column=5, sticky="nsew")
            self.widgets[rowid]["end_time"].grid(row=row, column=6, sticky="nsew")

        table.grid_columnconfigure(1, weight=1)
        table.grid_columnconfigure(2, weight=1)
        # invisible row after last row gets all extra space
        table.grid_rowconfigure(row+1, weight=1)

    def upload_cor(self):
        for rowid in sorted(self.widgets.keys()):
            entry_widget = self.widgets[rowid]["num_seconds_correction"]
            new_value = entry_widget.get()
            print("%s: %s" % (rowid, new_value))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()"""

from tkinter import *

class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
                 relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for l in self.lists:
            l.yview(*args)

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: return apply(map, [None] + result)
        return result

    def index(self, index):
        self.lists[0].index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size()

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

if __name__ == '__main__':
    tk = Tk()
    Label(tk, text='MultiListbox').pack()
    mlb = MultiListbox(tk, (('Subject', 40), ('Sender', 20), ('Date', 10)))
    for i in range(1000):
        mlb.insert(END, ('Important Message: %d' % i, 'John Doe', '10/10/%04d' % (1900+i)))
    mlb.pack(expand=YES,fill=BOTH)
    tk.mainloop()

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()




from tkinter import *
from tkinter import ttk
root = Tk()

# Initialize our country "databases":
#  - the list of country codes (a subset anyway)
#  - a parallel list of country names, in the same order as the country codes
#  - a hash table mapping country code to population<
countrycodes = ('ar', 'au', 'be', 'br', 'ca', 'cn', 'dk', 'fi', 'fr', 'gr', 'in', 'it', 'jp', 'mx', 'nl', 'no', 'es', 'se', 'ch')
countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
cnames = StringVar(value=countrynames)
populations = {'ar':41000000, 'au':21179211, 'be':10584534, 'br':185971537, \
        'ca':33148682, 'cn':1323128240, 'dk':5457415, 'fi':5302000, 'fr':64102140, 'gr':11147000, \
        'in':1131043000, 'it':59206382, 'jp':127718000, 'mx':106535000, 'nl':16402414, \
        'no':4738085, 'es':45116894, 'se':9174082, 'ch':7508700}

# Names of the gifts we can send
gifts = { 'card':'Greeting card', 'flowers':'Flowers', 'nastygram':'Nastygram'}

# State variables
gift = StringVar()
sentmsg = StringVar()
statusmsg = StringVar()

# Called when the selection in the listbox changes; figure out
# which country is currently selected, and then lookup its country
# code, and from that, its population.  Update the status message
# with the new population.  As well, clear the message about the
# gift being sent, so it doesn't stick around after we start doing
# other things.
def showPopulation(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        code = countrycodes[idx]
        name = countrynames[idx]
        popn = populations[code]
        statusmsg.set("The population of %s (%s) is %d" % (name, code, popn))
    sentmsg.set('')

# Called when the user double clicks an item in the listbox, presses
# the "Send Gift" button, or presses the Return key.  In case the selected
# item is scrolled out of view, make sure it is visible.
#
# Figure out which country is selected, which gift is selected with the
# radiobuttons, "send the gift", and provide feedback that it was sent.
def sendGift(*args):
    idxs = lbox.curselection()
    if len(idxs)==1:
        idx = int(idxs[0])
        lbox.see(idx)
        name = countrynames[idx]
        # Gift sending left as an exercise to the reader
        sentmsg.set("Sent %s to leader of %s" % (gifts[gift.get()], name))

# Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# Create the different widgets; note the variables that many
# of them are bound to, as well as the button callback.
# Note we're using the StringVar() 'cnames', constructed from 'countrynames'
lbox = Listbox(c, listvariable=cnames, height=5)
lbl = ttk.Label(c, text="Send to country's leader:")
g1 = ttk.Radiobutton(c, text=gifts['card'], variable=gift, value='card')
g2 = ttk.Radiobutton(c, text=gifts['flowers'], variable=gift, value='flowers')
g3 = ttk.Radiobutton(c, text=gifts['nastygram'], variable=gift, value='nastygram')
send = ttk.Button(c, text='Send Gift', command=sendGift, default='active')
sentlbl = ttk.Label(c, textvariable=sentmsg, anchor='center')
status = ttk.Label(c, textvariable=statusmsg, anchor=W)

# Grid all the widgets
lbox.grid(column=0, row=0, rowspan=6, sticky=(N,S,E,W))
lbl.grid(column=1, row=0, padx=10, pady=5)
g1.grid(column=1, row=1, sticky=W, padx=20)
g2.grid(column=1, row=2, sticky=W, padx=20)
g3.grid(column=1, row=3, sticky=W, padx=20)
send.grid(column=2, row=4, sticky=E)
sentlbl.grid(column=1, row=5, columnspan=2, sticky=N, pady=5, padx=5)
status.grid(column=0, row=6, columnspan=2, sticky=(W,E))
c.grid_columnconfigure(0, weight=1)
c.grid_rowconfigure(5, weight=1)

# Set event bindings for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key
lbox.bind('<<ListboxSelect>>', showPopulation)
lbox.bind('<Double-1>', sendGift)
root.bind('<Return>', sendGift)

# Colorize alternating lines of the listbox
for i in range(0,len(countrynames),2):
    lbox.itemconfigure(i, background='#f0f0ff')

# Set the starting state of the interface, including selecting the
# default gift to send, and clearing the messages.  Select the first
# country in the list; because the <<ListboxSelect>> event is only
# generated when the user makes a change, we explicitly call showPopulation.
gift.set('card')
sentmsg.set('')
statusmsg.set('')
lbox.selection_set(0)
showPopulation()

root.mainloop()
