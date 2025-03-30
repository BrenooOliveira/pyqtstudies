import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sinais e Slots (callback)')
        self.setGeometry(100,100,300,200)

        self.botao = QPushButton('Fecha Janela')
        self.botao.clicked.connect(self.close) # conectamos o signal 'clicked' ao slot 'close'

        layout = QVBoxLayout()
        layout.addWidget(self.botao)
        self.setLayout(layout)
app = QApplication(sys.argv)
janela = MinhaJanela()
janela.show()
sys.exit(app.exec())