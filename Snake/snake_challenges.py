#
# Let´s do a SNAKE game
# RETRO style
#
""" Code by Dany Jacquez
for video tutorial in Youtube Mision Codigo:
Watch it here:

Extra Challenges implemented:
 - Change the character for the food and maybe the snake:
 Solution: change the third parameter in the lines that draw the food

 - Add a time limit for each food.
 Solution: Add a timer variable, in the main loop check the current time
    and compare it to the time when food was created. If the time is
    larger than limit time then set food to None

 - Create a new screen with more walls after player's score
   reaches 10
 Solution: Monitor the score in the main loop, once the wanted score is reached
 trigger a function to define and draw walls. Store the walls in a list and
 add collision checks in the main loop.
"""


import curses
import random
import time


def draw_lev2(win, sh, sw):
    """
    Function to change to level 2
    This means drawing different walls


    PROBLEMS: This way of changing level layout can have 2 problems not handled here
        1. Snake may be on the wall or immediately crash into wall
        Solution: pause Snake and move it to a safe place to give player time to react
        2. a Food piece may be in the place where the new wall is set
        Solution: Since our food has a life and then it is redefined this is not a big issue
    """
    # define the walls for level 2
    wall = []
    x = int(sw / 4)
    x2 = int(3 * sw / 4)
    for y in range(int(sh / 4), int(3 * sh / 4)):
        # Define coordinate in left side of screen
        wall.append((y, x))
        win.addstr(y, x, "|")
        # define at right side of screen
        wall.append((y, x2))
        win.addstr(y, x2, "|")
    return wall


def create_random_food(sh, sw, restricted_locs):
    """
    Creates a food piece in a random position within the screen height and width
    returns food location and the time it was created at (seconds)
    sh: Screen Height
    sw: Screen Width
    resctricted_locs: list of tuples definining coordinates where food
                      can't be located
    """
    food = None
    food_start_sec = None

    while food is None:
        new_food = (random.randint(1, sh - 1), random.randint(1, sw - 1))

        # check that the position is free
        if new_food in restricted_locs:
            new_food = None
        else:
            food = new_food
            food_start_sec = time.time()
    return (food, food_start_sec)


def main(stdscr):
    stdscr.clear()
    sh = 30
    sw = 90

    # Let's create our Game Screen
    win = curses.newwin(sh + 1, sw + 1, 0, 0)

    # Define 2 color pairs in order to change colors in our screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)

    win.attron(curses.color_pair(2))
    win.border()
    win.attroff(curses.color_pair(2))

    # Listen for key presses
    win.keypad(True)

    # starting velocity of the game
    vel = 100
    win.timeout(vel)

    # Keep track of the score
    score = 0
    win.addstr(0, int(sw * 0.8), "SCORE: {} ".format(score), curses.color_pair(1))

    # Challenge 3:
    # Define variable to know score to move to next level
    lev2_score = 3
    # keep track of what is the current level
    level_now = 1
    # Also keep a list of the wall positions.
    # It will be empty until player goes to level 2
    walls = []

    # Implement the Snake
    vib_x = int(sw / 4)
    vib_y = int(sh / 2)

    snk = [
        (vib_y, vib_x),
        (vib_y, vib_x - 1),
        (vib_y, vib_x - 2)
    ]

    # define our starting movement direction
    d = curses.KEY_RIGHT

    # Create the first food
    # always in the center of the screen
    food = (int(sh / 2), int(sw / 2))
    win.addch(food[0], food[1], curses.ACS_PI)
    # Keep track of time when food was created
    food_start_sec = time.time()
    # Set max time the food will be available in seconds
    food_max_time = 5

    # This is the execution Loop that
    # will be running all the time our screen is active meaning
    # while the game is running
    while True:

        # define a new head of the snake
        nhead = None

        # check for collisions to wall
        if snk[0][0] in (0, sh) or snk[0][1] in (0, sw) or snk[0] in snk[1:] or snk[0] in walls:
            # We crashed
            curses.endwin()
            print("GAME OVER")
            quit()

        key = win.getch()
        if key == -1:
            #no change in direction required
            d = d
        else:
            d = key

        if d == ord('q'):
            break
        if d == curses.KEY_RIGHT or d == 454:
            nhead = (snk[0][0], snk[0][1] + 1)
        elif d == curses.KEY_LEFT or d == 452:
            nhead = (snk[0][0], snk[0][1] - 1)
        elif d == curses.KEY_UP or d == 450:
            nhead = (snk[0][0] - 1, snk[0][1])
        elif d == curses.KEY_DOWN or d == 456:
            nhead = (snk[0][0] + 1, snk[0][1])

        snk.insert(0, nhead)

        # calculate the time the food has been available
        food_age = time.time() - food_start_sec

        # challenge 2 add another check that the food expired
        if food_age > food_max_time:

            # We need to erase the food
            win.addch(food[0], food[1], " ")
            # our food is gone so reset the timer for it
            food_start_sec = None

            # get new food
            food, food_start_sec = create_random_food(sh, sw, snk)
            win.addch(food[0], food[1], curses.ACS_PI)

        # Check if the snake ate the food
        if snk[0] == food:
            # increase velocity
            win.timeout(int(vel * 0.98))
            # Increase the score
            score += 1
            win.addstr(0, int(sw * 0.8), "SCORE: {} ".format(score), curses.color_pair(1))

            # CHALLENGE 3
            # check if new walls must be drawn
            if level_now == 1 and score >= lev2_score:
                walls = draw_lev2(win, sh, sw)

            # get new food
            food, food_start_sec = create_random_food(sh, sw, snk)
            win.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Erase the tail from the screen
            tail = snk.pop()
            win.addch(tail[0], tail[1], " ")

        # now we can draw the new head
        win.addch(nhead[0], nhead[1], curses.ACS_BLOCK)

    print("GAME OVER")

curses.wrapper(main)