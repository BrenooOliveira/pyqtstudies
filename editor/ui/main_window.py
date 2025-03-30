import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from ui.windows.whiteboard import WhiteboardWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor Low-Code")
        self.setGeometry(100, 100, 1024, 768)  # Tamanho inicial da janela
        
        # LAYOUT PRINCIPAL
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QGridLayout()
        
        # ICON DECORATIVO SUP ESQUERDO
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap("assets/logo.png")) 
        self.icon_label.setFixedSize(70, 70)
        
        # HEADER COM BOTOES
        self.new_button = QPushButton("New")
        self.new_button.clicked.connect(self.start_new_project)
        
        self.open_button = QPushButton("Open")
        self.open_button.clicked.connect(self.open_project)
        
        # IMAGEM DE BACKGROUND
        self.bg_label = QLabel()
        self.bg_label.setPixmap(QPixmap("assets/logo_bg.png"))  # Substitua pelo caminho correto
        self.bg_label.setScaledContents(True)
        self.bg_label.setAlignment(Qt.AlignCenter)
        
        # Menu lateral (espaço reservado, pode ser expandido futuramente)
        self.menu_label = QLabel("Menu")
        self.menu_label.setAlignment(Qt.AlignCenter)
        
        # ADICIONANDO ELEMENTOS DO LAYOUT
        layout.addWidget(self.menu_label, 0, 0, 3, 1)  # Menu ocupa 3 linhas na primeira coluna e está na 0x0
        layout.addWidget(self.icon_label, 0, 0)  # Ícone no topo
        layout.addWidget(self.new_button, 0, 1)  # Botão "New" na linha 0, coluna 1
        layout.addWidget(self.open_button, 0, 2)  # Botão "Open" na linha 0, coluna 2
        layout.addWidget(self.bg_label, 1, 1, 2, 3)  # Imagem de fundo ocupa 2 linhas e 3 colunas e está situado na 1x1
        
        self.central_widget.setLayout(layout)
    

    ###  SIGNALS DOS BOTOES  ###
    def start_new_project(self):
        print("Novo projeto iniciado")
        self.whiteboard_window = WhiteboardWindow(self)
        self.whiteboard_window.showMaximized()
        self.hide()
    
    def open_project(self):
        print("Abrindo explorador de arquivos")
        # Aqui adicionaremos a lógica para abrir um projeto salvo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
