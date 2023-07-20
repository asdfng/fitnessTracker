from . import sqlite_interface
import curses

class ScreenManager:

    def __init__(self,stdscr, database):
        self.stdscr = stdscr
        self.screen = self.menu_screen
        self.height = None
        self.width = None
        self.database = database

    def menu_screen(self, stdscr):
        pass

    def run(self):
        while self.screen is not None:
            self.screen = self.screen()

    