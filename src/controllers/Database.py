# Connect application to sqlite database
import sqlite3
from sqlite3 import Error


class Database:
    def connect():
        try:
            con = sqlite3.connect('./notas.db')
            return con
        except Error:
            print(Error)

    def create():
        return null

    def read(table=None, where=None):
        db = Database.connect()
        data = db.execute('SELECT * from %s' % table)
        return data.fetchall()

    def readOne(table=None,fields=None, field=None, equalTo=None):
        db = Database.connect()
        data = db.execute('select %s from %s where %s=%d' %
                          (fields, table, field, equalTo))
        return data.fetchall()

    def delete(table = None, field_id = None, id = None):
        db.Database.connect()
        db.execute('delete from %s where %s=%d' % (table, field_id, id))

    def update():
        return null

    def close():
        return null
