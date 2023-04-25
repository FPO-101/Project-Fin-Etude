#import sqlite
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import IntVar
from privacy_policy import *
from numpy import linalg
from scipy.linalg import qr
import psycopg2
from scipy import linalg as la
import warnings
#import numpy as np
import numpy as np
from tkinter.font import Font
from scipy.linalg import solve
from numpy.linalg import inv
from numpy.linalg import *
from numpy import array, zeros, diag, diagflat, dot
from scipy import linalg
from sympy import *
from fractions import Fraction
from decimal import Decimal

root = Tk()
root.title("DiagTriWeb")
root.geometry('1000x600')
root.configure(bg='#fff')
root.resizable(False, False)
right_frame=Frame(root,bg="white")

left_frame=Frame(root,bg="white")
matrix_frame=Frame(left_frame,bg="white")
methode_direct_frame=Frame(left_frame,bg="black")
methode_itera_frame=Frame(left_frame,bg="black")
determinant_frame=Frame(left_frame,bg="black")
img = PhotoImage(file='vv.png')
Label(root, image=img, bg='white').place(x=0, y=0)

frame = Frame(root, width=400, height=400, bg='white')
frame.place(x=500, y=160)

hed = Label(frame, text='Bienvenue', bg='white', fg='#00a896', font=('Microsoft YaHei UI Light', 23, 'bold'))
hed.place(x=95, y=0)
hed = Label(frame, text='Pour accéder au contenu, connectez-vous', bg='white', fg='black', font=("Helvetica",10))
hed.place(x=62, y=50)
copywrite_label = Label(root, text="© 2023 Tous droits réservés- FPO Ouarzazate", bg='white')
copywrite_label.place(x=370, y=580)
photo1 = PhotoImage(file='hamza.png')
photo2 = PhotoImage(file='de.png')

row = IntVar()
col = IntVar()

def create_back_button():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15), command=signin)
    back_button.place(relx=0.1, rely=0.1, anchor="center")

def create_back_button_2():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15), command=signin)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def create_back_button_2():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15), command=signin)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def create_back_button_3():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15), command=signin)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def remove_back_button():
    global back_button_1
    back_button_1.destroy()
########################################" Login Verification ###########################################################

def trigonalisation_input_row_column():
    from random import randint, choice
    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(x=0, y=0)
    #create_back_button_Home()
    input_frame = Frame(root, bg="#00a896")
    input_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Declare verify_label as a global variable
    global verify_label

    # Declare solution as a global variable
    global solution

    # Define a function to generate a new verification expression
    def generate_expression():
        global solution, verify_label
        a = randint(1, 10)
        b = randint(1, 10)
        op = choice(['+', '-', '*'])
        expression = f"{a} {op} {b} = ?"
        solution = eval(f"{a} {op} {b}")
        verify_label.config(text=expression)

    title_label = Label(input_frame, text="Vérification - Vous n'êtes pas un robot", fg="white", bg="#00a896",
                        font=("ariel", 20, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Créer une étiquette pour l'expression de vérification
    verify_label = Label(input_frame, text="", fg="white", bg="#00a896", font=("ariel", 15))
    verify_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    # Générer l'expression et la solution de vérification initiale
    generate_expression()
    # Créer un bouton pour générer une nouvelle expression de vérification
    reset_button = Button(input_frame, text="Réinitialiser", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),
                          command=lambda: (verify_entry.delete(0, END), generate_expression()))
    reset_button.grid(row=2, column=1, padx=10, pady=10)
    # Create an entry for the user to enter the solution
    verify_entry = Entry(input_frame, width=10, font=("ariel", 15))
    verify_entry.grid(row=1, column=1, padx=10, pady=10)

    def submit_dimensions():
        global solution
        # Vérifier si l'utilisateur a saisi la bonne solution à l'expression de vérification
        if int(verify_entry.get()) == solution:
            # Passez les dimensions de la matrice au menu principal de diagonalisation
            beinvenu()
        else:
            # Afficher un message d'erreur si la solution est incorrecte
            messagebox.showerror("Erreur", "Veuillez résoudre l'expression mathématique pour continuer.")
            # Générer une nouvelle expression de vérification et une solution
            generate_expression()
    # Créer un bouton pour soumettre les dimensions de la matrice
    submit_button = Button(input_frame, text="Valide", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),
                           command=submit_dimensions)
    submit_button.grid(row=2, column=0, padx=10, pady=10)
    # Ajouter un libellé d'avis de droit d'auteur
    copywrite_label = Label(input_frame, text="© 2023 Tous droits réservés.", fg="white", bg="#00a896",
                            font=("ariel", 10))
    copywrite_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    # Créer le bouton de sortie
    exit_button = Button(root, text="Quitter", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),
                         command=root.destroy)
    exit_button.place(relx=0.5, rely=0.7, anchor="center")

