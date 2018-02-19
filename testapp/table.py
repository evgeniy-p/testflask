import pymysql
import datetime

class Table:
    def __init__(self, table_name, mysql):
        self.name = table_name
        self.exist = None
        self.mysql = mysql
        self.check_if_exist()

    def check_if_exist(self):
        with self.mysql.cursor() as cursor:
            cursor.execute("SHOW TABLES LIKE '{name}'".format(name=self.name))
            self.exist = cursor.fetchone()
            print('database is ?', self.exist)

    def create(self):
        print('create db')
        try:
            with self.mysql.cursor() as cursor:
                cursor.execute("CREATE TABLE {table_name} (client_code TEXT, comment TEXT)".format(table_name=self.name))
        except pymysql.err.Error as e:
            print('error in create db')
            return e
        print('db created')
        return 'done'

    def update(self, text):
        print('update db')
        try:
            with self.mysql.cursor() as cursor:
                cursor.execute("INSERT INTO {table_name} (client_code, comment) VALUES ('{client_code}','{comment}')"
                               "".format(table_name=self.name, client_code=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), comment=text))

        except pymysql.err.Error as e:
            print('error in update db')
            return e
        finally:
            self.mysql.commit()
        print('db updated')
        return 'done'

    def search(self):
        print('search db')
        try:
            with self.mysql.cursor() as cursor:
                cursor.execute("SELECT * FROM {name}".format(name=self.name))
                result = cursor.fetchall()
                print(result)
                return result
        except pymysql.err.Error as e:
            print('error in search db', e)
            return e