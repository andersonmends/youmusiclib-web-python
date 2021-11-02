__author__ = 'Anderson'

"import MySQLdb"
from flask_sqlalchemy import SQLAlchemy


class ConnectionFactory():
    def get_connection(self):
        conn = SQLAlchemy.connect(host="localhost", user="root", passwd="", db="youmusiclib")
        return conn