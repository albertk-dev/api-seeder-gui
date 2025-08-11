import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.setWindowTitle("API Seeder GUI")
        self.setGeometry(100, 100, 800, 600)  # Position x, y, largeur, hauteur

        # Ajout d'un widget simple pour commencer
        central_widget = QLabel("Bienvenue dans l'API Seeder ! L'interface est en construction.")
        central_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(central_widget)