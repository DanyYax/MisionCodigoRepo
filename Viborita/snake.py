#
# Let´s do a SNAKE game
# RETRO style
#

import curses
import random

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
    win.addch(food[0], food[1], "O")

    # This is the execution Loop that
    # will be running all the time our screen is active meaning
    # while the game is running
    while True:

        # define a new head of the snake
        nhead = None

        # check for collisions to wall
        if snk[0][0] in (0, sh) or snk[0][1] in (0, sw) or snk[0] in snk[1:]:
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

        # Check if the snake ate the food
        if snk[0] == food:
            food = None

            # increase velocity
            win.timeout(int(vel * 0.98))
            # Increase the score
            score += 1
            win.addstr(0, int(sw * 0.8), "SCORE: {} ".format(score), curses.color_pair(1))

            while food is None:
                new_food = (random.randint(1, sh - 1), random.randint(1, sw - 1))

                # check that the position is free (no snake)
                if new_food in snk:
                    new_food = None
                else:
                    food = new_food
            win.addch(food[0], food[1], "O")
        else:
            # Erase the tail from the screen
            tail = snk.pop()
            win.addch(tail[0], tail[1], " ")

        # now we can draw the new head
        win.addch(nhead[0], nhead[1], curses.ACS_BLOCK)

    print("GAME OVER")

curses.wrapper(main)