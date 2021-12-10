#
# Vamos a hacer un script que resuelve Problemas de SUDOKU
#

import copy
from selenium import webdriver
import pyautogui as pg
import time

# Etapa 1
# Tenemos un SUDOKU
# Los espacios vacios estan representados con un cero

def print_sudoku(sudoku):
    for l in sudoku:
        print(l)


class Sudoku ():
    def __init__(self):
        self.prob = None
        self.solucion = []

    def def_sudoku(self, sudoku):
        self.prob = sudoku

    def print(self):
        print_sudoku(self.prob)

    def leer_ny_times(self, dificulad='hard'):
        # esta funcion lee de sudoku.com usando selenium
        self.dificultad = dificulad

        driver = webdriver.Firefox()
        self.driver = driver

        url = "https://www.nytimes.com/puzzles/sudoku/" + dificulad
        print("Leyendo SUDOKU de {}".format(url))
        driver.get(url)

        time.sleep(2)  # Wait for expert mode to load

        sudoku_dict = {}
        grid = driver.find_element_by_class_name("su-board")
        for e in grid.find_elements_by_tag_name("div"):
            cell = e.get_attribute("data-cell")
            val = e.get_attribute("aria-label")
            if cell is None or val is None:
                continue
            sudoku_dict[int(cell)] = 0 if val == 'empty' else int(val)

        #print(sudoku_dict)

        # ahora solo tenemos que cambiar el diccionario a nuestro formato de listas
        # queremos una lista por fila. Es decir 9 listas de 9 elementos
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

        self.def_sudoku(sudoku)

    def encontrar_coordenada_3x3(self, x):
        if x <= 2:
            return 0
        elif x <= 5:
            return 1
        else:
            return 2

    def grid_3x3_para_celda(self, x, y):
        col_3x3 = self.encontrar_coordenada_3x3(x)
        fila_3x3 = self.encontrar_coordenada_3x3(y)

        grid = []
        for fila in self.prob[fila_3x3 * 3: fila_3x3 * 3 + 3]:
            for col in fila[col_3x3 * 3: col_3x3 * 3 + 3]:
                grid.append(col)

        return grid

    def posible(self, x, y, n):
        #print("Posible {} en ({}, {})".format(n, x, y))
        # Revisar Fila
        if n in self.prob[y]:
            #print(self.prob[y])
            return False

        # Revisar Columna
        # primero vamos a hacer una lista de los valores en la columna
        col = [fila[x] for fila in self.prob]
        if n in col:
            #print(col)
            return False

        # revisar grid 3x3
        # primero hay que encontrar en que grid esta
        # hay 9
        grid3x3 = self.grid_3x3_para_celda(x, y)
        if n in grid3x3:
            #print(grid3x3)
            return False

        return True

    def resolver(self):
        for y in range(9):
            for x in range(9):
                if self.prob[y][x] == 0:
                    for v in range(1,10):
                        if self.posible(x, y, v):
                            self.prob[y][x] = v
                            #print()
                            #self.print()
                            #print()
                            self.resolver()
                            #print("Backtrack {},{}".format(x,y))
                            self.prob[y][x] = 0
                    return
        self.solucion.append(copy.deepcopy(self.prob))
        return

    def subir_solucion(self):
        if len(self.solucion) == 0:
            print("No encontre solucion...")
            return

        # cuando carga la pagina el cursor esta en el primer cuadro
        # asi que solo presionaremos la tecla y luego nos movemos a la derecha
        
        sudoku_sol = {}
        cell = 0
        for row in self.solucion[0]:
            for col in row:
                sudoku_sol[str(cell)] = str(col)
                cell += 1
                pg.press(str(col))
                pg.hotkey("right")
                
            # once the column is done we move to the first position
            pg.press("down")
            pg.press('left', presses=8)

        #print(sudoku_sol)
        
        return
    
        grid = self.driver.find_element_by_class_name("su-board")
        for e in grid.find_elements_by_tag_name("div"):
            cell = e.get_attribute("data-cell")
            val = e.get_attribute("aria-label")
            if val == 'empty':
                # ahora solo tenemos que mandar la solucion
                # para esto voy a usar pyautogui porque ny times tiene funciones que no nos dejan usar selenium
                # obtenedremos las coordenadas del elemento
                x_coord = e.location['x']
                y_coord = e.location['y']
                print("Presionando coordenada {}, {} con {}".format(x_coord, y_coord, sudoku_sol[cell]))
                #pg.click(x=x_coord, y=y_coord)
                pg.press(sudoku_sol[cell])
                


        print("Listo ;)")


    def print_solucion(self):
        if len(self.solucion) == 0:
            print("Sin Solucion")
        for i, s in enumerate(self.solucion):
            print("Solucion {}".format(i + 1))
            print_sudoku(s)

    def probar(self):
        # probemos uno que no pueda estar en la fila
        print(s.posible(0, 0, 1))

        # probemos uno que no pueda estar en columna pero si en fila
        print(s.posible(2, 0, 8))

        # ahora uno que si pueda estar en fila y columna pero no en grid 3x3
        print(s.posible(4, 0, 2))
        print(s.posible(4, 7, 2))
        print(s.posible(4, 7, 4))
        print(s.posible(4, 7, 5))

def sudoku_manual():
    s1 = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
    return s1


s = Sudoku()
#s.def_sudoku(sudoku_manual())
s.leer_ny_times("hard")
s.print()

#sys.exit(1)

print()
print()
#s.probar()
print("Resolviendo ...")
s.resolver()
s.print_solucion()

s.subir_solucion()
