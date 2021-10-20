# Connect application to sqlite database
import sqlite3
from sqlite3 import Error


class Database:
    DB_LOCATION = 'notas.db'

    def connect(self):
        try:
            con = sqlite3.connect(DB_LOCATION)
            return con
        except Error:
            print(Error)

    def create():
        return null

    def read(self, table=None, where=None):
        data = self.connect.execute('SELECT * from %s' % table)
        return data.fetchall()

    def readOne(self, table=None,fields=None, field=None, equalTo=None):
        data = self.connect.execute('select %s from %s where %s=%d' %
                          (fields, table, field, equalTo))
        return data.fetchall()

    def delete(self, table = None, field_id = None, id = None):
        self.connect.execute('delete from %s where %s=%d' % (table, field_id, id))

    def update():
        return null

    def close():
        self.connect.close()
