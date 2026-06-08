import sqlite3
from pathlib import Path

class Database:
    def __init__(self):
        Path("data").mkdir(exist_ok=True)
        self.conn = sqlite3.connect("data/vendor_book.db")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS seller(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Email TEXT UNIQUE,
            Password TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
            SellerId INTEGER,
            ProductName TEXT,
            Price INTEGER,
            Quantity INTEGER,
            Descriptions TEXT,
            FOREIGN KEY(SellerId) REFERENCES seller(Id)
        )
        """)
        self.conn.commit()

    def close(self):
        self.conn.close()        