def beinvenu():
    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(x=0, y=0)
    # créer le texte d'introduction
    intro_text = "La triangularisation et la diagonalisation sont deux techniques courantes utilisées en algèbre linéaire , pour transformer une matrice en une forme plus simple."
    # créer le widget d'étiquette avec une taille de police personnalisée et une position fixe
    intro_label = Label(root, text=intro_text, font=("Arial", 16), wraplength=800, justify="center")
    intro_label.place(x=100, y=40)
    Label(fpage, text="        Diagonalisation      ", fg='black', font=('calibri', 15, 'bold')).place(x=231, y=400)
    Button(fpage, text="Plus Detail", bg='#80ffdb', border=2, fg='#05668d', height=2, width=20,cursor='hand2', command=main_menu_diagonal).place(x=255, y=450)
    Label(fpage, text="       Triangularisation     ", fg='black', font=('calibri', 15, 'bold')).place(x=598, y=400)
    Button(fpage, text="Plus Detail", bg='#80ffdb', border=2, fg='#05668d', height=2, width=20,cursor='hand2', command=trigonalisation_main_menu_diagonal).place(x=649, y=450)
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10), fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)
    Label(fpage, image=photo2, width=200, height=200).place(x=225, y=190)
    Label(fpage, image=photo1, width=200, height=200).place(x=600, y=190)
def signin():
    username = user.get()
    password = passw.get()
    if username == "admin" and password == 'admin':
        fpage = Frame(root, width=1000, height=1000, bg='#00a896')
        fpage.place(x=0, y=0)
        trigonalisation_input_row_column()
    elif username != "admin" and password != 'admin':
        messagebox.showerror("Invallid", "Invallid nom d'utilisateur and password")
    elif username != "admin":
        messagebox.showerror("Invallid", "nom d'utilisateur non valid")
    elif password != 'admin':
        messagebox.showerror("Invallid", "Mot de passe non valid")
    else:
        messagebox.showerror("Invallid", "Mot de passe non valid")
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'username')

user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=95)
user.insert(0, 'Nom de utilisateur')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=300, height=2, bg='black').place(x=25, y=119)

def on_enter(e):
    passw.delete(0, 'end')

def on_leave(e):
    name = passw.get()
    if name == '':
        passw.insert(0, 'Mot de passe')

passw=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11),)
passw.place(x=30,y=158)
passw.insert(0,'Mot de passe')
passw.bind('<FocusIn>',on_enter)
passw.bind('<FocusOut>',on_leave)
Frame(frame,width=300,height=2,bg='black').place(x=25,y=180)

####################################

def creat_new_account():
    global entry_1, entry_2, entry_3, gender_var
    root1 = Toplevel(root)
    root1.geometry('500x450')
    root1.title("Formulaire d'inscription")
    label_0 = Label(root1, text="Formulaire d'inscription", width=20, fg='#00a896', font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root1, text="Nom d'utilisateur", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(root1)
    entry_1.place(x=240, y=130)
    label_2 = Label(root1, text="Mot de passe", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(root1)
    entry_2.place(x=240, y=180)
    label_3 = Label(root1, text="Genre", width=20, font=("bold", 10))
    label_3.place(x=70, y=230)
    gender_var = IntVar()
    Radiobutton(root1, text="Mâle", padx=5, variable=gender_var, value=1).place(x=235, y=230)
    Radiobutton(root1, text="Femelle", padx=20, variable=gender_var, value=2).place(x=290, y=230)
    label_4 = Label(root1, text="Âge:", width=20, font=("bold", 10))
    label_4.place(x=70, y=280)
    entry_3 = Entry(root1)
    entry_3.place(x=240, y=280)
    Button(root1, text='Submit', width=30, bg='#05668d', fg='white', command=submit_form).place(x=180, y=380)
    root1.mainloop()
    print("formulaire d'inscription créé avec soin...")

def submit_form():
    # Récupérer les données du formulaire à partir de l'interface graphique de Tkinter
    username = entry_1.get()
    password = entry_2.get()
    gender = "Male" if get_gender() == 1 else "Female"
    age = entry_3.get()

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="database-1-pfo.cp6yqwinhmvh.eu-central-1.rds.amazonaws.com",
        database="database-1-pfo",
        user="hamza2016",
        password="hamza2016",
        port='5432'
    )

    # Ouvrir un curseur pour effectuer des opérations de base de données
    cursor = conn.cursor()

    # Exécutez une instruction INSERT pour insérer les données du formulaire dans la base de données
    cursor.execute(
        "INSERT INTO users (username, password, gender, age) VALUES (%s, %s, %s, %s)",
        (username, password, gender, age)
    )

    # Valider la transaction
    conn.commit()

    # Fermez le curseur et la connexion
    cursor.close()
    conn.close()

    # Afficher un message de réussite à l'utilisateur
    messagebox.showinfo("Success", "Account created successfully!")

    # Appelez la fonction display_account_info() pour afficher les informations de compte de l'utilisateur
    display_account_info()

def display_account_info():
    global entry_1
    # Connectez-vous à la base de données PostgreSQL
    conn = psycopg2.connect(
        host="database-1-pfo.cp6yqwinhmvh.eu-central-1.rds.amazonaws.com",
        database="postgres",
        user="078790301136",
        password="hamza2016",
        port = '5432'
    )

    # Ouvrir un curseur pour effectuer des opérations de base de données
    cursor = conn.cursor()

    # Exécuter une instruction SELECT pour récupérer les informations de compte de l'utilisateur
    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (entry_1.get(),)
    )

    # Récupérer les informations de compte de l'utilisateur à partir de la base de données
    account_info = cursor.fetchone()

    # Fermez le curseur et la connexion
    cursor.close()
    conn.close()

    # Afficher les informations de compte de l'utilisateur à l'utilisateur
    messagebox.showinfo(
        "Account Information",
        f"Username: {account_info[1]}\nGender: {account_info[3]}\nAge: {account_info[4]}"
    )

