# Connect application to sqlite database
import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, database):
        self.DB_LOCATION = database
        self.con = None
        self.data = None

    def connect(self):
        """Conecta la base de datos
        """
        try:
            self.con = sqlite3.connect(self.DB_LOCATION)
        except Error:
            print(Error)

    def create(self, table, fields, values):
        """Crea un registro en la base de datos

        Args:
            table (string): nombre de la tabla
            fields (list): campos de la tabla incluyendo el campo
                           autoincrementado
            values (list): valores en cada una de las columnas
                           el valor autoincrementado se
                           genera automaticamente
        """

        try:
            if len(fields) == len(values):

                params = ["?" for v in fields]
                params = (", ").join(params)

                fields = (", ").join(fields)

                self.connect()
                sql = "INSERT INTO %s (%s) VALUES(%s)" % (
                    table, fields, params)
                # values.insert(0, len(self.readAll(table, "*")) + 1)

                self.con.execute(sql, values)
                self.con.commit()
            else:
                return TypeError("Error en los datos")
        except Error as e:
            self.con.rollback()
            print(e)

        self.close()

    def read(self, table, fields="*", where=""):

        """ Lee los registros en la base de datos

        Args:
            table (str): ingresa el nombre de la tabla
            fields (str, optional): son los campos que seran llamados de la base de datos. Defaults to "*".
            where (str, optional): ingresar la condicional de retorno de datos. Defaults to None.

        Example:
            read("users", "user_name, user_lastname, user_code", "user_id=1")
            >> [("Jhon", "Doe", "ABC123")]

        Returns:
            array: retorna un objeto con los registros de la base de datos
        """

        if where != "":
            where = "where %s" % where

        self.data = self.con.execute("SELECT %s from %s %s" %
                                     (fields, table, where))

    def delete(self, table, where):
        """ Elimina un registro de la base de datos

        Args:
            table (str): [description]
            where (str): [description]

        Example:
            delete("users", "user_id=1")
        """

        if where is not None or where != "":
            self.connect()
            self.con.execute("DELETE FROM %s WHERE %s" % (table, where))
            self.con.commit()
            self.close()
        else:
            print("No es posible eliminar registros sin el identificador de comparacion")

    def update(self, table, fields, values, where):
        """Actualiza la informacion en la base de datos

        Args:
            table (string): nombre de la tabla
            fields (list): campos de la base datos
            values (list): valores de cada campo a actualizar
            where (string): condicional para actualizar la informacion

        """

        try:
            if len(fields) == len(values):

                params = [f + " = ?" for f in fields]
                params = (", ").join(params)

                self.connect()
                sql = "UPDATE %s SET %s WHERE %s" % (
                    table, params, where)
                print(sql)
                self.con.execute(sql, values)
                self.con.commit()
            else:
                return TypeError("Error en los datos")
        except Error as e:
            self.con.rollback()
            print(e)
        finally:
            self.close()

    def close(self):
        self.con.close()

    def readAll(self, table, fields=None):
        """ Lee los registros en la base de datos

        Args:
            table (str): ingresa el nombre de la tabla
            fields (str, optional): son los campos que seran llamados de la base de datos. Defaults to "*".

        Example:
            readAll("users", "user_role, user_name, user_lastname")
            readAll("users", "*")
            >>  [
                    (1, 1, "Jhon", "Doe"),
                    (2, 3, "Ana", "Schultz"),
                    (3, 2, "Frank", "Doe"),
                    (4, 3, "Filipe", "Romein")
                ]

        Returns:
            array: retorna un objeto con los registros de la base de datos
        """

        self.connect()
        self.read(table, fields)
        return self.data.fetchall()
        self.close()

    def readOne(self, table, fields, where=""):
        """ Lee los registros en la base de datos

        Args:
            table (str): ingresa el nombre de la tabla
            fields (str, optional): son los campos que seran llamados de la base de datos. Defaults to "*".
            where (str, optional): ingresar la condicional de retorno de datos. Defaults to None.

        Example:
            readOne("users", "user_id, user_role, user_name, user_lastname", "user_id=2")
            readOne("users", "*", "user_id=2")
            >> (2, 3, "Ana", "Schultz")

        Returns:
            array: retorna un objeto con los registros de la base de datos
        """

        self.connect()
        self.read(table, fields, where)
        return self.data.fetchone()
        self.close()

    def validate(self, table, fields="*", compares=[]):

        c = ["%s='%s'" % (c[0], c[1]) for c in compares]
        c = (" and ").join(c)
        self.connect()
        self.data = self.con.execute("SELECT %s FROM %s WHERE %s" % (fields, table, c))
        data = self.data.fetchall()
        self.close()
        return True if len(data) == 1 else False
