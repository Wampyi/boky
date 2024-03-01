import sqlite3
from PySide6.QtWidgets import QTableWidgetItem

class ProjetManager:
    def __init__(self):
        self.conn = sqlite3.connect("GESTION_ENTREPRISE.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projet (
                id INTEGER PRIMARY KEY,
                Nom TEXT,
                societe TEXT,
                email TEXT,
                numero TEXT,
                Date_début TEXT,
                Date_fin TEXT
            )
        """)
        self.conn.commit()

    def ajouter_projet(self, id, Nom, societe, email, numero, Date_début, Date_fin):
        self.cursor.execute("""
            INSERT INTO projet (id, Nom, societe, email, numero, Date_début, Date_fin)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (id, Nom, societe, email, numero, Date_début, Date_fin))
        self.conn.commit()

    def afficher_projet(self, tableWidget2):
        tableWidget2.setRowCount(0)
        self.cursor.execute("SELECT * FROM projet")
        data = self.cursor.fetchall()
        for row, record in enumerate(data):
            tableWidget2.insertRow(row)
            for column, value in enumerate(record):
                tableWidget2.setItem(row, column, QTableWidgetItem(str(value)))