def get_gender():
    global gender_var
    return gender_var.get()
"""diagonalisation_input_row_column"""
result_frame=Frame(root,bg="#5F9EA0")
right_frame = Frame(root, bg="yellow")
def frame_destroy():
    global middle_frame
    middle_frame.destroy()
    middle_frame=Frame(root,bg="#02c39a")
    global right_frame
    right_frame.destroy()
    right_frame = Frame(root, bg="#02c39a")
    global result_frame
    result_frame.destroy()
    result_frame = Frame(root, bg="red") #Contole Result to change the color of background !!
def remove_back_button():
    global back_button
    back_button.destroy()
#########################################    Diagonalisatio Des Matrices    ############################################
middle_frame=Frame(root,bg="#02c39a")
l1 = None
cl1 = None
def create_back_button_2():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),command=main_menu_diagonal)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def create_back_button_Home():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),command=beinvenu)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
# Function to display the main menu

def main_menu_diagonal():
    global dic1
    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    frame_destroy()
    create_back_button_Home()
    # Créer une étiquette pour le menu principal
    main_menu_label = Label(root, text="Diagonalisation de matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    main_menu_label.place(relx=0.5, rely=0.3, anchor="center")
    # Créer un bouton pour entrer dans une matrice
    matrix_button = Button(root, text="Entrer une matrice", bg="#5F9EA0", fg="white", width=20, font=("ariel", 15),command=diagonalisation_grid)
    matrix_button.place(relx=0.5, rely=0.5, anchor="center")
    # Créer un bouton pour quitter le programme
    exit_button = Button(root, text="Quitter", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15), command=root.destroy)
    exit_button.place(relx=0.5, rely=0.7, anchor="center")
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10),
                            fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)
def create_back_button_14():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),command=main_menu_diagonal)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def diagonalisation_grid():
    global dic1
    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    frame_destroy()
    create_back_button_14()
    # Créer une étiquette pour l'entrée de la matrice
    matrix_label = Label(root, text="Entrez une matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    matrix_label.place(relx=0.5, rely=0.2, anchor="center")
    # Créer une entrée pour le nombre de lignes
    row_label = Label(root, text="Nombre de lignes (2-4):", fg="white", bg="#00a896", font=("ariel", 15))
    row_label.place(relx=0.35, rely=0.4, anchor="center")
    row_entry = Entry(root, width=10, font=("ariel", 15))
    row_entry.place(relx=0.6, rely=0.4, anchor="center")
    # Créer une entrée pour le nombre de colonnes
    col_label = Label(root, text="Nombre de colonnes (2-4):", fg="white", bg="#00a896", font=("ariel", 15))
    col_label.place(relx=0.35, rely=0.5, anchor="center")
    col_entry = Entry(root, width=10, font=("ariel", 15))
    col_entry.place(relx=0.6, rely=0.5, anchor="center")
    # Créer un bouton pour soumettre les dimensions de la matrice
    submit_button = Button(root, text="Suivant", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),command=lambda:check_input())
    submit_button.place(relx=0.5, rely=0.6, anchor="center")
    # Créer un bouton pour revenir au menu principal
    main_menu_button = Button(root, text="Menu principal", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),  command=beinvenu)
    main_menu_button.place(relx=0.5, rely=0.8, anchor="center")
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10),
                            fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)

    def check_input():
        rows = int(row_entry.get())
        cols = int(col_entry.get())
        if rows < 2 or cols < 2 or rows > 4 or cols > 4:
            messagebox.showerror("Erreur", "Le nombre de lignes et de colonnes doit être entre 2 et 4.")
            return False
        elif rows != cols:
            messagebox.showerror("Erreur", "Le nombre de lignes doit être égal au nombre de colonnes.")
            return False
        else:
            command = lambda: matrix_input(row_entry.get(), col_entry.get())
            submit_button.config(command=command)


###########################################################################################################################
# Fonction pour afficher l'entrée de la matrice
def create_back_button_4():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),command=diagonalisation_grid)
    back_button.place(relx=0.1, rely=0.1, anchor="center")

