# Importer le module sqlite3 pour accéder à la base de données
import sqlite3
from PySide6.QtWidgets import QTableWidgetItem
# Définir la classe qui gère la table personnel
class PersonnelManager:
    def __init__(self):
        # Créer ou ouvrir la connexion à la base de données
        self.conn = sqlite3.connect("GESTION_ENTREPRISE.db")
        self.cursor = self.conn.cursor()
        # Créer la table personnel si elle n'existe pas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Personnel (
                id INTEGER PRIMARY KEY,
                Nom TEXT,
                Prenom TEXT,
                Adresse TEXT,
                Email TEXT,
                Numero TEXT
            )
        """)
        self.conn.commit()

    def ajouter_personnel(self, id, nom, prenom, adresse, email, numero):
        # Ajouter un enregistrement dans la table personnel avec les données fournies
        self.cursor.execute("""
            INSERT INTO Personnel (id, Nom, Prenom, Adresse, Email, Numero)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id, nom, prenom, adresse, email, numero))
        self.conn.commit()

    def afficher_personnel(self, tableWidget):
        # Afficher les données de la table personnel dans le QTableWidget fourni
        # Effacer les données précédentes du QTableWidget
        tableWidget.setRowCount(0)
        # Récupérer les données de la table personnel
        self.cursor.execute("""
            SELECT * FROM Personnel
        """)
        data = self.cursor.fetchall()
        # Remplir le QTableWidget avec les données
        for row, record in enumerate(data):
            tableWidget.insertRow(row)
            for column, value in enumerate(record):
                tableWidget.setItem(row, column, QTableWidgetItem(str(value)))