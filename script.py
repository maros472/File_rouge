from tkinter import *
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(Titre_text.get(),Auteur_text.get(),Annee_text.get(),isbb_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(Titre_text.get(),Auteur_text.get(),Annee_text.get(),isbb_text.get())
    list1.delete(0,END)
    list1.insert(END,(Titre_text.get(),Auteur_text.get(),Annee_text.get(),isbb_text.get()))


window=Tk()

l1=Label(window,text="Titre")
l1.grid(row=0,column=0)

l2=Label(window,text="Auteur")
l2.grid(row=0,column=2)

l3=Label(window,text="Année")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

Titre_text=StringVar()
e1=Entry(window,textvariable=Titre_text)
e1.grid(row=0,column=1)

Auteur_text=StringVar()
e2=Entry(window,textvariable=Auteur_text)
e2.grid(row=0,column=3)

Annee_text=StringVar()
e3=Entry(window,textvariable=Annee_text)
e3.grid(row=1,column=1)

isbb_text=StringVar()
e4=Entry(window,textvariable=isbb_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="Voir tout", width=12,command=view_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Rechercher", width=12,command=search_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Ajouter", width=12,command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Supprimer", width=12)
b4.grid(row=6,column=3)

b5=Button(window,text="Fermer", width=12)
b5.grid(row=7,column=3)


window.mainloop()
