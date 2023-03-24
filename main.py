from tkinter import *
from matrix_function import *
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
root.configure(bg="sky blue")
root.geometry("1020x720")
root.title("Operations Matricelle")
#root.iconbitmap("matrix-logo1.png")
#root.iconphoto(Image.open("Matrice_logo.png"))
################################################################

######################################################
main_frame=Frame(root,height=700,width=580,bg="red")
result_frame=Frame(root,bg="#5F9EA0")
root1=Frame(root,bg="red",bd=5,width=9880,height=2000)
result_frame=Frame(root,bg="#5F9EA0")
right_frame=Frame(root,bg="#5F9EA0")
middle_frame=Frame(root,bg="red")
left_frame=Frame(root,bg="red")
matrix_frame=Frame(left_frame,bg="#14d9d9")
methode_direct_frame=Frame(left_frame,bg="black")
methode_itera_frame=Frame(left_frame,bg="black")
determinant_frame=Frame(left_frame,bg="black")
###############################################################
"""
image = Image.open("matrix.png")
ima=image.resize((400,150))
new_image= ImageTk.PhotoImage(ima)
label1 = Label(root, image=new_image,bg="sky blue")
label1.place(x=1200, y=0)


"""
##############################################################
####middle frame###
def input_row_column():
    global row, col
    Label(middle_frame, text="Enter number of rows for matrix   1:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Enter number of column for matrix 1:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=4)
    row = IntVar()
    Entry(middle_frame, width=4, textvariable=row, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4, column=12)
    col = IntVar()
    Entry(middle_frame, width=4, textvariable=col, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    Button(middle_frame, text="submit", bg="black", fg="white", width=5, command=input_grid).grid(row=6, column=10, columnspan=3)
    middle_frame.grid(row=5,rowspan=4, column=2, columnspan=4, padx=200, pady=50)
def input_grid():
    global right_frame
    middle_frame.grid_forget()
    right_frame.destroy()
    right_frame=Frame(root,bg="sky blue")
    r=row.get()
    c=col.get()
    global dic
    temp = []
    dic = []
    for i in range(r):
        for j in range(c):
            temp.append(IntVar())
        dic1.append(temp)
        temp = []
    Label(right_frame, text="INPUT MATRIX ", fg="white", bg="black", font=("ariel", 15)).grid(row=0, column=1,columnspan=3,padx=10, pady=10)
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
            ent.grid(row=i, column=j)
    Button(right_frame, text="Submit", bg="black", fg="white", width=5, font=("ariel", 15),command=input_cmd).grid(row=4,column=1,columnspan=3,pady=10)
    right_frame.grid(row=5,rowspan=100,column=50,columnspan=4,padx=200,pady=50)
def input_cmd():
    global mainmatrix
    mainmatrix=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        mainmatrix.append(temp)
        temp=[]
    return mainmatrix
########################################################
def frame_destroy():
    global middle_frame
    middle_frame.destroy()
    middle_frame=Frame(root,bg="sky blue")
    global right_frame
    right_frame.destroy()
    right_frame = Frame(root, bg="sky blue")
    global result_frame
    result_frame.destroy()
    result_frame = Frame(root, bg="sky blue")
#######################################################
#matrix
##########################################################################################################################
#Adjoint
def adjoint_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="  Dimension de matrice:", bg="sky blue", fg="black",font=("ariel", 16)).grid(row=2, column=4)

    Label(middle_frame, text="Entrer nombre de ligne    :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne    :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="white", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="white", relief="solid").grid(row=5,column=12)
    submit_btn=Button(middle_frame,text="Envoyer",bg="#5F9EA0",fg="white",width=5,command=adjoint_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,column=2,columnspan=4,padx=200,pady=50)
def adjoint_grid():
    r1=row1.get()
    c1=col1.get()
    if r1 != 0 and c1 != 0 and c1 == r1:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice A:", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 ,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=adjoint_cmd).grid(row=r1 + r1 + 5, column=12)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=adjoint_input_row_column).grid(row=r1 + r1 + 5, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or c1 == 0 :
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles.")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")
def adjoint_cmd():
    global adjm1
    adjm1 = []
    temp = []
    for i in dic1:
         for j in i:
             temp.append(j.get())
         adjm1.append(temp)
         temp = []

    adjoint = adjoint_of_matrix(adjm1)
    Label(result_frame, text="Matrice Adjoint", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=0,columnspan=len(adjoint[0]))
    for i in range(len(adjoint)):
        for j in range(len(adjoint[0])):
            Label(result_frame, text=adjoint[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i + 1,column=j,padx=5,pady=5)
    result_frame.grid(row=7, column=300, padx=100)
####################################################################################################################################################
   #Inverse
def inverse_input_row_column():
    frame_destroy()
    global row1, col1
    Label(middle_frame, text="Dimension de matrice", bg="sky blue", fg="black",font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer le nombre de ligne:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entre le nombre de colonne:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, command=inverse_grid)
    submit_btn.grid(row=11, column=14, columnspan=3)
    middle_frame.grid(row=5, column=2, columnspan=4, padx=200, pady=50)


def inverse_grid():
    r1 = row1.get()
    c1 = col1.get()
    if r1 != 0 and c1 != 0 and c1 == r1:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=inverse_cmd).grid(row=r1 + r1 + 5, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=inverse_input_row_column).grid(row=r1 + r1 + 5, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or c1 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles.")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")


def inverse_cmd():
    global invm1
    invm1 = []
    temp = []
    for i in dic1:
        for j in i:
            temp.append(j.get())
        invm1.append(temp)
        temp = []
    if main_determinant(invm1) != 0:
        inverse = inverse_of_matrix(invm1)
        Label(result_frame, text="Matrice Inverse", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=0,columnspan=len(inverse[0]))
        for i in range(len(inverse)):
            for j in range(len(inverse[0])):
                Label(result_frame, text=inverse[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i + 1,column=j,padx=5,pady=5)
        result_frame.grid(row=7, column=300, padx=100)
    else:
        messagebox.showerror("Input Error","l’inverse n’est pas possible car \n déterminant est zéro")
######################################################################################################################################################
#Cofactor
def cofactor_input_row_column():
    frame_destroy()
    global row1, col1
    Label(middle_frame, text="Dimension de matrice:", bg="sky blue", fg="black",font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, command=cofactor_grid)
    submit_btn.grid(row=11, column=14, columnspan=3)
    middle_frame.grid(row=5, column=2, columnspan=4, padx=200, pady=50)


def cofactor_grid():
    r1 = row1.get()
    c1 = col1.get()
    if r1 != 0 and c1 != 0 and c1 == r1:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer matrice", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 ,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=cofactor_cmd).grid(row=r1 + r1 + 5, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=cofactor_input_row_column).grid(row=r1 + r1 + 5, column=2)

        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or c1 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles..")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")


def cofactor_cmd():
    global cofm1
    cofm1 = []
    temp = []
    for i in dic1:
        for j in i:
            temp.append(j.get())
        cofm1.append(temp)
        temp = []
    cofactor_re = cofactor_matrix(cofm1)
    Label(result_frame, text="Matrice cofacteur", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=0,columnspan=len(cofactor_re[0]))
    for i in range(len(cofactor_re)):
        for j in range(len(cofactor_re[0])):
            Label(result_frame, text=cofactor_re[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i + 1,column=j,padx=5,pady=5)
    result_frame.grid(row=7, column=300, padx=100)
#########################################################################################################################################
#determinant
def determinant_input_row_column():
    frame_destroy()
    global row, col
    Label(middle_frame, text="Dimension de matrice:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne  :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=20)
    Label(middle_frame, text="Entrer nombre de colonne :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=6, column=20)
    row = IntVar()
    Entry(middle_frame, width=4, textvariable=row, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=22)
    col = IntVar()
    Entry(middle_frame, width=4, textvariable=col, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=6,column=22)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, command=determinant_grid)
    submit_btn.grid(row=11, column=20, columnspan=3)
    middle_frame.grid(row=8, column=20, columnspan=4, padx=200, pady=50)


def determinant_grid():
    r1 = row.get()
    c1 = col.get()
    if r1 != 0 and c1 != 0 and r1 == c1:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame ,text="Entrer matrice", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 ,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j , padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=determinant_cmd).grid(row=r1 +1 , column=c1-1,columnspan=c1,padx=10,pady=2)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=determinant_input_row_column).grid(row=r1 + r1 + 5, column=10)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=4,padx=20,pady=50)
    elif r1 == 0 or c1 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles..")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal.")


