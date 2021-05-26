from tkinter import *
from PIL import ImageTk, Image
import cryptography

from ViewBooks import *
from AddBook import *
from DeleteBook import *
from UpdateBook import *

from ViewUsers import *
from AddUser import *
from DeleteUser import *
from UpdateUser import *

from LendBook import *
from ReturnBook import *

from ViewBorrowers import *
from ViewBorrowerByName import *
from ViewBorrowerByBookName import *

# tkinter root
root = Tk()

# GUI window
root.title("Library Information Management System - Group 16")
root.geometry("1000x618")
root.wm_attributes('-alpha', 0.9)

# background image
bg_img = Image.open("lib_img2.jpg")
[img_width, img_height] = bg_img.size

# resize images while keeping aspect ratio Image.ANTIALIAS
bg_img = bg_img.resize((img_width, img_height), Image.ANTIALIAS)

# import image and turn to tk image
img = ImageTk.PhotoImage(bg_img)

# create canva
cv = Canvas(root)

# add img to canva
cv.create_image(500, 500, image=img)
cv.config(bg="grey", width=img_width, height=img_height)
cv.pack(expand=True, fill=BOTH)

heading_frame = Frame(root, bg="grey", bd=2)
heading_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)

heading_label = Label(heading_frame, text="G16 Library Information Management System",
                     bg='black', fg='white', font=('Segoe Script', 18))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

button1 = Button(root, text="View All Books", bg='white', fg='black', command=viewBooks)
button1.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)

button2 = Button(root, text="Add Book", bg='white', fg='black', command=addBook)
button2.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)


button3 = Button(root, text="Delete Book", bg='white', fg='black', command=deleteBook)
button3.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.1)

button4 = Button(root, text="Update Book", bg='white', fg='black', command=updateBook)
button4.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)

button5 = Button(root, text="View All Users", bg='white', fg='black', command=viewUsers)
button5.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

button6 = Button(root, text="Add User", bg='white', fg='black', command=addUser)
button6.place(relx=0.55, rely=0.3, relwidth=0.4, relheight=0.1)

button7 = Button(root, text="Delete User", bg='white', fg='black', command=deleteUser)
button7.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)

button8 = Button(root, text="Update User", bg='white', fg='black', command=updateUser)
button8.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.1)

button9 = Button(root, text="Lend Book", bg='white', fg='black', command=lendBook)
button9.place(relx=0.05, rely=0.75, relwidth=0.4, relheight=0.1)

button10 = Button(root, text="Return Book", bg='white', fg='black', command=returnBook)
button10.place(relx=0.05, rely=0.85, relwidth=0.4, relheight=0.1)

button11 = Button(root, text="View All Borrowers", bg='white', fg='black', command=viewBorrowers)
button11.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.1)

button12 = Button(root, text="View Borrowers By Name", bg='white', fg='black', command=viewBorrowerByName)
button12.place(relx=0.55, rely=0.75, relwidth=0.4, relheight=0.1)

button13 = Button(root, text="View Borrowers By Book Name", bg='white', fg='black', command=viewBorrowersByBookName)
button13.place(relx=0.55, rely=0.85, relwidth=0.4, relheight=0.1)

# initialize GUI
root.mainloop()