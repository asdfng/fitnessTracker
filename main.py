from windows.screen_states import ScreenManager
from windows.sqlite_interface import DBManager
import curses
import sys, os


db = DBManager('workouts.db')

def main(stdscr):
    manager = ScreenManager(stdscr, db)
    manager.run()

try:
    db.open()
    curses.wrapper(main)

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)

# Need to make sure the database closes safely
finally:
    db.close()