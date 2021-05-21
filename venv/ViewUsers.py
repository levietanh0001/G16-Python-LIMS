from tkinter import *
#import tkinter as tk
from tkinter import ttk
#from tkinter import messagebox, filedialog
#import mysql.connector
from PIL import ImageTk, Image
import pymysql



# def toggle2(event):
#     for i in trv.get_children():
#         trv.item(i, tags="unchecked")
#         toggleCheck(event)
#
# def toogleCheck(event):
#     rowid = trv.identify_row(event.y)
#     tag = trv.item(rowid, "tags")[0]
#     tags = list(trv.item(rowid, "tags"))
#     tags.remove(tag)
#     trv.item(rowid, tags=tags)
#     if tag == "checked":
#         trv.item(rowid, tags="unchecked")
#     else:
#         trv.item(rowid, tags="checked")
#
# def search():
#     q2 = q.get()
#     query = "select book_id, book_title, author_id, available_copies from books"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     update(rows)
#
# def clear():
#     query = "select book_id, book_title, author_id, available_copies from books"
#     cursor.execute(query)
#     rows = cursor.fetchall()
#     update(rows)

def viewUsers():

    root = Tk()
    root.title("Scrollable Tree View")
    root.resizable(False, False)
    root.geometry("700x400")
    q = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()

    wrapper1 = Frame(root)
    wrapper2 = LabelFrame(root, text="")
    # wrapper3 = LabelFrame(root, text="Book Details")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
    # wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

    trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5))
    style = ttk.Style(trv)
    style.configure('Treeview', rowheight=30)

    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='User ID')
    trv.heading('#2', text='User Name')
    trv.heading('#3', text='Date of Birth')
    trv.heading('#4', text='Phone Number')
    trv.heading('#5', text='Email')
    trv.column('#0', width=1, minwidth=1)
    trv.column('#1', width=25, minwidth=75)
    trv.column('#2', width=100, minwidth=100)
    trv.column('#3', width=120, minwidth=100)
    trv.column('#4', width=120, minwidth=100)
    trv.column('#5', width=120, minwidth=150)

        # vertical scroll bar
    yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=trv.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

        # horizontal scroll bar
    xscrollbar = ttk.Scrollbar(wrapper1, orient="horizontal", command=trv.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)

    trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar)

        # database details
    my_pass = "123321"
    my_db = "g16_db"

        # connect to database
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_db, port=3306)
    cur = con.cursor()
    book_table = "books"

    query = "select * from users"
    cur.execute(query)
    rows = cur.fetchall()

    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tags='unchecked')

    root.mainloop()
