# Ejercios Mision Codigo
# Domingo 26
# Dada una matriz cuadrada (n x n) escribe un programa que rote la matriz 90 
# grados en sentido de las manecillas del reloj.

def rotate(mat):
    # para rotarla 90 grados solo cambiamos:
    # primera fila a ultima columna
    # segunda fila a pen ultima columna
    # y asi hasta llegar a fila n
    
    n = len(mat[0])
    
    # mi matriz sera definida por columnas y no filas
    col_mat = [row for row in mat[::-1]]
    #print(col_mat)
    
    # ahora solo cambiamos para que la matriz sea por filas
    rot = []
    for row in range(n):
        rot.append([col[row] for col in col_mat])
        
    return rot


def prt(mat):
    for row in mat:
        for col in row:
            print(col, end=" ")
        print()



def prueba_2x2():
    print("-" * 30)
    print("Probando una Matriz 2x2:")
    mat = [[1, 2], [3, 4]]
    # Esta matriz se ve asi
    # 1 2
    # 3 4
    prt(mat)
    
    print("Rotando 90 Grados")
    mat = rotate(mat)
    prt(mat)
    # Esta matriz se ve asi
    # 3 1
    # 4 2
    
    if mat == [[3, 1], [4, 2]]:
        print("Matriz de 2x2: CORRECTA")
    else:
        print("Matriz de 2x2: INCORRECTA")
        
        
def prueba_3x3():
    print("-" * 30)
    print("Probando una Matriz 3x3:")
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Esta matriz se ve asi
    # 1 2 3
    # 4 5 6
    # 7 8 9
    prt(mat)
    
    print("Rotando 90 Grados")
    mat = rotate(mat)
    prt(mat)
    # Esta matriz se ve asi
    # 7 4 1
    # 8 5 2
    # 9 6 3
    
    if mat == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]:
        print("Matriz de 3x3: CORRECTA")
    else:
        print("Matriz de 3x3: INCORRECTA")
        
    
    
def prueba_4x4():
    print("-" * 30)
    print("Probando una Matriz 4x4:")
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    # Esta matriz se ve asi
    # 1  2  3  4
    # 5  6  7  8
    # 9  10 11 12
    # 13 14 15 16
    prt(mat)
    
    print("Rotando 90 Grados")
    mat = rotate(mat)
    prt(mat)
    # Esta matriz se ve asi
    # 13  9  5  1
    # 14 10  6  2
    # 15 11  7  3
    # 16 12  8  4
    
    if mat == [[13, 9, 5, 1] ,[14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]:
        print("Matriz de 4x4: CORRECTA")
    else:
        print("Matriz de 4x4: INCORRECTA")
        
    
    
# probar varios tamanos de matrices
prueba_2x2()
prueba_3x3()
prueba_4x4()