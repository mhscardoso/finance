import sqlite3


class Banco:

    def __init__(self):
        self.conection = sqlite3.connect("base.db")
        self.createTable()

    
    def createTable(self):
        cursor = self.conection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            userId INTEGER NOT NULL,
            username TEXT NOT NULL,
            hash_pass TEXT NOT NULL,
            cash DECIMAL DEFAULT 10000.00,
            PRIMERY KEY (userId)
        );

        CREATE TABLE IF NOT EXISTS bought (
            user INTEGER NOT NULL,
            stock TEXT NOT NULL,
            price DECIMAL,
            shares INTEGER,
            FOREING KEY (user) REFERENCES users(userId)
        );

        CREATE TABLE IF NOT EXISTS sold (
            user INTEGER NOT NULL,
            stock TEXT NOT NULL,
            price DECIMAL,
            shares INTEGER,
            FOREING KEY (user) REFERENCES users(userId)
        )
        """)
        self.conection.commit()
        cursor.close()
