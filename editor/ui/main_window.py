from PySide6.QtWidgets import QMainWindow
from ui.designer.w_main import Ui_MainWindow  # Importa o arquivo gerado

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Carrega o layout gerado pelo Qt Designer
        