import mysql
from mysql.connector import DatabaseError, Error
from src.database.DatabaseSession import DatabaseSession
from src.config.settings import DB_SETTINGS


class Database:
    def __init__(self):
        self.settings = DB_SETTINGS


    def connect(self):
        try:
            return mysql.connector.connect(
                host=self.settings.host,
                user=self.settings.user,
                password=self.settings.password,
                database=self.settings.database,
                autocommit=False,
            )
        except Error as e:
            raise DatabaseError(f"connection mysql impossible : {e}") from e


    def session(self):
        return DatabaseSession(self)
