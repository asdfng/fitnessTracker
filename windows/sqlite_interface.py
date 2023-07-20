import sqlite3

class DBManager:

    def __init__(self,db_name):

        '''This function takes the filename and connects to the database'''

        #TODO: Add code for generating the file if it doesn't exist

        self.conn = None
        self.db_name = db_name
        self.c = None

    def open(self):

        '''Opens the database'''

        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        #TODO: Add sqlite command for tables, determine data layout

    def close(self):

        '''Safely closes database'''

        if self.conn:
            self.conn.commit()
            self.conn.close()
            