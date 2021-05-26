from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

def delU():
    # database details
    my_pass = "123321"
    my_db = "g16_db"

    # connect to database
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_db, port=3306)
    cur = con.cursor()

    user_id = userID.get()

    # error message if unable to delete book
    try:
        args = [user_id]
        cur.callproc('DeleteUserByID', args)
        con.commit()
        messagebox.showinfo('Success', "User Record Deleted Successfully")
    except:
        messagebox.showinfo("Failed to delete!")

    root.destroy()


def deleteUser():
    global root, con, cur, cv
    global userID

    root = Tk()
    root.title("Delete User")
    root.minsize(width=300, height=100)
    root.geometry("400x247")

    cv = Canvas(root)

    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    lb2 = Label(root, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    userID = Entry(root)
    userID.place(relx=0.2, rely=0.4, relwidth=0.7, relheight=0.1)

    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=delU)
    submit_button.place(relx=0.2, rely=0.85, relwidth=0.25, relheight=0.12)

    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.85, relwidth=0.25, relheight=0.12)

    root.mainloop()