# Fonction pour entrer une matrice et effectuer des opérations dessus
def matrix_input(rows, cols):
    # Convertir l'entrée en nombres entiers
    rows = int(rows)
    cols = int(cols)
    # Créer une liste pour stocker les valeurs de la matrice
    matrix_values = [[0 for j in range(cols)] for i in range(rows)]
    # Créer un cadre pour l'interface graphique
    fpage = Frame(root, width=800, height=600, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    create_back_button_4()
    # Créer une étiquette pour l'entrée de la matrice
    matrix_label = Label(fpage, text="Entrez les valeurs de la matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    matrix_label.place(relx=0.5, rely=0.1, anchor="center")
    # Créer des widgets d'entrée pour chaque élément de la matrice
    x_offset = 0.05 if cols % 2 == 0 else 0
    y_offset = 0.1 if rows % 2 == 0 else 0
    for i in range(rows):
        for j in range(cols):
            matrix_entry = Entry(fpage, width=5, font=("ariel", 15))
            x_pos = (j - cols//2) * 50 / cols
            y_pos = (i - rows//2) * 30 / rows
            matrix_entry.place(relx=0.5+x_pos/100+x_offset, rely=0.4+y_pos/100+y_offset, anchor="center")
            matrix_values[i][j] = matrix_entry
    # Créer un bouton pour soumettre les dimensions de la matrice
    submit_button = Button(root, text="Suivant", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),command=lambda: check_diagonalizability(matrix_values))
    submit_button.place(relx=0.5, rely=0.7, anchor="center")
    # Créer un bouton pour revenir au menu principal
    main_menu_button = Button(root, text="Menu principal", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),  command=beinvenu)
    main_menu_button.place(relx=0.5, rely=0.9, anchor="center")
    # Définir une fonction pour appliquer un format d'entrée cohérent
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10),
                            fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)

    def enforce_input_format(event):
        """
        Enforces consistent format for matrix input.
        """
        widget = event.widget
        # Obtenir le texte actuel dans le widget
        text = widget.get()
        # Supprimez tous les espaces de début ou de fin
        text = text.strip()
        # Remplacer tous les espaces consécutifs par un seul espace
        text = " ".join(text.split())
        # Définissez le texte du widget sur le texte formaté
        widget.delete(0, END)
        widget.insert(0, text)

    # Liez la fonction enhance_input_format aux widgets d'entrée de matrice+
    for i in range(rows):
        for j in range(cols):
            matrix_entry = matrix_values[i][j]
            matrix_entry.bind("<FocusOut>", enforce_input_format)

    # Set focus to the first matrix entry widget
    matrix_values[0][0].focus()

    def check_diagonalizability(matrix_values):
        # Convertir les valeurs de la matrice en un tableau numpy
        matrix = np.array([[float(matrix_values[i][j].get()) for j in range(cols)] for i in range(rows)])

        # Vérifier si la matrice est diagonalisable
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        if len(set(eigenvalues)) == len(eigenvalues):
            # Appliquer la fonction de diagonalisation à la matrice d'entrée
            diagonalisation_cmd(matrix_values)
        else:
            # Afficher le message d'erreur
            messagebox.showerror("Erreur", "La matrice ne peut pas être diagonalisée.")
#-----------------------------------------------------------------------------------------------------------------------
# Fonction pour calculer les vecteurs propres d'une matrice
def vecteur_propre(matrix):
    matrix_np = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(matrix_np)
    eigenvectors = [[round(vec.real, 2) for vec in eigenvectors[:, i]] for i in range(len(eigenvectors))]
    return eigenvectors
# Fonction pour calculer les valeurs propres d'une matrice
def valeur_propre(matrix):
    matrix_np = np.array(matrix)
    eigenvalues = np.linalg.eigvals(matrix_np)
    eigenvalues = [[round(val.real, 2)] for val in eigenvalues]
    return eigenvalues

# Fonction pour calculer la matrice diagonale d'une matrice
def diago_of_matrix(matrix):
    matrix_np = np.array(matrix)
    eigenvalues, eigenvectors = np.linalg.eig(matrix_np)
    diagonal = np.zeros_like(matrix_np)
    for i in range(len(eigenvalues)):
        diagonal[i][i] = eigenvalues[i]
    return diagonal.tolist()
def create_back_button_5(rows, cols):
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),
                         command=lambda: matrix_input(rows, cols))
    back_button.place(relx=0.1, rely=0.1, anchor="center")
# Fonction pour effectuer les calculs de diagonalisation et afficher les résultats
def diagonalisation_cmd(matrix_values):
    global dic1
    # Récupérer les valeurs de la matrice à partir des champs de saisie
    matrix = [[float(matrix_values[i][j].get()) for j in range(len(matrix_values[0]))] for i in range(len(matrix_values))]
    # Calculer la diagonale, les valeurs propres et les vecteurs propres de la matrice
    diagonal = diago_of_matrix(matrix)
    eigenvalues = valeur_propre(matrix)
    eigenvectors = vecteur_propre(matrix)
    # Supprimer le contenu précédent de la fenêtre
    for widget in root.winfo_children():
        widget.destroy()
    fpage = Frame(root, width=1000, height=600, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    # Créer une étiquette pour la matrice diagonale
    diagonal_label = Label(root, text="Matrice diagonale:", fg="white", bg="#5F9EA0", font=("ariel", 25))
    diagonal_label.place(relx=0.2, rely=0.2, anchor="center")
    # Afficher la matrice diagonale
    for i in range(len(diagonal)):
        for j in range(len(diagonal[0])):
            diagonal_entry = Entry(root, width=10, font=("ariel", 15))
            diagonal_entry.insert(END, diagonal[i][j])
            diagonal_entry.config(state=DISABLED)
            diagonal_entry.place(relx=0.2+j*(0.6/len(diagonal[0])), rely=0.3+i*(0.6/len(diagonal)), anchor="center")

    # Créer une étiquette pour les valeurs propres
    eigenvalue_label = Label(root, text="Valeurs propres:", fg="white", bg="#5F9EA0", font=("ariel", 25))
    eigenvalue_label.place(relx=0.2, rely=0.7, anchor="center")

    # Afficher les valeurs propres
    for i in range(len(eigenvalues)):
        eigenvalue_entry = Entry(root, width=10, font=("ariel", 15))
        eigenvalue_entry.insert(END, eigenvalues[i][0])
        eigenvalue_entry.config(state=DISABLED)
        eigenvalue_entry.place(relx=0.2, rely=0.8+i*(0.1/len(eigenvalues)), anchor="center")

    # Créer une étiquette pour les vecteurs propres
    eigenvector_label = Label(root, text="Vecteurs propres:", fg="white", bg="#5F9EA0", font=("ariel", 25))
    eigenvector_label.place(relx=0.6, rely=0.7, anchor="center")

    # Afficher les vecteurs propres
    for i in range(len(eigenvectors)):
        for j in range(len(eigenvectors[0])):
            eigenvector_entry = Entry(root, width=10, font=("ariel", 15))
            eigenvector_entry.insert(END, eigenvectors[i][j])
            eigenvector_entry.config(state=DISABLED)
            eigenvector_entry.place(relx=0.6+j*(0.6/len(eigenvectors[0])), rely=0.8+i*(0.1/len(eigenvectors)), anchor="center")

    # Créer un bouton pour revenir au menu principal
    main_menu_button = Button(root, text="Menu principal", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15), command=beinvenu)
    main_menu_button.place(relx=0.5, rely=0.95, anchor="center")

    # Enregistrer les valeurs de la matrice dans une variable globale
    dic1 = matrix_values
