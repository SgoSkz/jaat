#!/usr/bin/env python
"""
Learning curses.py through experience
    - Create working window
        - Window is resizeable without crashing
        - Working colors
        - Split windows
            - Split size based of terminal size
            - Bordered
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
        self.std.leaveok(0)
        self.std.keypad(1)
        curses.nocbreak()
        curses.noecho()
        curses.halfdelay(20)
        curses.start_color()

    def key_handler(self):
        pass

    def key(self):
        pass

    def selector(self):
        pass

    def update_size(self):
        pass

    @staticmethod
    def close_window():
        curses.endwin()


def main():
    windowMain = MainWindow()
    windowMain.new_window()
    windowMain.close_window()

if __name__ == "__main__":
    main()
