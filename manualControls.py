import curses
from finch import Finch
import time
import os

screen = curses.initscr()


screen.refresh()
curses.noecho()
screen.keypad(1)
curses.halfdelay(1)


screen.addstr("Use WASD or arrow keys to control bot. Use X to exit controls.")

finch = Finch()

left, right = finch.obstacle()

done = False


while not done:
    key = screen.getch()
    print(key)

    rightWheel = 0.0
    leftWheel = 0.0

    if key == 119 or key == curses.KEY_UP:
        rightWheel = 0.5
        leftWheel = 0.5
    elif key == 115 or key == curses.KEY_DOWN:
        rightWheel = -0.5
        leftWheel = -0.5
    elif key == 100 or key == curses.KEY_RIGHT:
        rightWheel = -0.5
        leftWheel = 0.5
    elif key == 97 or key == curses.KEY_LEFT:
        rightWheel = 0.5
        leftWheel = -0.5
    elif key == 120:
        done = True

    elif key == -1:
        rightWheel = 0.0
        leftWheel = 0.0

    finch.wheels(rightWheel, leftWheel)

    left, right = finch.obstacle()
    screen.refresh()

finch.halt()
finch.close()
curses.endwin()
os.system('stty sane')