##################################### ---------- TRIANGULARISATION ---------- ##########################################

def create_back_button_8():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),
                         command=beinvenu)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def trigonalisation_main_menu_diagonal():

    global dic1
    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    frame_destroy()

    # Créer une étiquette pour le menu principal
    main_menu_label = Label(root, text="Trigonalisation de matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    main_menu_label.place(relx=0.5, rely=0.3, anchor="center")
    # Créer un bouton pour entrer dans une matrice
    create_back_button_8()
    matrix_button = Button(root, text="Entrer une matrice", bg="#5F9EA0", fg="white", width=20, font=("ariel", 15),command=trigonalisation_grid)
    matrix_button.place(relx=0.5, rely=0.5, anchor="center")
    # Créer un bouton pour quitter le programme
    exit_button = Button(root, text="Quitter", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15), command=root.destroy)
    exit_button.place(relx=0.5, rely=0.7, anchor="center")
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10),
                            fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)

def create_back_button_9():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),
                         command=trigonalisation_main_menu_diagonal)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def trigonalisation_grid():
    global dic1

    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    frame_destroy()
    # Créer une étiquette pour l'entrée de la matrice
    matrix_label = Label(root, text="Entrez une matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    matrix_label.place(relx=0.5, rely=0.2, anchor="center")
    create_back_button_9()
    # Créer une entrée pour le nombre de lignes
    row_label = Label(root, text="Nombre de lignes (2-4):", fg="white", bg="#00a896", font=("ariel", 15))
    row_label.place(relx=0.35, rely=0.4, anchor="center")
    row_entry = Entry(root, width=10, font=("ariel", 15))
    row_entry.place(relx=0.6, rely=0.4, anchor="center")
    # Créer une entrée pour le nombre de colonnes
    col_label = Label(root, text="Nombre de colonnes (2-4):", fg="white", bg="#00a896", font=("ariel", 15))
    col_label.place(relx=0.35, rely=0.5, anchor="center")
    col_entry = Entry(root, width=10, font=("ariel", 15))
    col_entry.place(relx=0.6, rely=0.5, anchor="center")

    # Créer un bouton pour soumettre les dimensions de la matrice
    submit_button = Button(root, text="Suivant", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),command=lambda:trigonalisation_check_input())
    submit_button.place(relx=0.5, rely=0.6, anchor="center")
    # Créer un bouton pour revenir au menu principal
    main_menu_button = Button(root, text="Menu principal", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),  command=beinvenu)
    main_menu_button.place(relx=0.5, rely=0.8, anchor="center")
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10),
                            fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)

    def trigonalisation_check_input():
        rows = int(row_entry.get())
        cols = int(col_entry.get())
        if rows < 2 or cols < 2 or rows > 4 or cols > 4:
            messagebox.showerror("Erreur", "Le nombre de lignes et de colonnes doit être entre 2 et 4.")
            return False
        elif rows != cols:
            messagebox.showerror("Erreur", "Le nombre de lignes doit être égal au nombre de colonnes.")
            return False
        else:
            command = lambda: trigonalisation_matrix_input(row_entry.get(), col_entry.get())
            submit_button.config(command=command)



def is_trigonally_similar(matrix):
    """
    Checks if a matrix can be trigonally similar to an upper triangular matrix.
    """
    matrix = np.array(matrix)  # Convertir la matrice en un tableau numpy
    eigenvalues, eigenvectors = np.linalg.eig(matrix)  # Calculer les valeurs propres et les vecteurs propres de la matrice
    if not all(np.isreal(eigenvalues)):
        return False  # Si la matrice a des valeurs propres complexes, elle n'est pas trigonalement similaire
    if not all(np.linalg.matrix_rank(eigenvectors[:, :i+1]) == i+1 for i in range(matrix.shape[0])):
        return False  # Si les vecteurs propres ne couvrent pas tout l'espace, la matrice n'est pas trigonalement similaire
    return True

def is_trigonally_diagonalizable(matrix):
    """
    Checks if a matrix is trigonally diagonalizable.
    """
    matrix = np.array(matrix)
    triangular_matrix, _ = np.linalg.qr(matrix)
    if not np.allclose(matrix, np.dot(triangular_matrix, np.dot(triangular_matrix.T, matrix))):
        return False
    return True

