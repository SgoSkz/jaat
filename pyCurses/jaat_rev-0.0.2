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
import _4anime

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

    def addstr(self, y: int, x: int, string: str = "", color_pair: int = 0, wrapping: bool = False):
        if(not(wrapping)):
            self.pane.addnstr(y, x, string, self.pane.getmaxyx()[1], curses.color_pair(color_pair))
        else:
            j = 0
            row = [""]
            strings = string.split()
            for i in range(len(strings)):
                if self.pane.getmaxyx()[1] > len(row[j] + strings[i])+1:
                    row[j] += strings[i]+" "
                else:
                    if(j+3 < self.pane.getmaxyx()[0]):
                        row.append("")
                        j+=1
                    continue
            for i in range(len(row)):
                self.addstr(i+1, 1, row[i], 0)


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
            # FIXME: Pages not loading because of key not yet registered
            key = self.std.getch()
            # Compares main window size with last known
            if(mainDim != self.std.getmaxyx()):
                self.update_size()
            result = self.menu.key_handler(key)
            if(self.menu.animes == self.menu.items and len(list(self.menu.animes))>0):
                self.menu.currentAnime = _4anime.Anime(self.menu.items[list(self.menu.items)[self.menu.sel]])
                self.menu.currentAnime.get_info()
                self.description.description = self.menu.currentAnime.description
            self.refresh_panes()
            if(result == "quit"):
                break
            elif(result == "search"):
                self.search()
            elif(result in list(self.menu.animes)):
                self.menu.currentAnime = _4anime.Anime(self.menu.items[result])
                self.episodes()
            elif(result in list(self.menu.episodes)):
                self.watch()

    # TODO: Add support for watching videos
    def watch(self):
        pass

    def episodes(self):
        self.menu.currentAnime.enumerate_episodes()
        self.menu.episodes = self.menu.currentAnime.enumerated_ep
        self.menu.items = self.menu.episodes
        self.refresh_panes()

    def search(self):
        self.title.search()
        self.menu.animes = _4anime.search(self.title.query)
        self.menu.items = self.menu.animes
        self.refresh_panes()

    def refresh_panes(self):
        self.menu._refresh()
        self.title._refresh()
        self.description._refresh()

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
        self.animes = {}
        self.currentAnime = None
        self.episodes = {}
        self.items = {}
        self.sel = 0

    def setup(self):
        self.pane = curses.newwin(mainDim[0]-3, int(mainDim[1]*(1/2)-1), 3, 0)

    # TODO: Find faster method
    def key_handler(self, key):
        if(key == curses.KEY_UP):
            self.sel-=1
        if(key == curses.KEY_DOWN):
            self.sel+=1
        if(key == ord('r') or key == ord('R')):
            return "random"
        if(key == ord('s') or key == ord('S')):
            return "search"
        if(key == ord('q') or key == ord('Q')):
            return "quit"
        if(key in [10, 13]):
            return list(self.items)[self.sel]
        if(key == curses.KEY_BACKSPACE):
            return "back"
        if(len(self.items) > 0):
            self.sel %= len(self.items)
        return None

    def main_func(self):
        self.list_items()

    def list_items(self):
        self._clear()
        for i in range(len(self.items)):
            if(self.sel == i):
                self.addstr(i+1, 1, str(list(self.items)[i]), 1)
            else:
                self.addstr(i+1, 1, str(list(self.items)[i]), 0)


# Creates a title bar containing search information
# TODO: rename search bar
class Title(Pane):
    def __init__(self):
        self.query = ""
        self.title = ""

    def setup(self):
        self.pane = curses.newwin(3, mainDim[1], 0, 0)

    def main_func(self):
        self.addstr(1, 1, self.title, 2)

    def search(self):
        self._clear()
        self.title = "Search: "
        self._refresh()
        curses.curs_set(1)
        curses.echo()
        self.query = self.pane.getstr(1, len("Search: ")+1).decode("utf-8")
        curses.curs_set(0)
        curses.noecho()
        self.title = "Search: " + self.query


# Plan on using w3m
class Picture(Pane):
    # TODO: Add support
    def __init__(self):
        self.picturePath = ""


# Description of anime
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
        self._clear()
        self.addstr(1, 1, self.description, 0, True)


def main():
    try:
        windowMain = MainWindow()
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
