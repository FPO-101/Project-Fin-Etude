
import numpy as np
from scipy.linalg import solve
from numpy.linalg import inv
from numpy.linalg import *
from numpy import array, zeros, diag, diagflat, dot
from scipy import linalg
def input_matrix():
    matrix=[]
    col=[]
    no_of_row=int(input("enter no. of rows ::  "))
    no_of_col = int(input("enter no. of columns ::  "))
    for ir in range(1,no_of_row+1):
        for ic in range(1,no_of_col+1):
            print("Enter value of a",ir,ic)
            val=int(input())
            col.append(val)
        matrix.append(col)
        col=[]
    return no_of_row,no_of_col,matrix
#Addition
#############################################################################
def addition_of_matrix(matrixA,matrixB):
    addition_matrix=[]
    addition_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    if no_of_rowA==no_of_rowB and no_of_colA==no_of_colB:
        for r in range(no_of_rowA):
            for c in range(no_of_colA):
                val = matrixA[r][c] + matrixB[r][c]
                addition_col.append(val)
            addition_matrix.append(addition_col)
            addition_col = []
    return addition_matrix

#################################################################################
#subtraction
def subtraction_of_matrix(matrixA,matrixB):
    subtraction_matrix=[]
    subtraction_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    if no_of_rowA==no_of_rowB and no_of_colA==no_of_colB:
        for r in range(no_of_rowA):
            for c in range(no_of_colA):
                val = matrixA[r][c] - matrixB[r][c]
                subtraction_col.append(val)
            subtraction_matrix.append(subtraction_col)
            subtraction_col = []
    return subtraction_matrix
#########################################################################################################################################3
#produit
def produit_of_matrix(matrixA,matrixB):
    produit_matrix=[]
    produit_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    val=0
    for i in range(no_of_rowA):
        for j in range(no_of_colB):
            for k in range(no_of_colA):
                val = val + (matrixA[i][k] * matrixB[k][j])
            produit_col.append(val)
            val=0
        produit_matrix.append(produit_col)
        produit_col = []
    return produit_matrix
#######################################################################################
#gauss
def gaus_of_matrix(a,b,x,n):
    v=[]

    L=np.tril(a)
    U=a-L
    for i in range(n):
        x=np.dot(np.linalg.inv(L),b-np.dot(U,x))
        #b = np.array(x, dtype='float16')
        #print(x)
    c= np.array(x, dtype="float16")
    v.append(c)
    return c
#######################################################################################
#jacobi
def jacobi_of_matrix1234(A, b, x,n):

    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(n):
        x = ((b - np.dot(R, x)) / D)
    c = np.array(x, dtype="float16")
    return c

#######################################################################################
#Methode direct
def lu_of_matrix1(A):
    rows, columns = np.shape(A)
    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))
    for i in range(columns):
        for j in range(i):
            total = 0
            for k in range(j):
                total += lower[i][k] * upper[k][j]
            lower[i][j] = (A[i][j] - total) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            total = 0
            for k in range(i):
                total += lower[i][k] * upper[k][j]
            upper[i][j] = A[i][j] - total
    return lower
########################################################################################################################
def Qr_of_matrix(A, type=float):
    A = np.array(A, dtype=type)
    n = len(A)
    m = len(A[0])

    Q = np.array(A, dtype=type)
    R = np.zeros((n, n), dtype=type)

    for k in range(n):
        for i in range(k):
            R[i, k] = np.transpose(Q[:, i]).dot(Q[:, k]);
            Q[:, k] = Q[:, k] - R[i, k] * Q[:, i];

        R[k, k] = linalg.norm(Q[:, k]);
        Q[:, k] = Q[:, k] / R[k, k];
    c = np.array(Q, dtype="float16")
    return c
def Rq_of_matrix(A, type=float):
    A = np.array(A, dtype=type)
    n = len(A)
    m = len(A[0])

    Q = np.array(A, dtype=type)
    R = np.zeros((n, n), dtype=type)

    for k in range(n):
        for i in range(k):
            R[i, k] = np.transpose(Q[:, i]).dot(Q[:, k]);
            Q[:, k] = Q[:, k] - R[i, k] * Q[:, i];

        R[k, k] = linalg.norm(Q[:, k]);
        Q[:, k] = Q[:, k] / R[k, k];
        c = np.array(R, dtype="float16")

    return c
########################################################################################################################
def lu_of_matrix(A):
    rows, columns = np.shape(A)
    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))
    for i in range(columns):
        for j in range(i):
            total = 0
            for k in range(j):
                total += lower[i][k] * upper[k][j]
            lower[i][j] = (A[i][j] - total) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            total = 0
            for k in range(i):
                total += lower[i][k] * upper[k][j]
            upper[i][j] = A[i][j] - total
    return upper
####################################################################################
#cholesky
def chol_of_matrix(A):
    B = np.linalg.cholesky(A)
    b = np.array(B, dtype='float16')
    return b


###############################################################################
def cofactor_matrix(matrix):
    cofactor = None
    cofactor = np.linalg.inv(matrix).T * np.linalg.det(matrix)
    a=cofactor
    b = np.array(a, dtype='float16')

    # return cofactor matrix of the given matrix
    return b
###############################################################################
#inverse
def inverse_of_matrix(matrix):
    ainv = np.linalg.inv(matrix)
    a=ainv
    b = np.array(a, dtype='float16')
    return b


################################################################################
#adjoint
def adjoint_of_matrix(matrix):
    cofac=cofactor_matrix(matrix)
    adjoint=transpose(cofac)
    a=adjoint
    b = np.array(a, dtype='float16')
    return adjoint


#determinant

