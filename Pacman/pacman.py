import turtle

DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]


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

    pacman = Character(s, "Pacman", "yellow")
    pacman.draw()
    # pacman.move()
    
    # t = turtle.Turtle()
    # t.forward(100)
    # t.right(90)
    # t.forward(100)
    
    # colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    # t = turtle.Pen()
    # turtle.bgcolor('black')
    # turtle.speed("fast")
    # for x in range(360):
    #     t.pencolor(colors[x%6])
    #     t.width(x//100 + 1)
    #     t.forward(x)
    #     t.left(59)
    
    s.onkeypress(pacman.move_up, "Up")
    s.onkeypress(pacman.move_down, "Down")
    s.onkeypress(pacman.move_right, "Right")
    s.onkeypress(pacman.move_left, "Left")
    turtle.listen()
    
    # s.mainloop()
    while True:
        pacman.move()
        s.update()