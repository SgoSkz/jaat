#!/usr/bin/env python
"""
Goal:
    - Make window
        - Has panes
            - Menu
                - Selectable items
                    - Items have their own data
                    - Item highlighting
                    - Not dependent on other scripts
            - Title
                - Search
                    - Correctly reads user input
                - Current mode
            - Picture
            - Description
                - No wrap, wrap is ugly
        - Updates size correctly without crashing
        - Scales correctly
    - Watch anime
"""

import re
import curses


# TODO: Make seperate files
class Pane:
    pane = None
    box = True
    def _refresh(self):
        self.main_func()
        if(self.box):
            self.pane.box()
        self.pane.refresh()

    def _update_size(self):
        self.setup()
        self._clear()
        self._refresh()

    def _clear(self):
        self.pane.clear()

    def setup(self):
        pass

    def main_func(self):
        pass

    def addstr(self, y: int, x: int, string: str = "", color_pair: int = 0):
        self.pane.addnstr(y, x, string, self.pane.getmaxyx()[1]-x, curses.color_pair(color_pair))


class MainWindow():
    def __init__(self):
        self.std = curses.initscr()
        self.initialize()

    def __create_panes(self):
        self.menu = Menu()
        self.title = Title()
        self.description = Description()
        self.picture = Picture()

    def initialize(self):
        # Stuff taken from ranger
        self.std.leaveok(0)
        self.std.keypad(1)
        curses.nocbreak()
        curses.noecho()
        curses.curs_set(0)
        curses.halfdelay(20)
        curses.start_color()
        self.__create_panes()

        # Initiate color pairs
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        
    def loop(self):
        self.menu.setup()
        self.title.setup()
        self.description.setup()
        while 1:
            key = self.std.getch()
            if(mainDim != self.std.getmaxyx()):
                self.update_size()
            result = self.menu.key_handler(key)
            self.menu._refresh()
            self.title._refresh()
            self.description._refresh()
            if(result == "quit"):
                break

    def resize_panes(self):
        self.menu._update_size()
        self.title._update_size()
        self.description._update_size()
        self.std.clear()
        self.std.refresh()

    def update_size(self):
        global mainDim
        mainDim = self.std.getmaxyx()
        self.resize_panes()


class Menu(Pane):
    def __init__(self):
        self.sel = 0
        self.items = {1:2,3:4,5:6}

    def setup(self):
        self.pane = curses.newwin(mainDim[0]-3, int(mainDim[1]*(1/2)-1), 3, 0)

    def key_handler(self, key):
        if(key == curses.KEY_UP):
            self.sel-=1
        if(key == curses.KEY_DOWN):
            self.sel+=1
        if(key == ord('q') or key == ord('Q')):
            return "quit"
        if(key in [10, 13]):
            return self.items[list(self.items)[self.sel]]
        if(key == curses.KEY_BACKSPACE):
            return "back"
        self.sel %= len(self.items)
        return None

    def main_func(self):
        self.list_items()

    def list_items(self):
        for i in range(len(self.items)):
            if(self.sel == i):
                self.addstr(i+1, 1, str(list(self.items)[i]), 1)
            else:
                self.addstr(i+1, 1, str(list(self.items)[i]), 0)


class Title(Pane):
    def __init__(self):
        self.title = ""

    def setup(self):
        self.pane = curses.newwin(3, mainDim[1], 0, 0)

    def main_func(self):
        self.addstr(1, 1, self.title, 2)

class Picture(Pane):
    def __init__(self):
        self.picturePath = ""


class Description(Pane):
    def __init__(self):
        self.description = ""

    def setup(self):
        self.pane = curses.newwin(
                int((mainDim[0]-3)*(1/2)+1),
                int(mainDim[1]*(1/2)+1),
                int(2+(mainDim[0]-3)*(1/2)),
                int(mainDim[1]*(1/2)-1))

    def main_func(self):
        pass

def main():
    try:
        windowMain = MainWindow()
        windowMain.initialize()
        windowMain.update_size()
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
