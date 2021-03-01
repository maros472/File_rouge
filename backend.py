import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY, titre text, auteur text, annee integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(titre,auteur,annee,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(titre,auteur,annee,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(titre="",auteur="",annee="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE titre=? OR annee=? OR auteur=? OR isbn=?", (titre,auteur,annee,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,titre,auteur,annee,isbn):
    conn = sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET titre=?, auteur=?, annee=?, isbn=? WHERE id=?", (titre,auteur,annee,isbn,id))
    conn.commit()
    conn.close()



connect()
#insert("the sea","Jhon Maro",1944,202558)
#insert("Mon pays","James blond",1950,203040)
#insert("La boite à merveilles","Denis",1980,203050)
#update(2,"the moon","marouane jebbari","1992","2020205")
#delete(3)
#print(view())
print(search(auteur="James blond"))

