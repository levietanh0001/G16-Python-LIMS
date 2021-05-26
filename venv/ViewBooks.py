from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import mysql.connector
from PIL import ImageTk, Image
import pymysql

def viewBooks():

    root = Tk()
    root.title("Books")
    root.resizable(False, False)
    root.geometry("700x400")
    q = StringVar()
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()

    wrapper1 = Frame(root)
    wrapper2 = LabelFrame(root, text="")

    wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
    
    trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5))
    style = ttk.Style(trv)
    style.configure('Treeview', rowheight=30)

    trv.pack(side=LEFT)
    trv.place(x=0, y=0)
    trv.heading('#0', text='')
    trv.heading('#1', text='Book ID')
    trv.heading('#2', text='Title')
    trv.heading('#3', text='Author ID')
    trv.heading('#4', text='Author Name')
    trv.heading('#5', text='Copies')
    trv.column('#0', width=1, minwidth=1)
    trv.column('#1', width=50, minwidth=60)
    trv.column('#2', width=175, minwidth=200)
    trv.column('#3', width=50, minwidth=60)
    trv.column('#4', width=100, minwidth=100)
    trv.column('#5', width=25, minwidth=50)

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

    query = "select book_id, book_title, authors.author_id, authors.author_name, available_copies from books, authors where books.author_id = authors.author_id"
    cur.execute(query)
    rows = cur.fetchall()

    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i, tags='unchecked')

    root.mainloop()
