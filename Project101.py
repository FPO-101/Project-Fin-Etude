from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import IntVar

root = Tk()
root.title('Matrice Calculation')
root.geometry('1000x600')
root.configure(bg='#fff')
#root.iconbitmap("se.png")
root.resizable(False, False)

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=80)

frame = Frame(root, width=400, height=400, bg='white')
frame.place(x=500, y=120)

hed = Label(frame, text='sign in', bg='white', fg='green', font=('Microsoft YaHei UI Light', 23, 'bold'))
hed.place(x=100, y=5)

photo1 = PhotoImage(file='hamza.png')
photo2 = PhotoImage(file='de.png')

row = IntVar()
col = IntVar()
copywrite_label = Label(root, text="Copyright © 2023 Maths. All Rights Reserved - FPO - Ouarzazate.")
copywrite_label.pack(side=BOTTOM, fill=X)
def input_row_column():
    global row, col
    Label(frame, text="Enter number of rows for matrix 1 :", bg="green", fg="white", borderwidth=3, relief="groove", font=("ariel", 10), width=35).place(x=5, y=200)
    Label(frame, text="Enter number of column for matrix 1 :", bg="green", fg="white", borderwidth=3, relief="groove", font=("ariel", 10), width=35).place(x=5, y=250)
    Entry(frame, width=4, textvariable=row, borderwidth=3, bg="green", fg="black", relief="solid").place(x=300, y=200)
    Entry(frame, width=4, textvariable=col, borderwidth=3, bg="green", fg="black", relief="solid").place(x=300, y=250)
    Button(frame, text="submit", bg="black", fg="white", width=5, ).place(x=320, y=280)

def create_back_button():
    back_button = Button(root, text="Back to Home Page", command=signin)
    back_button.place(x=0,y=0)
#jojo=copywrite_label.bind("<Button-1>", open_link)
def signin():
    username = user.get()
    password = passw.get()
    if username == "1" and password == '1':
        fpage = Frame(root, width=1000, height=1000, bg='green')
        fpage.place(x=0, y=0)
        # create the introduction text
        intro_text = "La diagonalisation de matrice est une méthode pour simplifier la résolution de systèmes linéaires en la transformant en une matrice diagonale. Les méthodes directes et itératives sont utilisées pour résoudre des équations linéaires dans divers domaines tels que l'ingénierie, les sciences physiques et les mathématiques financières."

        # create the label widget with custom font size and fixed position
        intro_label = Label(root, text=intro_text, font=("Arial", 16), wraplength=800, justify="center")
        intro_label.place(x=100, y=40)

        Label(fpage, text="diagonalisation d'un matrce ", fg='black', font=('calibri', 15, 'bold')).place(x=200, y=400)
        Button(fpage, text="Plus Detail", bg='black', border=2, fg='white', height=2,width=20, cursor='hand2', command=matrix_diagonal).place(x=255, y=450)
        #Button(root1, text='Submit', width=30, bg='green', fg='white')
        Label(fpage, text="resolution d' un systeme", fg='black', font=('calibri', 15, 'bold')).place(x=598, y=400)
        Button(fpage, text="plus detail", bg='black', border=2, fg='white', height=2,width=20,  cursor='hand2', command=method_sys_linear).place(x=649, y=450)
        copywrite_label = Label(root, text="Copyright © 2023 Maths. All Rights Reserved - ")
        copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)
        Label(fpage, image=photo2, width=200, height=200).place(x=225, y=190)
        Label(fpage, image=photo1, width=200, height=200).place(x=600, y=190)
    elif username != "admin" and password != 'admin':
        messagebox.showerror("Invallid", "Invallid username and password")
    elif username != "admin":
        messagebox.showerror("Invallid", "username non valid")
    elif password != 'admin':
        messagebox.showerror("Invallid", "password non valid")

# function to open the external link
def open_link():
    webbrowser.open_new("https://www.your-external-link.com")


# bind the label to the open_link function

#def fpo_name():
   # hamzaa = "FPO - Ouarzazate"




# bind the label to the open_link function
#copywrite_label.bind("<Button-1>", open_link)
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=300, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    passw.delete(0, 'end')

def on_leave(e):
    name = passw.get()
    if name == '':
        passw.insert(0, 'password')

passw=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11),)
passw.place(x=30,y=158)
passw.insert(0,'password')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)
Frame(frame,width=300,height=2,bg='black').place(x=25,y=180)

####################################
def creat_new_account():
    from tkinter import IntVar
    root1 = Toplevel(root)
    root1.geometry('500x450')
    root1.title("Registration Form")
    label_0 = Label(root1, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root1, text="Username", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(root1)
    entry_1.place(x=240, y=130)
    label_2 = Label(root1, text="Password", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(root1)
    entry_2.place(x=240, y=180)
    label_3 = Label(root1, text="Gender", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)
    var = IntVar()
    Radiobutton(root1, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
    Radiobutton(root1, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
    label_4 = Label(root1, text="Age:", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)
    entry_2 = Entry(root1)
    entry_2.place(x=240, y=280)
    Button(root1, text='Submit', width=30, bg='green', fg='white').place(x=180, y=380)
    # it is use for display the registration form on the window
    root1.mainloop()
    print("registration form  seccussfully created...")

def method_sys_linear():
    #root = Tk()
    fpage = Frame(root, width=1000, height=1000, bg='green')
    fpage.place(x=0, y=0)
    root.title("Resolution d' un Systeme")
    lab_1 = Label(root, text="Resolution D' Un Systeme", width=50, font=("bold", 20))
    lab_1.place(x=90, y=53)
    Button(root, text='Submit', width=20, bg='green', fg='white', height=5).place(x=590, y=465)
    Button(root, text='Submit', width=20, bg='green', fg='white', height=5).place(x=220, y=465)
    create_back_button()

def matrix_diagonal():
    #root = Tk()
    fpage = Frame(root, width=1000, height=1000, bg='green')
    fpage.place(x=0, y=0)
    root.title("Diagonalisation D'Matrix")
    lab_1 = Label(root, text="Diagonalisation D'Matrix", width=50, font=("bold", 20))
    lab_1.place(x=90, y=53)
    Button(root, text='Submit', width=20, bg='green', fg='white', height=5).place(x=590, y=465)
    Button(root, text='Submit', width=20, bg='green', fg='white', height=5).place(x=220, y=465)
    create_back_button()

Button(frame,width=25,pady=7,text='sign in',bg='green',fg='white',command=signin).place(x=90,y=200)
label=Label(frame,text="Create new Account",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=260)
Button(frame,text='sign up', width=6,border=0.4,bg='white',cursor='hand2',fg='#57a1f8',command=creat_new_account).place(x=200,y=260)

root.mainloop()