def main_determinant( matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    def det(matrix, n):
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        ret = 0
        for i in range(n):
            if i % 2 == 0:
                ret += matrix[0][i] * det([row[:i] + row[i + 1:] for row in matrix[1:]], n - 1)
            else:
                ret -= matrix[0][i] * det([row[:i] + row[i + 1:] for row in matrix[1:]], n - 1)
        return ret

    return det(matrix,n)
#Tranpose

def transpose(matrix):
    row_len=len(matrix)
    col_len=len(matrix[0])
    row_tr=[]
    transpose_matrix=[]
    for z in range(col_len):
        for e in range(row_len):
            row_tr.append(matrix[e][z])
        transpose_matrix.append(row_tr)
        row_tr=[]
    return transpose_matrix

#########################################################################################################################
def cofactor_matrix12(A,b,x):
    tol = 1e-16
    # tol définie la précision seuil
    err = 0
    itmax = 300000
    # itmax est le nombre d'itération maximal
    s = 0
    w = 0.1
    # 0 <w <1 , est un facteur de relaxation qui modifie un peu l'algo, c'est pour amener
    # le système à converger.En effet il se peut que le système ne converge pas pour certaine matrice
    for k in range(itmax):
        err = 0
        for i in range(len(A)):
            s = 0
            xprim = x[i]
            for j in range(len(A)):
                if i != j:
                    s += sum(A[i][j] * x[j])
            x[i] = w * ((b[i] - sub(s)) / A[i][i]) + (1 - w) * x[i]
            err = err + fabs((x[i] - xprim))
        if err < tol:
            #print('Nombre d\' iterations', k, 'Erreur', float(err))
            #print(" la solution de votre système est:", x)
            return x
            break

#################################################
"""
#cofactor
def cofactor_matrix1(matrix):
    tol = 1e-16
    # tol définie la précision seuil
    err = 0
    itmax = 300000
    # itmax est le nombre d'itération maximal
    s = 0
    w = 0.1
    # 0 <w <1 , est un facteur de relaxation qui modifie un peu l'algo, c'est pour amener
    # le système à converger.En effet il se peut que le système ne converge pas pour certaine matrice
    for k in range(itmax):
        err = 0
        for i in range(len(A)):
            s = 0
            xprim = x[i]
            for j in range(len(A)):
                if i != j:
                    s = s + A[i][j] * x[j]
            x[i] = w * ((b[i] - s) / A[i][i]) + (1 - w) * x[i]
            err = err + fabs((x[i] - xprim))
        if err < tol:
            print('Nombre d\' iterations', k, 'Erreur', float(err))
            print(" la solution de votre système est:", x)
            break



   

def transpose1(matrix):
    row_len=len(matrix)
    col_len=len(matrix[0])
    row_tr=[]
    transpose_matrix=[]
    for z in range(col_len):
        for e in range(row_len):
            row_tr.append(matrix[e][z])
        transpose_matrix.append(row_tr)
        row_tr=[]
    return transpose_matrix
"""
"""
def transpose(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j]
        #for r in Result:
    return result
"""
"""
def gaus_of_matrix1(a, b):
    # Finding length of a(3)
    x = [0, 0, 0]
    c=np.array(a)
    e=np.array(b)
    s=np.array(x)
    n = len(a)

    # for loop for 3 times as to calculate x, y , z
    for j in range(0, n):
        # temp variable d to store b[j]
        d = e[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d = d - c[j][i] * s[i]
        # updating the value of our solution
        s[j] = d / c[j][j]
    # returning our updated solution
    return s

def gaus_of_matrix2(a,b):
    x = [0,0,0]
    #b=[105,155,65]
    c = b.copy()
    subtraction_matrix = []
    subtraction_col = []
    no_of_rowA = len(a)
    no_of_colA = len(a[0])

    data_type = object
    v = []
    n = 6
    L = np.tril(a)
    U = a - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), c - np.dot(U, x))
        # b = np.array(x, dtype='float16')
        # print(x)
    for r in range(no_of_colA):
        # for c in range(no_of_colA):
        val = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    subtraction_col.append(val)
    subtraction_matrix.append(subtraction_col)
    subtraction_col = []
    c = np.array(subtraction_matrix, dtype="float16")
    v.append(c)
    return c
def gaus_of_matrix23(A,b):
    ITERATION_LIMIT = 1000
    c= np.array(b)

    #print("System of equations:")
    for i in range(len(A[0])):
        row = ["{0:3g}*x{1}".format(A[i][j], j + 1) for j in range(len(A[1]))]
        # print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

    x = np.zeros_like(b)
    for it_count in range(1, ITERATION_LIMIT):
        x_new = np.zeros_like(x)
        # print("Iteration {0}: {1}".format(it_count, x))
        for i in range(len(A[0])):
            s1 = np.dot(A[i][:i], x_new[:i])
            s2 = np.dot(A[i][ i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i][ i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new
    c = np.array(x, dtype="float")
    return c
"""


def jacobi_of_matrix1(A, b, x,n):
    D = np.diag(A)

    R = A - np.diagflat(D)


    for i in range(n):
        x = (b - np.dot(R, x)) / D

    c = np.array(x, dtype="float")

    return c


def ana12(A, b,n):
    x = np.zeros_like(b)
    for it_count in range(n):
        if it_count != 0:
            print("Iteration {0}: {1}".format(it_count, x))
        x_new = np.zeros_like(x)
        for i in range(len(A[0])):
            s1 = np.dot(A[i][i], x[i])
            s2 = np.dot(A[i][i + 1], x[i + 1])
            x_new[i] = (b[i] - s1 - s2) / A[i][ i]
            if x_new[i] == x_new[i - 1]:
                break
                # if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        # break
        x = x_new

    return x
def moi(A,b):
    x = np.linalg.solve(A, b)
    return x