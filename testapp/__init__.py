from flask import Flask
import pymysql
import conf

app = Flask(__name__)
try:
    mysql = pymysql.connect(host='localhost',
                            user=conf.USR,
                            password=conf.PWD,
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
except pymysql.err.OperationalError:
        raise conf.MyException('ERROR- no connect to DB')


from testapp import routes