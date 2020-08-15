#!/usr/bin/env python
import curses
import _4anime


class Pane:
    box = 1
    pane = None
    def __init__(self):
        pass

    def _refresh_new(self):
        if(maxyx != screen.getmaxyx()):
            screen.clear()
            self.setup()
        if(self.box == 1):
            self.pane.box()
        self.pane.clear()
        self.main()
        self.pane.refresh()

    def _refresh(self):
        if(maxyx != screen.getmaxyx()):
            screen.clear()
            self.setup()
            screen.refresh()
        if(self.box == 1):
            self.pane.box()
        self.main()
        self.pane.refresh()

    def addstr(self, y:int = 1, x:int = 1, string:str = "", attrib:int = 0, wrap:bool = 0):
        if(wrap):
            cat = ""
            strings = string.split()
            for i in strings:
                if(y < self.pane.getmaxyx()[0] - 1):
                    if(len(i+cat) < self.pane.getmaxyx()[1] - x - 1):
                        cat += i + " "
                    else:
                        self.addstr(y, x, cat, 0)
                        y += 1
        else:
            self.pane.addnstr(y, x, string + " "*1000, self.pane.getmaxyx()[1] - x - 1)

    def setup(self):
        pass

    def main(self):
        pass


class Main(Pane):
    """Main pane which contains the selection of items which include animes and episodes"""
    selA = 0
    anime = dict()
    episodes = dict()
    items = list()

    def __init__(self):
        self.sel = 0
        self.setup()

    def setup(self):
        self.pane = curses.newwin(screen.getmaxyx()[0]-3, screen.getmaxyx()[1]//2, 3, 0)

    def main(self):
        for i in range(len(self.items)):
            if self.sel == i:
                self.addstr(i+1, 1, self.items[i], 1, 0)
            else:
                self.addstr(i+1, 1, self.items[i], 0, 0)


class Meta(Pane):
    """Stuff that will be shown in description"""
    desc = ""
    title = ""
    episodes = ""

    def __init__(self):
        self.setup()

    def setup(self):
        self.pane = curses.newwin(
                (screen.getmaxyx()[0]-((3+screen.getmaxyx()[0])//2)),
                (screen.getmaxyx()[1]-(screen.getmaxyx()[1]//2)-1),
                ((3+screen.getmaxyx()[0])//2),
                (screen.getmaxyx()[1]//2)+1)

    def main(self):
        pass


class Search(Pane):
    """Search bar"""
    query = ""
    results = dict()

    def __init__(self):
        self.setup()

    def setup(self):
        self.pane = curses.newwin(3, screen.getmaxyx()[1], 0, 0)

    def main(self):
        if(self.query):
            self.addstr(1, 1, self.query)

    def search(self):
        pass


class Jaat():
    """This is the window class which contains basically everything"""
    def __init__(self, *args, **kwargs):
        pass

    def setup_curses(self):
        global screen
        screen = curses.initscr()

    def init_curses(self):
        screen.leaveok(0)
        screen.keypad(1)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        
    def __init_panes(self):
        self.main = Main()
        self.meta = Meta()
        self.search = Search()

    def __refresh_panes(self):
        self.main._refresh()
        self.meta._refresh()
        self.search._refresh()

    def loop(self):
        global maxyx
        screen.refresh()
        self.__init_panes()
        maxyx = screen.getmaxyx()
        c = -1
        while 1:
            if(c == ord("q") or c == ord("Q")):
                break
            if(maxyx != screen.getmaxyx()):
                self.__refresh_panes()
                maxyx = screen.getmaxyx()
            self.__refresh_panes()
            c = screen.getch()


def main():
    # Don't break terminal when exiting
    try:
        win = Jaat()
        win.setup_curses()
        win.init_curses()
        win.loop()
    except:
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        exit()
    finally:
        curses.nocbreak()
        curses.echo()
        curses.endwin()

if(__name__ == "__main__"):
    main()
