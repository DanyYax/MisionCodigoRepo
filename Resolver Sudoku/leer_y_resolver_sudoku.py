from selenium import webdriver
import time

def leer_ny_times_sudoku(dificultad="hard"):
    
    driver = webdriver.Firefox()
    url = "https://www.nytimes.com/puzzles/sudoku/" + dificultad
    print("Leyendo SUDOKU desde {}".format(url))
    driver.get(url)
    
    time.sleep(2)
    
    sudoku_dict = {}
    grid = driver.find_element_by_class_name("su-board")
    for el in grid.find_elements_by_tag_name("div"):
        cell = el.get_attribute("data-cell")
        val = el.get_attribute("aria-label")
        if cell is None or val is None:
            continue
        sudoku_dict[int(cell)] = 0 if val == "empty" else int(val)
    #print (sudoku_dict)
    
    # pasarlo a la estructura de datos que necesitamos
    sudoku = []
    x = 0
    y = 0
    for i in range(81):
        if x == 9:
            y += 1
            x = 0
        if x == 0:
            sudoku.append([])
            
        sudoku[y].append(sudoku_dict[i])
        x += 1
        
    print_sudoku(sudoku)
    print()
    return sudoku


def sudoku_manual():
    sudoku = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]
    return sudoku


def print_sudoku(sudoku):
    for l in sudoku:
        print(l)

def encontrar_coordenada_grid(val):
    if val <= 2:
        return 0
    elif val <= 5:
        return 1
    else:
        return 2

def obtener_grid_para_celda(x, y, sudoku):
    subgrid_col = encontrar_coordenada_grid(x)
    subgrid_fila = encontrar_coordenada_grid(y)
    
    grid = []
    for fila in sudoku[subgrid_fila *3: subgrid_fila *3 + 3]:
        for col in fila[subgrid_col *3: subgrid_col *3 + 3]:
            grid.append(col)
            
    return grid


def es_posible(x, y, v, sudoku):
    # Revisar la fila
    if v in sudoku[y]:
        return False
    
    # revisar la columna
    col = [fila[x] for fila in sudoku]
    if v in col:
        return False
    
    # Revisar sub grid 3x3
    grid3x3 = obtener_grid_para_celda(x, y, sudoku)
    if v in grid3x3:
        return False
    
    return True


def resolver_sudoku(sudoku):
    """
    Esta implementación es casi la misma que la de resolver_sudoku1
    Pero aqui regresamos un bool indicando si ya fue resuelto
    o no
    Esto nos permite terminar el algoritmo cuando se encuentra una solución
    El sudoku original es actualizado y contiene la respuesta
    """
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0:                
            
                for valor in range(1,10):
                    
                    if es_posible(columna,fila,valor,sudoku):
                        
                        sudoku[fila][columna] = valor
                        resuelto = resolver_sudoku(sudoku)
                        if resuelto:
                            return True
                        sudoku[fila][columna] = 0
                        
                return False
    #print_sudoku(sudoku)
    return True

#s = sudoku_manual()
s = leer_ny_times_sudoku()

resolver_sudoku(s)
#es_posible(6, 8, 3, sudoku)