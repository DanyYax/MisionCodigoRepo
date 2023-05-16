import turtle

DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
TILE_SIZE = 20


def draw_tile(t: turtle.Turtle, w: float):
    t.begin_fill()
    for _ in range(4):
        t.forward(w)
        t.right(90)
    t.end_fill()
    
    
class GameStage:
    def __init__(self, width: int, height: int) -> None:
        self.sw = width 
        self.sh = height
        self.grid_x = 0
        self.grid_y = 0
        self.grid = None
        
        self.grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        
        # self.grid = [
        #     [1, 1],
        #     [1, 1],
        # ]

        self.grid_x = len(self.grid[0])
        self.grid_y = len(self.grid)
        print(f"Game Grid is {self.grid_x} X {self.grid_y}")
        
        # Calcular tamaño de cuadricula
        self.tile_width = self.sw / self.grid_x
        
        return
    
    def draw(self) -> None:
        t = turtle.Turtle()
        turtle.tracer(0, 0)
        t.fillcolor("blue")
        
        t.penup()
        t.goto(-self.sw * 0.5, self.sh * 0.5)
        
        t.pendown()
        for col_id, col in enumerate(self.grid):
            for row_id, val in enumerate(col):
                t.fillcolor("blue")
                if val == 1:
                    t.fillcolor("red")
                # Dibujar un cuadrado
                draw_tile(t, self.tile_width)
                t.forward(self.tile_width)
            t.right(90)
            t.forward(self.tile_width)
            t.right(90)
            t.forward(self.tile_width * self.grid_x)
            t.right(180)

        turtle.update()


class Character:
    def __init__(self, game_screen, name: str, color: str) -> None:
        self.game_screen = game_screen
        
        self.t = turtle.Turtle()
        self.color = color
        self.name = name
        self.size = 5
        
        # self.direction = "RIGHT"
       
    def draw(self) -> None:
        print(f"Dibujando a {self.name}")
        self.t.shape("circle")
        self.t.pen(fillcolor="yellow")
        self.t.shapesize(5)
        self.t.penup()
        
        # point our turtle in the right direction
        # For now point always to the right
        self.t.setheading(0)
        
        turtle.update()
        
        
    def move(self) -> None:
        # print(f"Moviendo a {self.name}")
        self.t.forward(1)
        
    def move_up(self) -> None:
        print(f"Moviendo a {self.name} para arriba")
        self.t.setheading(90)

    def move_down(self) -> None:
        print(f"Moviendo a {self.name} para abajo")
        self.t.setheading(270)
    
    def move_right(self) -> None:
        print(f"Moviendo a {self.name} para la derecha")
        self.t.setheading(0)

    def move_left(self) -> None:
        print(f"Moviendo a {self.name} para la izquierda")
        self.t.setheading(180)


if __name__ == '__main__':
    s = turtle.Screen()
    s.title("Pac-Man")
    
    screen_width = 650
    screen_height = 800
    s.setup(screen_width, screen_height)

    game_stage = GameStage(screen_width - 50, screen_height - 100)
    game_stage.draw()

    # pacman = Character(s, "Pacman", "yellow")
    # pacman.draw()
    
    # s.onkeypress(pacman.move_up, "Up")
    # s.onkeypress(pacman.move_down, "Down")
    # s.onkeypress(pacman.move_right, "Right")
    # s.onkeypress(pacman.move_left, "Left")
    turtle.listen()
    
    # s.mainloop()
    while True:
        # pacman.move()
        s.update()