def verify_trigonalisation(matrix):
    """
    Verifies if a matrix has been trigonalized.
    """
    matrix = np.array(matrix)
    triangular_matrix, _ = np.linalg.qr(matrix)
    if not is_trigonally_similar(matrix) or not is_trigonally_diagonalizable(matrix):
        messagebox.showerror("Erreur", "La matrice n'a pas été trigonalisée.")
        return
    # La matrice a été trigonalisée avec succès
    # Faire quelque chose avec la matrice triangulaire
    # ...
    # Fonction pour obtenir l'entrée d'une matrice et afficher un bouton pour vérifier si la matrice est diagonalisable

def create_back_button_10():
    back_button = Button(root, text="Retour", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),
                         command=trigonalisation_grid)
    back_button.place(relx=0.1, rely=0.1, anchor="center")
def trigonalisation_matrix_input(rows, cols):
    # Convert the input to integers
    rows = int(rows)
    cols = int(cols)

    # Créer une liste pour stocker les valeurs de la matrice
    matrix_values = [[0 for j in range(cols)] for i in range(rows)]

    # Créer un cadre pour l'interface graphique
    fpage = Frame(root, width=800, height=600, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")
    create_back_button_10()
    # Créer une étiquette pour l'entrée de la matrice
    matrix_label = Label(fpage, text="Entrez les valeurs de la matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    matrix_label.place(relx=0.5, rely=0.1, anchor="center")

    # Créer des widgets d'entrée pour chaque élément de la matrice
    x_offset = 0.05 if cols % 2 == 0 else 0
    y_offset = 0.1 if rows % 2 == 0 else 0
    for i in range(rows):
        for j in range(cols):
            matrix_entry = Entry(fpage, width=5, font=("ariel", 15))
            x_pos = (j - cols//2) * 50 / cols
            y_pos = (i - rows//2) * 30 / rows
            matrix_entry.place(relx=0.5+x_pos/100+x_offset, rely=0.4+y_pos/100+y_offset, anchor="center")
            matrix_values[i][j] = matrix_entry
    # Créer un bouton pour soumettre les dimensions de la matrice
    submit_button = Button(root, text="Suivant", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15),command=lambda: check_triangularizability(matrix_values))
    submit_button.place(relx=0.5, rely=0.7, anchor="center")
    # Créer un bouton pour revenir au menu principal
    main_menu_button = Button(root, text="Menu principal", bg="#5F9EA0", fg="white", width=15, font=("ariel", 15),  command=beinvenu)
    main_menu_button.place(relx=0.5, rely=0.9, anchor="center")
    # Définir une fonction pour appliquer un format d'entrée cohérent
    copywrite_label = Label(root, text="©2023 Tous droits réservés - FPO Ouarzazate", bg='#00a896', font=("ariel", 10),
                            fg="white")
    copywrite_label.place(x=root.winfo_width() // 2 - 150, y=580)
    def enforce_input_format(event):
        """
        Enforces consistent format for matrix input.
        """
        widget = event.widget
        # Obtenir le texte actuel dans le widget
        text = widget.get()
        # Supprimez tous les espaces de début ou de fin
        text = text.strip()
        # Remplacer tous les espaces consécutifs par un seul espace
        text = " ".join(text.split())
        # Définissez le texte du widget sur le texte formaté
        widget.delete(0, END)
        widget.insert(0, text)

    # Liez la fonction enhance_input_format aux widgets d'entrée de matrice
    for i in range(rows):
        for j in range(cols):
            matrix_entry = matrix_values[i][j]
            matrix_entry.bind("<FocusOut>", enforce_input_format)

    # Set focus to the first matrix entry widget
    matrix_values[0][0].focus()

    def check_triangularizability(matrix_values):
        # Convertir les valeurs de la matrice en un tableau numpy
        matrix = np.array([[float(matrix_values[i][j].get()) for j in range(cols)] for i in range(rows)])

        # Vérifier si la matrice peut être triangularisée
        if np.linalg.matrix_rank(matrix) == rows:
            # Appliquer la fonction de trigonalisation à la matrice d'entrée
            trigonalisation_cmd(matrix_values)
        else:
            # Afficher le message d'erreur
            messagebox.showerror("Erreur", "La matrice ne peut pas être triangularisée.")
def trigonalisation_cmd(matrix_values):
    global results
    # Convertir les valeurs de la matrice en un tableau numpy
    matrix = np.array([[float(entry.get()) for entry in row] for row in matrix_values])
    # Calculer la trigonalisation de la matrice
    Q, T = la.qr(matrix)
    # Enregistrez les matrices résultantes pour une utilisation ultérieure
    results = (Q, T)
    # Créer une nouvelle fenêtre pour les résultats
    result_window = Toplevel(root)
    result_window.configure(bg='#00a896')
    result_window.title("Trigonalisation de la matrice")
    # Créer une étiquette pour les résultats
    result_label = Label(result_window, text="Trigonalisation de la matrice", fg="white", bg="#2E86C1",
                         font=("Arial", 25))
    result_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
    # Create a frame for the Q and T matrices
    matrix_frame = Frame(result_window, bg="#F7DC6F")
    matrix_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    # Créer une étiquette pour la matrice Q
    Q_label = Label(matrix_frame, text="Q =", font=("Arial", 14), bg="#F7DC6F")
    Q_label.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="e")
    # Créer une étiquette pour les valeurs de la matrice Q
    Q_values_label = Label(matrix_frame,
                           text="\n".join("\t".join(f"{round(entry, 3):.3f}" for entry in row) for row in Q),
                           font=("Arial", 14), bg="#F7DC6F")
    Q_values_label.grid(row=0, column=1, pady=10, sticky="w")

    # Créer une étiquette pour la matrice T
    T_label = Label(matrix_frame, text="T =", font=("Arial", 14), bg="#F7DC6F")
    T_label.grid(row=1, column=0, padx=(0, 10), pady=10, sticky="e")

    # Créer une étiquette pour les valeurs de la matrice T
    T_values_label = Label(matrix_frame,
                           text="\n".join("\t".join(f"{round(entry, 3):.3f}" for entry in row) for row in T),
                           font=("Arial", 14), bg="#F7DC6F")
    T_values_label.grid(row=1, column=1, pady=10, sticky="w")

    # Créer un bouton pour revenir au menu principal
    main_menu_button = Button(result_window, text="Menu principal", bg="#5F9EA0", fg="white", width=15,
                              font=("Arial", 15),
                              command=lambda: [result_window.destroy(), beinvenu()])
    main_menu_button.grid(row=2, column=0, columnspan=2, pady=20)
    # Définissez les poids des lignes et des colonnes pour vous assurer que le cadre de la matrice s'agrandit pour remplir la fenêtre
    result_window.rowconfigure(1, weight=1)
    result_window.columnconfigure(0, weight=1)
#################################  politique de confidentialité ######################################################################
def quit_program():
    if root.winfo_exists():
        root.destroy()

def main_menu_triangular():
    global dic1, n_rows, n_cols  # Ajouter n_rows et n_cols à la portée globale

    fpage = Frame(root, width=1000, height=1000, bg='#00a896')
    fpage.place(relx=0.5, rely=0.5, anchor="center")

    frame_destroy()

    # Créer une étiquette pour le menu principal
    main_menu_label = Label(root, text="Triangularisation de matrice", fg="white", bg="#5F9EA0", font=("ariel", 25))
    main_menu_label.place(relx=0.5, rely=0.3, anchor="center")

    # Définissez n_rows et n_cols avec les valeurs appropriées
    n_rows = 3
    n_cols = 3

    # Créer un bouton pour entrer dans une matrice
    matrix_button = Button(root, text="Entrer une matrice", bg="#5F9EA0", fg="white", width=20, font=("ariel", 15),
                           command=triangulation_grid)
    matrix_button.place(relx=0.5, rely=0.5, anchor="center")

    # Créer un bouton pour quitter le programme
    exit_button = Button(root, text="Quitter", bg="#5F9EA0", fg="white", width=10, font=("ariel", 15), command=root.destroy)
    exit_button.place(relx=0.5, rely=0.7, anchor="center")



Button(frame,width=25,pady=7,text='login',bg="#02c39a",fg='white',command=signin).place(x=90,y=200)
label=Label(frame,text="Créer un nouveau compte",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=55,y=260)
Button(frame,text="s'inscrire", width=6,border=0.4,bg='white',cursor='hand2',fg='#05668d',command=creat_new_account).place(x=200,y=260)
# Fenêtre Politique de confidentialité
def privacy_window():
    privacy_win = Toplevel(root)
    privacy_win.title("Politique de confidentialité")
    privacy_win.geometry("600x500")
    privacy_win.resizable(False, False)
    privacy_win.configure(bg="#f5f5f5")

    privacy_text = """Politique de confidentialité:

Nous prenons votre vie privée au sérieux et nous nous engageons à protéger vos informations personnelles. Cette politique de confidentialité explique comment nous collectons, utilisons et protégeons vos informations personnelles lorsque vous utilisez notre application.

Types de renseignements personnels recueillis :
Nous ne collectons aucune information personnellement identifiable via cette application. Toutes les données saisies dans l'application ne sont utilisées que dans le but d'effectuer le calcul demandé et ne sont ni stockées ni partagées.

Comment les informations personnelles sont collectées :
Toutes les données saisies dans l'application sont collectées via la saisie de l'utilisateur.

Finalité de la collecte des informations personnelles :
Le but de la collecte des données est uniquement dans le but d'effectuer le calcul demandé.

Comment les informations personnelles sont utilisées :
Nous utilisons les données saisies dans l'application uniquement dans le but d'effectuer le calcul demandé. Il n'est pas utilisé à d'autres fins.

Comment les informations personnelles sont partagées :
Nous ne partageons aucune information personnelle collectée via l'application avec des tiers.

Mesures de sécurité:
Nous prenons les mesures techniques et organisationnelles appropriées pour protéger les informations personnelles que nous collectons via l'application contre tout accès, divulgation, altération ou destruction non autorisés.

Droits de l'utilisateur:
Les utilisateurs ont le droit d'accéder, de corriger, de supprimer ou de restreindre l'utilisation de leurs informations personnelles. Si vous avez des préoccupations concernant la confidentialité, veuillez nous contacter à hamza.oukhacha@edu.uiz.ac.ma.

Coordonnées:
Si vous avez des questions ou des préoccupations concernant nos pratiques de confidentialité, veuillez nous contacter à hamza.oukhacha@edu.uiz.ac.ma.
"""

    privacy_frame = Frame(privacy_win, bg="#f5f5f5")
    privacy_frame.pack(fill=BOTH, expand=True)

    privacy_scrollbar = Scrollbar(privacy_frame)
    privacy_scrollbar.pack(side=RIGHT, fill=Y)

    privacy_textbox = Text(
        privacy_frame,
        font=("Helvetica", 12),
        bg="#f5f5f5",
        padx=20,
        pady=20,
        wrap=WORD
    )
    privacy_textbox.pack(fill=BOTH, expand=True)

    privacy_textbox.insert(END, privacy_text)
    privacy_scrollbar.config(command=privacy_textbox.yview)
    privacy_textbox.config(yscrollcommand=privacy_scrollbar.set)
# Fenêtre À propos de moi
def about_window():
    about_win = Toplevel(root)
    about_win.title("Sur equipe")
    about_win.geometry("600x500")
    about_win.resizable(False, False)
    about_win.configure(bg="#f5f5f5")

    about_text = """Le projet "Application Web de Diagonalisation et Trigonalisation de Matrices Carrées avec Python" est un effort collaboratif de quatre personnes : \n\nSouad Tahri, Samira Mazine, Hamza Oukhacha et Abdelghani ET-Toulouti.\n\nLe projet est en cours développé dans le cadre de leur projet de fin d'année à l'université, et il se concentre sur la création d'une application Web qui implémente la diagonalisation et la triangularisation d'une matrice carrée à l'aide de Python. Le projet est développé sous la supervision du stade universitaire\n\nProf Brahim EL HABIL.\n\nLe projet vise à fournir une application Web efficace et conviviale qui permet aux utilisateurs d'effectuer facilement la diagonalisation et la triangularisation de matrices carrées à l'aide de Python . La diagonalisation et la triangularisation sont des concepts mathématiques importants qui ont des applications dans divers domaines tels que la physique, l'ingénierie et l'informatique. En implémentant ces concepts dans une application web, le projet vise à les rendre accessibles à un public plus large, comprenant des étudiants, des chercheurs et des professionnels.

L'équipe utilise Python comme langage de programmation principal pour le projet, ainsi que diverses bibliothèques et frameworks tels que Flask, NumPy et SciPy. L'application Web aura une interface conviviale qui permettra aux utilisateurs de saisir leurs données matricielles, de sélectionner l'opération souhaitée (diagonalisation ou triangularisation) et de visualiser les résultats. L'équipe travaille également sur la mise en œuvre de fonctionnalités supplémentaires telles que la visualisation de la matrice et de ses propriétés, ainsi que la possibilité d'enregistrer et de charger des matrices à partir de fichiers.

Dans l'ensemble, le projet "Application web sur Diagonalisation et Trigonalisation d'une matrice carrée sous python" est une entreprise innovante et ambitieuse qui met en valeur les compétences et l'expertise de l'équipe en programmation, en mathématiques et en développement web. Le projet a le potentiel d'apporter une contribution significative au domaine des opérations matricielles et à la communauté universitaire La Faculté Polydisciplinaire de Ouarzazate  au sens large.
\nPour Use cette application utilise \nusername : admin ,\npassword : admin
"""

    about_frame = Frame(about_win, bg="#f5f5f5")
    about_frame.pack(fill=BOTH, expand=True)

    about_scrollbar = Scrollbar(about_frame)
    about_scrollbar.pack(side=RIGHT, fill=Y)

    about_textbox = Text(
        about_frame,
        font=("Helvetica", 12),
        bg="#f5f5f5",
        padx=20,
        pady=20,
        wrap=WORD
    )
    about_textbox.pack(fill=BOTH, expand=True)

    about_textbox.insert(END, about_text)
    about_scrollbar.config(command=about_textbox.yview)
    about_textbox.config(yscrollcommand=about_scrollbar.set, state=DISABLED)

    # Mettez en surbrillance les noms des équipes et le nom du superviseur
    team_names = ["Souad Tahri", "Samira Mazine", "Hamza Oukhacha", "Abdelghani ET-Toulouti"]
    supervisor_name = "Prof Brahim EL HABIL"
    color = "#2471A3"

    for name in team_names:
        start = about_text.index(name)
        end = f"{start}+{len(name)}c"
        about_textbox.tag_add("bold", start, end)
        about_textbox.tag_config("bold", font=("Helvetica", 12, "bold"), foreground=color)

    start = about_text.index(supervisor_name)
    end = f"{start}+{len(supervisor_name)}c"
    about_textbox.tag_add("bold", start, end)
    about_textbox.tag_config("bold", font=("Helvetica", 12, "bold"), foreground=color)

    about_win.mainloop()
# Ajouter un cadre en bas de la fenêtre
bottom_frame = Frame(root)
bottom_frame.grid(row=1, column=0, sticky="s")

# Ajoutez les boutons Politique de confidentialité et À propos de moi au cadre inférieur
privacy_button = Button(bottom_frame, text="politique de confidentialité", command=privacy_window)
privacy_button.grid(row=0, column=0, padx=10)

about_button = Button(bottom_frame, text="Sur Equipe", command=about_window)
about_button.grid(row=0, column=1, padx=10)



root.mainloop()