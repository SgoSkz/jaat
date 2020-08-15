#!/usr/bin/env python
"""
Learning curses.py through experience
    - Create working window
        - Window is resizeable without crashing
        - Working colors
        - Split windows
            - Split size based of terminal size
            - Bordered
        - Text does note go passed column amount
    - User input
        - Text input
        - OPTIONAL: Mouse input
    - Independent modular features
        - Menu
        - Search
        - Information
        - Images
"""

import curses

class MainWindow(object):
    def __init__(self):
        self.description = None
        self.image = None
        self.search = None
        self.list = None

    def setup_curses(self):
        self.std = curses.initscr()

    def initialize(self):
        # Stuff taken from ranger
        self.std.leaveok(0)
        self.std.keypad(1)
        curses.nocbreak()
        curses.noecho()
        curses.curs_set(0)
        curses.halfdelay(20)
        curses.start_color()
        self.update_size()

        # Initiate color pairs
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    def loop(self):
        selWin=Pane(self.lines-3,10,3,0)
        selWin.items = {"test":1, "hello world":2}
        c = self.std.getch()
        while c != ord('q'):
            self.update_size()
            c = self.std.getch()
            selWin.key_handler(c)
            selWin.refresh()

    def update_size(self):
        self.lines, self.columns = self.std.getmaxyx()


# TODO: Add a way for real selections
# Add a way to create or remove items from menu
class Pane():
    def __init__(self, nLines: int, nCols: int, begin_y: int = 0, begin_x: int = 0, box: bool = True):
        self.pane = curses.newwin(nLines, nCols, begin_y, begin_x)
        self.pane.box()
        self.box = box
        self.items = {}
        self.sel = 0

    # NOTE: Made for menu system, generally not used for anything else
    def key_handler(self, key):
        if key == curses.KEY_UP:
            self.sel-=1
        if key == curses.KEY_DOWN:
            self.sel+=1
        if key in [10, 13]:
            self.go = 1
        self.sel %= len(self.items)
        self.menu()

    # Made to display a list of items
    def menu(self):
        for i in range(len(self.items)):
            # Highlight if selected
            if(self.sel == i):
                self.addstr(list(self.items)[i], i+1, 1, 1)
            # Normal if not selected
            else:
                self.addstr(list(self.items)[i], i+1, 1)

    # Add str based on column count
    def addstr(self, string: str, y: int, x: int, color_pair: int=0):
        lines, columns = self.pane.getmaxyx()
        self.pane.addnstr(y, x, string, columns - x, curses.color_pair(color_pair))

    # Clear the screen
    def clear(self):
        self.pane.clear()

    # Refresh the screen
    def refresh(self):
        # NOTE: Might remove the border later
        if(self.box == True):
            self.pane.box()
        self.pane.refresh()

def main():
    try:
        windowMain = MainWindow()
        windowMain.setup_curses()
        windowMain.initialize()
        windowMain.loop()
    except KeyboardInterrupt:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        exit()
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()


if __name__ == "__main__":
    main()
