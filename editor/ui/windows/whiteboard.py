from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class WhiteboardWindow(QMainWindow):
    def __init__(self,main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Whiteboard")
        self.setGeometry(100, 100, 1024, 768)

        # Criar um widget central para a janela
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)

        # ICON DECORATIVO SUP ESQUERDO
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap("assets/logo.png")) 
        self.icon_label.setFixedSize(70, 70)
        
        self.menu_label = QLabel("Menu de Opcoes")
        self.menu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.whiteboard_label = QLabel("Área de Edição (Whiteboard)")
        self.whiteboard_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.menu_label,1,0,3,1)
        layout.addWidget(self.whiteboard_label,1,1,3,3)
        layout.addWidget(self.icon_label, 0, 0)  # Ícone no topo

    def closeEvent(self, event):
        self.main_window.showMaximized()
        event.accept()

    def show_main_window(self):
        self.main_window.showMaximized()