# Interview problem by Google

class TicTacToe(object):
    def __init__(self, n):
        self.n = n
        # define a board
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.winner = None

    def move(self, row, col, player):
        if self.winner is not None :
            print("El juego a terminado")
            return 
        self.board[row][col] = player
        return self.win(player)

    def win(self, player):
        # check if the horizonal won
        for row in self.board:
            if all([True if e == player else False for e in row]):
                return player
            
        # check Vertical
        v = [[i[c] for i in self.board] for c in range(self.n)]
        for each in v:
            if all([True if e == player else False for e in each]):
                return player
            
        # revisar Diagonal
        # hay dos diagonales nadamas
        d1 = []
        d2 = []
        for c, row in enumerate(self.board):
            d1.append(row[c])
            d2.append(row[self.n -1 -c])
        
        if all([True if e == player else False for e in d1]):
            return player
        if all([True if e == player else False for e in d2]):
            return player
        
        return None

    def __str__(self):
        return str(self.board)


def test_1():
    board = TicTacToe(3)
    board.move(0, 0, 1)
    board.move(0, 2, 2)
    board.move(2, 2, 1)
    board.move(1, 1, 2)
    board.move(2, 0, 1)
    board.move(1, 0, 2)
    won = board.move(2, 1, 1)
    if won == 1:
        print("Prueba 1:     Correcta")
    else:
        print("Prueba 1:     Incorrecta")
        
def test_2():
    board = TicTacToe(3)
    board.move(0, 0, 1)
    board.move(1, 1, 2)
    board.move(2, 2, 1)
    board.move(1, 0, 2)
    board.move(2, 0, 1)
    won = board.move(1, 2, 2)
    if won == 2:
        print("Prueba 2:     Correcta")
    else:
        print("Prueba 2:     Incorrecta")
        
def test_3():
    board = TicTacToe(3)
    board.move(0, 0, 1)
    board.move(1, 1, 2)
    board.move(0, 2, 1)
    board.move(1, 0, 2)
    won = board.move(0, 1, 1)
    if won == 1:
        print("Prueba 3:     Correcta")
    else:
        print("Prueba 3:     Incorrecta")

# aqui agrega las pruebas
test_1()
test_2()
test_3()