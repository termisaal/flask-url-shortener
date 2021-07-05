import sqlite3
import config as cf


class Database:
    def __init__(self):
        conn = sqlite3.connect(cf.Database.location)