def determinant_cmd():
    global determinant
    determinantmatrix = []
    temp = []
    for i in dic1:
        for j in i:
            temp.append(j.get())
        determinantmatrix.append(temp)
        temp = []
    determinant_result = main_determinant(determinantmatrix)
    Label(result_frame, text="Determinent de matrice",bg="#5F9EA0" ,font=("ariel", 15)).grid(row=10, column=0, rowspan=10,columnspan=2)
    Label(result_frame, text=determinant_result, width=5, font=("ariel", 15)).grid(row=20, column=0,columnspan=1, pady=10)
    result_frame.grid(row=7, column=300, padx=100)



#########################################################################################################################################
#Transpose
def transpose_input_row_column():
    frame_destroy()
    global row1, col1
    Label(middle_frame, text="Dimension de matrice:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne:", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, command=transpose_grid)
    submit_btn.grid(row=11, column=14, columnspan=3)
    middle_frame.grid(row=5, column=2, columnspan=4, padx=200, pady=50)


def transpose_grid():
    r1 = row1.get()
    c1 = col1.get()
    if r1 != 0 and c1 != 0 :
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 ,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=transpose_cmd).grid(row=r1 + r1 + 5, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=transpose_input_row_column).grid(row=r1 + r1 + 5, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or c1 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles..")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")


