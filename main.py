import sys
from PySide6 import QtCore
from PySide6.QtCore import*
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout
    ,QWidget)
from ui_main import Ui_MainWindow

import projetManager
import personnelManager


from UIFunctions import*
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.personnel_manager = personnelManager.PersonnelManager()
        self.projet_manager = projetManager.ProjetManager()
        self.ui.setupUi(self)

        # COMMANDE BOUTTON MENU
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))
        self.ui.Btn_personnel.clicked.connect(lambda: self.ui.SW_principal.setCurrentIndex(0))
        self.ui.Btn_projet.clicked.connect(lambda: self.ui.SW_principal.setCurrentIndex(2))
        self.ui.Btn_depot.clicked.connect(lambda: self.ui.SW_principal.setCurrentIndex(1))
        
        # COMMANDE BOUTTON MENU PERSONNEL
        self.ui.Btn_liste.clicked.connect(lambda: self.ui.SW_pg_personnal.setCurrentIndex(0))
        self.ui.Btn_ajouter.clicked.connect(lambda: self.ui.SW_pg_personnal.setCurrentIndex(1))

        # COMMANDE BOUTTON MENU PROJET
        self.ui.pb_listeProjet.clicked.connect(lambda: self.ui.stackedWidget_projet.setCurrentIndex(0))
        self.ui.pb_ajoutProjet.clicked.connect(lambda: self.ui.stackedWidget_projet.setCurrentIndex(1))

        # COMMANDE BOUTTON BDD PROJET 
        self.ui.Btn_ajouter_projet.clicked.connect(self.ajouter_projet)
        self.ui.btn_actualiser_projet.clicked.connect(self.afficher_projet)

        # COMMANDE BOUTTON BDD PERSONNELLE 
        self.ui.Boutton_OK.clicked.connect(self.ajouter_personnel)
        self.ui.btn_Actualiser.clicked.connect(self.afficher_personnel)

        self.show()

    def ajouter_projet(self):
    # Récupérer les données des QTextEdit de projet
        id = self.ui.textEdit_ID_projet.toPlainText()
        nom = self.ui.textEdit_NOM_projet.toPlainText()
        societe = self.ui.textEdit_societe.toPlainText()
        numero = self.ui.textEdit_numero_projet.toPlainText()
        email = self.ui.textEdit_Email_projet.toPlainText()
        date_debut = self.ui.textEdit_date_debut.toPlainText()
        date_fin = self.ui.textEdit_date_fin.toPlainText()
   # Appeler la méthode d'ajout de la classe ProjetManager
        self.projet_manager.ajouter_projet(id, nom, societe, numero, email, date_debut,date_fin)
   # Effacer le contenu des QTextEdit après l'ajout
        self.ui.textEdit_ID_projet.clear()
        self.ui.textEdit_NOM_projet.clear()
        self.ui.textEdit_societe.clear()
        self.ui.textEdit_Email_projet.clear()
        self.ui.textEdit_date_debut.clear()
        self.ui.textEdit_numero_projet.clear()
        self.ui.textEdit_date_fin.clear()
# Définir la méthode d'affichage de la classe MainWindow
    def afficher_projet(self):
    # Appeler la méthode d'affichage de la classe ProjetManager en passant le QTableWidget
        self.projet_manager.afficher_projet(self.ui.tableWidget_2)


    def ajouter_personnel(self):
    # Récupérer les données des QTextEdit
        id = self.ui.textEdit_ID.toPlainText()
        nom = self.ui.textEdit_Nom.toPlainText()
        prenom = self.ui.textEdit_Prenom.toPlainText()
        adresse = self.ui.textEdit_Adresse.toPlainText()
        email = self.ui.textEdit_Email.toPlainText()
        numero = self.ui.textEdit_Numero.toPlainText()
    # Appeler la méthode d'ajout de la classe PersonnelManager
        self.personnel_manager.ajouter_personnel(id, nom, prenom, adresse, email, numero)
         # Effacer le contenu des QTextEdit après l'ajout
        self.ui.textEdit_ID.clear()
        self.ui.textEdit_Nom.clear()
        self.ui.textEdit_Prenom.clear()
        self.ui.textEdit_Adresse.clear()
        self.ui.textEdit_Email.clear()
        self.ui.textEdit_Numero.clear()

# Définir la méthode d'affichage de la classe MainWindow
    def afficher_personnel(self):
    # Appeler la méthode d'affichage de la classe PersonnelManager en passant le QTableWidget
        self.personnel_manager.afficher_personnel(self.ui.tableWidget_personnel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

