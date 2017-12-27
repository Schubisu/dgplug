import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
from timeit import Timer
import time

directions = {
    curses.KEY_UP: (-1, 0),
    curses.KEY_DOWN: (1, 0),
    curses.KEY_LEFT: (0, -1),
    curses.KEY_RIGHT: (0, 1),
}


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.segments = 5
        self.pos = [(10, 40)] * self.segments
        self.dir = directions[curses.KEY_LEFT]
        self.refresh = 0.100
        t = Timer()
        self.timer = t.timer
        self.last_update = self.timer()


    def update(self):
        t = self.timer()
        if (t - self.last_update) < self.refresh:
            return
        self.screen.addch(*self.pos[0], ord("o"))
        self.pos.insert(0, tuple(
            old + new for old, new in zip(
                self.pos[0], self.dir
            )
        ))
        self.screen.addch(*self.pos[0], ord("O"))

        self.screen.addch(*self.pos[-1], ord(" "))
        self.pos.remove(self.pos[-1])

        self.screen.refresh()
        self.last_update = self.timer()


def main(stdscr):
    stdscr.border(0)
    stdscr.addstr(12, 25, "This is a test")
    curses.curs_set(False)
    stdscr.refresh()
    stdscr.nodelay(True)

    s = Snake(stdscr)

    while True:
        key = stdscr.getch()
        if key in directions.keys():
            s.dir = directions[key]
        s.update()
        time.sleep(0.01)


if __name__ == "__main__":
    wrapper(main)

