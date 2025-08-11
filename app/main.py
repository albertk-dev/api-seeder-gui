import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

def run_in_gui_mode():
    """
    Point d'entrée principal pour l'application graphique.
    """
    # QApplication est l'objet central qui gère les widgets et les événements.
    app = QApplication(sys.argv)

    # On crée et on affiche notre fenêtre principale.
    window = MainWindow()
    window.show()

    # On lance la boucle d'événements de l'application.
    # Le script s'arrêtera ici jusqu'à ce que la fenêtre soit fermée.
    sys.exit(app.exec())


if __name__ == "__main__":
    # On bascule sur le mode graphique
    run_in_gui_mode()