def transpose_cmd():
    global trm1
    trm1 = []
    temp = []
    for i in dic1:
        for j in i:
            temp.append(j.get())
        trm1.append(temp)
        temp = []
    transposee = transpose(trm1)
    Label(result_frame, text="matrice Transpose", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=0,columnspan=len(transposee[0]))
    for i in range(len(transposee)):
        for j in range(len(transposee[0])):
            Label(result_frame, text=transposee[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i + 1,column=j,padx=5,pady=5)
    result_frame.grid(row=7, column=300, padx=100)



##########################################################################################################################
#product
def produit_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne de A:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne de A:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    global  row2,col2
    Label(middle_frame, text="Dimension de matrice B:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=8, column=4)
    Label(middle_frame, text="Entrer nombre de ligne de B:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=9, column=4)
    Label(middle_frame, text="Entrer nombre de colonne de B:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=10, column=4)
    row2 = IntVar()
    Entry(middle_frame, width=4, textvariable=row2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=9,column=12)
    col2 = IntVar()
    Entry(middle_frame, width=4, textvariable=col2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=10,column=12)
    Label(middle_frame,text="""   """,bg="sky blue").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    submit_btn=Button(middle_frame,text="Envoyer",bg="#5F9EA0",fg="white",width=5,command=produit_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,column=2,columnspan=4,padx=200,pady=50)
def produit_grid():
    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()
    if c1 == r2 and r1 != 0 and r2 != 0 and c1 != 0 and c2 != 0:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice A:", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        global dic2
        temp = []
        dic2 = []
        for i in range(r2):
            for j in range(c2):
                temp.append(IntVar())
            dic2.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice B:", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r1 + 1,column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r2 + 1):
            for j in range(1, c2 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic2[i - 1][j - 1])
                ent.grid(row=i + r1 + 2, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=produit_cmd).grid(row=r1 + r1 + 5, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=produit_input_row_column).grid(row=r1 + r1 + 5, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or r2 == 0 or c1 == 0 or c2 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles.")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal ")


def produit_cmd():
    global pdm1
    pdm1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        pdm1.append(temp)
        temp=[]
    global pdm2
    pdm2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        pdm2.append(temp)
        temp=[]
    produit=produit_of_matrix(pdm1,pdm2)
    Label(result_frame,text="A*B",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=len(produit[0]))
    for i in range (len(produit)):
        for j in range (len(produit[0])):
            Label(result_frame,text=produit[i][j],padx=6,pady=5,width=5,font=("ariel",15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
########################################################
def subtraction_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne de A:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne de A:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    global  row2,col2
    Label(middle_frame, text="Dimension de matrice B:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=8, column=4)
    Label(middle_frame, text="Entrer nombre de ligne de B:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=9, column=4)
    Label(middle_frame, text="Entrer nombre de colonne de B:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=10, column=4)
    row2 = IntVar()
    Entry(middle_frame, width=4, textvariable=row2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=9,column=12)
    col2 = IntVar()
    Entry(middle_frame, width=4, textvariable=col2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=10,column=12)
    Label(middle_frame,text="""   """,bg="sky blue").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    submit_btn=Button(middle_frame,text="Envoyer",bg="#5F9EA0",fg="white",width=5,command=subtraction_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,column=2,columnspan=4,padx=200,pady=50)
def subtraction_grid():
    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()
    if r1 == r2 and r1 != 0 and r2 != 0 and c1 == c2 and c1 != 0 and c2 != 0:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice A", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        global dic2
        temp = []
        dic2 = []
        for i in range(r2):
            for j in range(c2):
                temp.append(IntVar())
            dic2.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice B", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r1 + 1,column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r2 + 1):
            for j in range(1, c2 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic2[i - 1][j - 1])
                ent.grid(row=i + r1 + 2, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=subtraction_cmd).grid(row=r1 + r1 + 5, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=subtraction_input_row_column).grid(row=r1 + r1 + 5, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or r2 == 0 or c1 == 0 or c2 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles..")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")


def subtraction_cmd():
    global subm1
    subm1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        subm1.append(temp)
        temp=[]
    global subm2
    subm2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        subm2.append(temp)
        temp=[]
    subtraction=subtraction_of_matrix(subm1,subm2)
    Label(result_frame,text="A - B",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=len(subtraction[0]))

    for i in range (len(subtraction)):
        for j in range (len(subtraction[0])):
            Label(result_frame,text=subtraction[i][j],padx=6,pady=5,width=5,font=("ariel",15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)
###############################################################
def addition_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne de A:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne de A", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    global  row2,col2
    Label(middle_frame, text="Dimension de matrice de B:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=7, column=4)
    Label(middle_frame, text="entrer de nombre de ligne de B:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=9, column=4)
    Label(middle_frame, text="Entrer nobre de colonne de B:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=10, column=4)
    row2 = IntVar()
    Entry(middle_frame, width=4, textvariable=row2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=9,column=12)
    col2 = IntVar()
    Entry(middle_frame, width=4, textvariable=col2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=10,column=12)
    Label(middle_frame,text="""   """,bg="sky blue").grid(row=10,column=14,padx=80,pady=2,sticky=EW)
    submit_btn=Button(middle_frame,text="Valider",bg="#5F9EA0",fg="black",font=("ariel", 15),width=8,command=addition_grid)
    submit_btn.grid(row=11,column=14,columnspan=3)
    middle_frame.grid(row=5,column=2,columnspan=4,padx=200,pady=50)
def addition_grid():
    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()
    if r1 == r2 and r1 != 0 and r2 != 0 and c1 == c2 and c1 != 0 and c2 != 0:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice A", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        global dic2
        temp = []
        dic2 = []
        for i in range(r2):
            for j in range(c2):
                temp.append(IntVar())
            dic2.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice B", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r1 + 1,column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r2 + 1):
            for j in range(1, c2 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic2[i - 1][j - 1])
                ent.grid(row=i + r1 + 2, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Valider", bg="#5F9EA0", fg="black", width=8, font=("ariel", 15),command=addition_cmd).grid(row=r1 + r1 + 5, column=10)
        back=Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=addition_input_row_column).grid(row=r1 + r1 + 5, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    elif r1 == 0 or r2 == 0 or c1 == 0 or c2 == 0:
        messagebox.showerror("input error", "les lignes et les colonnes ne peuvent pas être nulles..")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")


def addition_cmd():
    global addm1
    addm1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        addm1.append(temp)
        temp=[]
    global addm2
    addm2=[]
    temp=[]
    for i in dic2:
        for j in i:
            temp.append(j.get())
        addm2.append(temp)
        temp=[]
    addition=addition_of_matrix(addm1,addm2)
    Label(result_frame,text="A + B",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=len(addition[0]))

    for i in range (len(addition)):
        for j in range (len(addition[0])):
            Label(result_frame,text=addition[i][j],padx=6,pady=5,width=5,font=("ariel",15)).grid(row=i+1,column=j,padx=5,pady=5)
    result_frame.grid(row=7,column=300,padx=100)

################################################################
def qr_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=8)
    Label(middle_frame, text="Entrer nombre de ligne de A  :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=8)
    Label(middle_frame, text="Entrer nombre de colonne de A:", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=8)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=14)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=14)
    Label(middle_frame, text="""   """, bg="sky blue").grid(row=10, column=14, padx=80, pady=2, sticky=EW)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=8,command=qr_grid)
    submit_btn.grid(row=11, column=14, columnspan=3)
    middle_frame.grid(row=8, column=20, columnspan=4, padx=200, pady=50)
def qr_grid():
    r1=row1.get()
    c1=col1.get()
    #r2=row2.get()
   # c2=col2.get()
    if r1 != 0 and c1 != 0 :
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice A: ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 , padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=8, font=("ariel", 15),command=qr_cmd).grid(row=r1 + r1 + 4, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=qr_input_row_column).grid(row=r1 + r1 + 4, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")
def qr_cmd():
    global lum1
    lum1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        lum1.append(temp)
        temp=[]
    LU=Qr_of_matrix(lum1)
    UL=Rq_of_matrix(lum1)

    Label(result_frame,text="MATRICE Q:",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=len(LU[0]))
    Label(result_frame, text="MATRICE R:", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=12, column=0,columnspan=len(UL[0]))
    for i in range (len(LU)):
        for j in range (len(LU[0])):
            Label(result_frame,text=LU[i][j],padx=6,pady=5,width=8,font=("ariel",15)).grid(row=i+1,column=j,padx=5,pady=5)
            Label(result_frame, text=UL[i][j], padx=6, pady=5, width=8, font=("ariel", 15)).grid(row=i +22, column=j,padx=5, pady=5)
    result_frame.grid(row=7,column=300,padx=100)
###################################################################################################################################
#Methode direct
def LU_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=8)
    Label(middle_frame, text=" Entrer nombre de ligne de A  :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=8)
    Label(middle_frame, text="Entrer nombre de colonne de A :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=8)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=14)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=14)
    Label(middle_frame, text="""   """, bg="sky blue").grid(row=10, column=14, padx=80, pady=2, sticky=EW)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=8,command=LU_grid)
    submit_btn.grid(row=11, column=14, columnspan=3)
    middle_frame.grid(row=8, column=20, columnspan=4, padx=200, pady=50)
def LU_grid():
    r1=row1.get()
    c1=col1.get()
    #r2=row2.get()
   # c2=col2.get()
    if r1 != 0 and c1 != 0 :
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer Matrice A: ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 , padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=8, font=("ariel", 15),command=LU_cmd).grid(row=r1 + r1 + 4, column=10)

        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=LU_input_row_column).grid(row=r1 + r1 + 4, column=2)

        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")
def LU_cmd():
    global lum1
    lum1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        lum1.append(temp)
        temp=[]
    LU=lu_of_matrix1(lum1)
    UL=lu_of_matrix(lum1)

    Label(result_frame,text="MATRICE L",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=len(LU[0]))
    Label(result_frame, text="MATRICE U", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=12, column=0,columnspan=len(UL[0]))
    for i in range (len(LU)):
        for j in range (len(LU[0])):
            Label(result_frame,text=LU[i][j],padx=6,pady=5,width=5,font=("ariel",15)).grid(row=i+1,column=j,padx=5,pady=5)
            Label(result_frame, text=UL[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i +22, column=j,padx=5, pady=5)
    result_frame.grid(row=7,column=300,padx=100)
####################################################################################################################################
#cholesky
def chol_input_row_column():
    frame_destroy()
    global row1,col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=1, column=8)
    Label(middle_frame, text="Entrer nombre de ligne de A   :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=4, column=8)
    Label(middle_frame, text="Entrer nombre de colonne de A :", bg="#5F9EA0", fg="white", borderwidth=3, relief="groove",font=("ariel", 10), width=35).grid(row=5, column=8)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=14)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=14)
    Label(middle_frame, text="""   """, bg="sky blue").grid(row=10, column=14, padx=80, pady=2, sticky=EW)
    submit_btn = Button(middle_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=8,command=chol_grid)
    submit_btn.grid(row=11, column=14, columnspan=3)
    middle_frame.grid(row=8, column=20, columnspan=4, padx=200, pady=50)
def chol_grid():
    r1=row1.get()
    c1=col1.get()
    #r2=row2.get()
   # c2=col2.get()
    if r1 != 0 and c1 != 0 :
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic1
        temp = []
        dic1 = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer matrice symetrique definie positif ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 , padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=4, textvariable=dic1[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=8, font=("ariel", 15),command=chol_cmd).grid(row=r1 + r1 + 4, column=10)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=chol_input_row_column).grid(row=r1 + r1 + 4, column=2)
        right_frame.grid(row=5, rowspan=100, column=50, columnspan=40)
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal ")

def chol_cmd():
    global lum1
    lum1=[]
    temp=[]
    for i in dic1:
        for j in i:
            temp.append(j.get())
        lum1.append(temp)
        temp=[]
    chol=chol_of_matrix(lum1)


    Label(result_frame,text="MATRICE L",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=len(chol[0]))
    #Label(result_frame, text="MATRIX U", fg="white", bg="black", font=("ariel", 15)).grid(row=12, column=0,columnspan=len(UL[0]))
    for i in range (len(chol)):
        for j in range (len(chol[0])):
            Label(result_frame,text=chol[i][j],padx=6,pady=5,width=5,font=("ariel",15)).grid(row=i+1,column=j,padx=5,pady=5)
           # Label(result_frame, text=UL[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i +22, column=j,padx=5, pady=5)
    result_frame.grid(row=7,column=300,padx=100)
#################################################################################################################################
#gauss
def gaus_input_row_column():
    frame_destroy()
    global row1, col1
    Label(middle_frame, text="Dimension de matrice A:", bg="sky blue", fg="black",font=("ariel", 16), width=35).grid(row=1, column=4)
    Label(middle_frame, text="Entrer nombre de ligne de A :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Entrer nombre de colonne de A :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    global row2,col2
    Label(middle_frame, text="Dimension de vecteur b:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=7, column=4)
    Label(middle_frame, text="Enter nombre de ligne de  vecteur b    :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=9, column=4)
    Label(middle_frame, text="Enter nombre de colonne de  vecteur  b    :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=10, column=4)
    row2 = IntVar()
    Entry(middle_frame, width=4, textvariable=row2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=9,column=12)
    col2 = IntVar()
    #col2 = 1
    Entry(middle_frame, width=4, textvariable=col2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=10,column=12)
    #Label(middle_frame, text="""   """, bg="sky blue").grid(row=11, column=12, padx=80, pady=2, sticky=EW)
    global row3, col3
    Label(middle_frame, text="Dimension de vecteur x:", bg="sky blue", fg="black", font=("ariel", 16), width=35).grid(row=11, column=4)
    Label(middle_frame, text=" Entrer nombre de ligne de  x    :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=13, column=4)
    Label(middle_frame, text=" Entrer nombre de colonne de  x      :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=14, column=4)
    row3 = IntVar()
    Entry(middle_frame, width=4, textvariable=row3, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=13,column=12)
    col3 = IntVar()
    Entry(middle_frame, width=4, textvariable=col3, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=14,column=12)
    Label(middle_frame, text="""   """, bg="sky blue").grid(row=10, column=14, padx=80, pady=2, sticky=EW)
    submit_btn = Button(middle_frame, text="Valider", bg="#5F9EA0", fg="black", font=("ariel", 15), width=8, command=gaus_grid)
    submit_btn.grid(row=14, column=14, columnspan=3)
    middle_frame.grid(row=5, column=8, columnspan=4, padx=200, pady=50)

def gaus_grid():
    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()
    r3=row3.get()
    c3=col3.get()
    if r1 != 0 and c1 != 0 and r2!=0 and c2!=0 and c2==1 and r3!=0 and c3!=0 and c3==1:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic
        temp = []
        dic = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic.append(temp)
            temp = []
        Label(right_frame, text="Entrer matrice A ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 , padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=8, textvariable=dic[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        global dic1
        temp = []
        dic1 = []
        for i in range(r2):
            for j in range(c2):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="Entrer vecteur b ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r2+1, column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r2 + 1):
            for j in range(1,c2+1):
                ent = Entry(right_frame, width=8, textvariable=dic1[i-1][j -1])
                ent.grid(row=i+r2+2, column=3, padx=5, pady=5)
        global dic2
        temp = []
        dic2 = []
        for i in range(r3):
            for j in range(c3):
                temp.append(IntVar())
            dic2.append(temp)
            temp = []
        Label(right_frame, text="Entrer vecteur  x ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r2 + 1, column=10,columnspan=c1 + c3,padx=10, pady=10)
        for i in range(1, r3 + 1):
            for j in range(1, c3 + 1):
                ent = Entry(right_frame, width=8, textvariable=dic2[i - 1][j - 1])
                ent.grid(row=i + r3 + 2, column=10, padx=5, pady=5)

        Label(right_frame, text="nombre d'iteration ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r2 + 1,column=20,columnspan=c1 + c3,padx=10, pady=10)
        global var_texte
        var_texte = IntVar()
        ligne_texte = Entry(right_frame, textvariable=var_texte, width=4)
        ligne_texte.grid(row= r3 + 2, column=20, padx=5, pady=5)

        Button(right_frame, text="Envoyer", bg="#5F9EA0", fg="white", width=7, font=("ariel", 15),command=gaus_cmd).grid(row=r1 + r1 + 23, column=14)
        back = Button(right_frame, text="Retour", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=gaus_input_row_column).grid(row=r1 + r1 + 23, column=2)
        right_frame.grid(row=4, column=40, rowspan=100,columnspan=40)
    elif c2 !=1 and c3!=1:
        messagebox.showerror("input error", "le nombre de colonnes pour le vecteur b doit être égal.1 ")
    else:
        messagebox.showerror("input error", "le nombre de lignes et de colonnes doit être égal. ")

def gaus_cmd():
    right_frame.destroy()
    n=var_texte.get()
    global A
    A=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        A.append(temp)
        temp=[]
    global b
    b = []
    temp = []
    for i in dic1:
        for j in i:
            temp.append(j.get())
        b.append(temp)
        temp = []
    global x
    x = []
    temp = []
    for i in dic2:
        for j in i:
            temp.append(j.get())
        x.append(temp)
        temp = []


    gaus = gaus_of_matrix(A, b, x,n)
    Label(result_frame,text="Solution",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=2)
    back = Button(result_frame, text="Retour", bg="#5F9EA0", fg="white", width=6, font=("ariel", 15),command= gaus_grid).grid(row=6 + 20, column=2)
    #Label(result_frame, text="MATRIX U", fg="white", bg="black", font=("ariel", 15)).grid(row=12, column=0,columnspan=len(UL[0]))
    for i in range (len(gaus)):
        for j in range (1):
            Label(result_frame,text=gaus[i][j],padx=6,pady=25,width=15,font=("ariel",15)).grid(row=20+1,column=i,padx=5,pady=5)
           # Label(result_frame, text=UL[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i +22, column=j,padx=5, pady=5)

    result_frame.grid(row=7,column=100,padx=100)
#################################################################################################################################
#jacobi
def jacobi_input_row_column():
    frame_destroy()
    global row1, col1
    Label(middle_frame, text="Enter number of rows for matrix   :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=4, column=4)
    Label(middle_frame, text="Enter number of column for matrix :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=5, column=4)
    row1 = IntVar()
    Entry(middle_frame, width=4, textvariable=row1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=4,column=12)
    col1 = IntVar()
    Entry(middle_frame, width=4, textvariable=col1, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=5,column=12)
    global row2,col2
    Label(middle_frame, text="Enter number of rows for vector b    :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=9, column=4)
    Label(middle_frame, text="Enter number of columns for vector b    :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=10, column=4)
    row2 = IntVar()
    Entry(middle_frame, width=4, textvariable=row2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=9,column=12)
    col2 = IntVar()
    #col2 = 1
    Entry(middle_frame, width=4, textvariable=col2, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=10,column=12)
    Label(middle_frame, text="""   """, bg="sky blue").grid(row=11, column=12, padx=80, pady=2, sticky=EW)
    global row3, col3
    Label(middle_frame, text=" rows for initialise vector x    :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=13, column=4)
    Label(middle_frame, text=" columns for initialise vector x     :", bg="#5F9EA0", fg="white", borderwidth=3,relief="groove", font=("ariel", 10), width=35).grid(row=14, column=4)
    row3 = IntVar()
    Entry(middle_frame, width=4, textvariable=row3, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=13,column=12)
    col3 = IntVar()
    Entry(middle_frame, width=4, textvariable=col3, borderwidth=3, bg="#5F9EA0", fg="black", relief="solid").grid(row=14,column=12)
    Label(middle_frame, text="""   """, bg="sky blue").grid(row=10, column=14, padx=80, pady=2, sticky=EW)
    submit_btn = Button(middle_frame, text="submit", bg="#5F9EA0", fg="white", width=5, command=jacobi_grid)
    submit_btn.grid(row=14, column=14, columnspan=3)
    middle_frame.grid(row=5, column=8, columnspan=4, padx=200, pady=50)

def jacobi_grid():
    r1=row1.get()
    c1=col1.get()
    r2=row2.get()
    c2=col2.get()
    r3=row3.get()
    c3=col3.get()
    if r1 != 0 and c1 != 0 and r2!=0 and c2!=0 and c2==1 and r3!=0 and c3!=0 and c3==1:
        global right_frame
        middle_frame.grid_forget()
        right_frame.destroy()
        right_frame = Frame(root, bg="sky blue")
        global dic
        temp = []
        dic = []
        for i in range(r1):
            for j in range(c1):
                temp.append(IntVar())
            dic.append(temp)
            temp = []
        Label(right_frame, text="INPUT MATRIX ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=0, column=1,columnspan=c1 , padx=10, pady=10)
        for i in range(1, r1 + 1):
            for j in range(1, c1 + 1):
                ent = Entry(right_frame, width=8, textvariable=dic[i - 1][j - 1])
                ent.grid(row=i, column=j + 2, padx=5, pady=5)
        global dic1
        temp = []
        dic1 = []
        for i in range(r2):
            for j in range(c2):
                temp.append(IntVar())
            dic1.append(temp)
            temp = []
        Label(right_frame, text="INPUT vector b ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r2+1, column=1,columnspan=c1 + c2,padx=10, pady=10)
        for i in range(1, r2 + 1):
            for j in range(1,c2+1):
                ent = Entry(right_frame, width=8, textvariable=dic1[i-1][j -1])
                ent.grid(row=i+r2+2, column=j + 2, padx=5, pady=5)
        global dic2
        temp = []
        dic2 = []
        for i in range(r3):
            for j in range(c3):
                temp.append(IntVar())
            dic2.append(temp)
            temp = []
        Label(right_frame, text="INPUT vector x ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r2 + 1, column= c3+6,columnspan=c1 + c3,padx=10, pady=10)
        for i in range(1, r3 + 1):
            for j in range(1, c3 + 1):
                ent = Entry(right_frame, width=8, textvariable=dic2[i - 1][j - 1])
                ent.grid(row=i + r3 + 2, column=j + 6, padx=5, pady=5)
        Label(right_frame, text="nombre iteration ", fg="white", bg="#5F9EA0", font=("ariel", 15)).grid(row=r2 + 1,column=20,columnspan=c1 + c3,padx=10, pady=10)
        global var_texte
        var_texte = IntVar()
        ligne_texte = Entry(right_frame, textvariable=var_texte, width=4)
        ligne_texte.grid(row=r3 + 2, column=20, padx=5, pady=5)
        Button(right_frame, text="Submit", bg="#5F9EA0", fg="white", width=5, font=("ariel", 15),command=jacobi_cmd).grid(row=r1 + r1 + 23, column=2)
        right_frame.grid(row=12, column=30, rowspan=100,columnspan=40)
    elif c2 !=1 and c3!=1:
        messagebox.showerror("input error", "number of columns for vector b should be equal.1 ")
    else:
        messagebox.showerror("input error", "number of rows and columns should be equal ")

def jacobi_cmd():
    n=var_texte.get()
    global A
    A=[]
    temp=[]
    for i in dic:
        for j in i:
            temp.append(j.get())
        A.append(temp)
        temp=[]
    global b
    b = []
    temp = []
    for i in dic1:
        for j in i:
            temp.append(j.get())
        b.append(temp)
        temp = []
    global x
    x = []
    temp = []
    for i in dic2:
        for j in i:
            temp.append(j.get())
        x.append(temp)
        temp = []

    jacobi = jacobi_of_matrix1(A, b, x,n)
    Label(result_frame,text="Solution",fg="white",bg="#5F9EA0",font=("ariel",15)).grid(row=0,column=0,columnspan=2)
    #Label(result_frame, text="MATRIX U", fg="white", bg="black", font=("ariel", 15)).grid(row=12, column=0,columnspan=len(UL[0]))
    for i in range (len(jacobi)):
        for j in range (1):
            Label(result_frame,text=jacobi[i][j],padx=6,pady=25,width=20,font=("ariel",15)).grid(row=20+1,column=i,padx=5,pady=5)
           # Label(result_frame, text=UL[i][j], padx=6, pady=5, width=5, font=("ariel", 15)).grid(row=i +22, column=j,padx=5, pady=5)
    result_frame.grid(row=7,column=35,padx=100)
####################################################################################################################################
def back_btn():
    back.grid_forget()
    determinant_frame.grid_forget()
    matrix_frame.grid_forget()
    methode_direct_frame.grid_forget()
    methode_itera_frame.grid_forget()
    root1.grid_forget()
    middle_frame.grid_forget()
    right_frame.grid_forget()
    result_frame.grid_forget()
    main_frame.grid()
def back_matrix():
    back.grid_forget()
    #matrix_frame.grid()
    matrix_frame.grid_forget()
    middle_frame.grid_forget()
    right_frame.grid_forget()
    result_frame.grid_forget()
    main_frame.grid()
################################################################
def matrix_cmd():
    global back
    main_frame.grid_remove()
    lb1=Label(matrix_frame,text="Matrice",font=("ariel",20),bg="black",fg="white")
    lb1.grid(row=0,column=0,ipadx=20,ipady=10)
    button1=Button(matrix_frame,text="Addition",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=addition_input_row_column)
    button1.grid(row=5,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Subtraction",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=subtraction_input_row_column)
    button1.grid(row=6,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Produit",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=produit_input_row_column)
    button1.grid(row=7,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Inverse",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=inverse_input_row_column)
    button1.grid(row=8,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Adjoint",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=adjoint_input_row_column)
    button1.grid(row=9,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="cofactor",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=cofactor_input_row_column)
    button1.grid(row=10,column=0,padx=10,pady=10,sticky="nsew")
    button1=Button(matrix_frame,text="Transpose",bd=10,bg="#DEB887",fg="black",font=("ariel",15),padx=10,pady=10,command=transpose_input_row_column)
    button1.grid(row=11,column=0,padx=10,pady=10,sticky="nsew")
    back=Button(matrix_frame,text="Home",bd=10,bg="red",fg="black",font=("ariel",15),padx=10,pady=10,width=10,command=back_btn)
    back.grid(row=12,column=0,padx=10,pady=10,sticky="nsew")
    matrix_frame.grid(row=0,column=0,columnspan=2,rowspan=6,sticky=W)
def determinant1_cmd():
    global back
    main_frame.grid_remove()
    lb1=Label(determinant_frame,text="DETERMINANT",font=("ariel",20),bg="black",fg="white")
    lb1.grid(row=0,column=0,ipadx=20,ipady=10)
    button1=Button(determinant_frame,text="value of determinant",bd=10,bg="green",fg="white",padx=10,pady=10,command=determinant_input_row_column)
    button1.grid(row=6,column=0,padx=10,pady=10,sticky="nsew")
    back = Button(determinant_frame, text="Home", bg="red", bd=10, fg="white", padx=10, pady=10, width=10,command=back_btn)
    back.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")
    determinant_frame.grid(row=0,column=0,columnspan=2,rowspan=6,sticky=W)


def methode_cmd():
    global back
    main_frame.grid_remove()
    lb1 = Label(methode_direct_frame, text="Methode direct", font=("ariel", 20), bg="black", fg="white")
    lb1.grid(row=0, column=0, ipadx=20, ipady=10)
    button1 = Button(methode_direct_frame, text="Decomposition LU", bg="#A52A2A",bd=10, fg="white", padx=10, pady=10,command=LU_input_row_column)
    button1.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
    button1 = Button(methode_direct_frame, text="Decomposition cholsky", bg="#A52A2A",bd=10, fg="white", padx=10, pady=10,command=chol_input_row_column)
    button1.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
    button1 = Button(methode_direct_frame, text="Decomposition QR", bg="#A52A2A", bd=10, fg="white", padx=10, pady=10,command=qr_input_row_column)
    button1.grid(row=7, column=0, padx=10, pady=10, sticky="nsew")
    back = Button(methode_direct_frame, text="Home", bg="red",bd=10, fg="white", padx=10, pady=10, width=10,command=back_btn)
    back.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")
    methode_direct_frame.grid(row=0, column=0, columnspan=2, rowspan=6, sticky=W)
#############################################################################
def methode_itera_cmd():
    global back
    main_frame.grid_remove()
    lb1 = Label(methode_itera_frame, text="Methode iterative", font=("ariel", 20), bg="black", fg="white")
    lb1.grid(row=0, column=0, ipadx=20, ipady=10)
    button1 = Button(methode_itera_frame, text="Jacobi",bg="#0000FF",bd=10, fg="black",font=("ariel", 20), padx=10, pady=10,command=jacobi_input_row_column)
    button1.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
    button1 = Button(methode_itera_frame, text="Gauss-seidel",bg="#0000FF",font=("ariel", 20),bd=10,fg="black", padx=10, pady=10,command=gaus_input_row_column)
    button1.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")
    back = Button(methode_itera_frame, text="Home",bg="red",bd=10, fg="black", padx=10,font=("ariel", 20), pady=10, width=10,command=back_btn)
    back.grid(row=12, column=0, padx=10, pady=10, sticky="nsew")
    methode_itera_frame.grid(row=0, column=0, columnspan=2, rowspan=6, sticky=W)
def demare():
    root1.grid_remove()
    root.protocol("WM_DELETE_window", close_main)
    Label(main_frame, text="""
    """, bg="sky blue").grid(row=6, columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, bg="sky blue").grid(row=0, columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=8, columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="         choisi une option      ", bg="sky blue", fg="white", font=("ariel", 20)).grid(row=5,column=20, columnspan=2, sticky=EW)
    Button(main_frame, text="Matrice", bg="#DEB887", fg="black",bd=30, font=("ariel", 20), width=10, command=matrix_cmd).grid(row=7, column=20, columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=7, padx=80, pady=2, sticky=EW)
    Button(main_frame, text="detirmenent", bg="green", fg="black",bd=30, font=("ariel", 20), width=10,command=determinant1_cmd).grid(row=9,column=20 ,columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=11, padx=80, pady=2, sticky=EW)
    Button(main_frame, text="Methode direct", bg="#A52A2A",bd=30, fg="black", font=("ariel", 20), width=15,command=methode_cmd).grid(row=25,column=20, columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=27, padx=80, pady=2, sticky=EW)
    Button(main_frame, text="Methode iterative", bg="#0000FF", fg="black", font=("ariel", 20),bd=30, width=15,command=methode_itera_cmd).grid(row=40,column=20, columnspan=2, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=41, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=27, padx=80, pady=2, sticky=EW)
    Label(main_frame, text="", bg="sky blue").grid(row=41, padx=80, pady=2, sticky=EW)
    back=Button(main_frame,text="Home",bg="red",bd=30,fg="black",font=("ariel", 18), width=15,command=ana)
    back.grid(row=50,column=20, columnspan=2, padx=80, pady=2, sticky=EW)
    left_frame.grid(row=4, column=0, columnspan=3, rowspan=7, sticky=W)
    main_frame.grid(row=0, column=0, columnspan=3, rowspan=3, sticky="nesw")
################################################################

################################################################
def close_main(event=None):
    if messagebox.askokcancel("quit","do youreally want to quit"):
        root.destroy()
#Label(root1,text="Bienvenu dans notre application, click sur aller pour commence les calcules",fg="black", font=("ariel", 20)).grid(row=0, column=1, columnspan=2, padx=80, pady=2, sticky=EW)
#Button(root1,text="Aller", bg="red", fg="white", font=("ariel", 18), width=15,bd=15,command=demare).grid(row=15, column=1, columnspan=2, padx=80, pady=2, sticky=EW)
########################################################################################################################################################################
def ana():
    main_frame.grid_remove()
    root1.grid(row=0, column=0, columnspan=3, rowspan=3, sticky="nesw")
    canevas = Canvas(root1, width=9880, height=7000, bg="#717113")

    ###########################################################

    image = PhotoImage(file="C:\\Users\\Pc\\PycharmProjects\\pythonProject10\\el.PNG")
    canevas.create_image(20, 0, anchor=NW, image=image)
    canevas.place(x=0, y=0)
    labelUsername = Label(canevas, text="Username: ", font=("ariel", 18), bg="#717113", fg="white")
    labelUsername.place(x=10, y=380)
    labelPassword = Label(canevas, text="Password: ", font=("ariel", 18), bg="#717113", fg="white")
    labelPassword.place(x=10, y=440)
    labelCfPass = Label(canevas, text='Conf.Pass: ', font=("ariel", 18), bg="#717113", fg="white")
    labelCfPass.place(x=10, y=500)
    entryUser = Entry(canevas, font=("ariel", 18), width=30, bg="#aed0a4", fg="#e8063b", justify="center")
    entryUser.place(x=150, y=380)
    global entryPassword
    c = StringVar()
    entryPassword = Entry(canevas, textvariable=c, font=("ariel", 18), width=30, bg="#aed0a4", fg="#e8063b",
                          justify="center", show="*")
    entryPassword.place(x=150, y=440)
    global entryCfPassword
    h = StringVar()
    entryCfPassword = Entry(canevas, textvariable=h, font=("ariel", 18), width=30, bg="#aed0a4", fg="#e8063b",
                            justify='center', show="*")
    entryCfPassword.place(x=150, y=500)

    c = entryPassword.get()

    buttonRegister = Button(root1, text="Submit", font=("ariel", 18), padx=6, bg="#aed0a4", fg="black", command=demare)
    buttonRegister.place(x=500, y=550)
def moi():
    c= entryPassword.get()
    v=entryCfPassword.get()
    if c =="2022" and v == "2022":
        demare()
    else:
        messagebox.showerror("input error", "mot de passe incorect ou configuration ")

########################################################################################################################################################################
root1.grid(row=0, column=0, columnspan=3, rowspan=3, sticky="nesw")
canevas = Canvas(root1, width=9880, height=7000, bg="#717113")

###########################################################
image = PhotoImage(file="C:\\Users\\lenovo\\Desktop\\imagetkinter\\wp5268499.png")
canevas.create_image(20, 0, anchor=NW, image=image)
canevas.place(x=0, y=0)
labelUsername = Label(canevas, text="Username: ", font=("ariel", 18), bg="#717113", fg="white")
labelUsername.place(x=10, y=380)
labelPassword = Label(canevas, text="Password: ", font=("ariel", 18), bg="#717113", fg="white")
labelPassword.place(x=10, y=440)
labelCfPass = Label(canevas, text='Conf.Pass: ', font=("ariel", 18), bg="#717113", fg="white")
labelCfPass.place(x=10, y=500)
entryUser = Entry(canevas, font=("ariel", 18), width=30, bg="#aed0a4", fg="#e8063b",justify="center")
entryUser.place(x=150, y=380)
global entryPassword
c=StringVar()
entryPassword = Entry(canevas,textvariable=c, font=("ariel", 18), width=30, bg="#aed0a4", fg="#e8063b",justify="center", show="*")
entryPassword.place(x=150, y=440)
global entryCfPassword
h=StringVar()
entryCfPassword = Entry(canevas,textvariable=h, font=("ariel", 18), width=30, bg="#aed0a4", fg="#e8063b",justify='center', show="*")
entryCfPassword.place(x=150, y=500)

c=entryPassword.get()

buttonRegister = Button(root1, text="Se connecter", font=("ariel", 18), padx=6, bg="blue", fg="black",command=moi)
buttonRegister.place(x=500, y=550)



root.mainloop()