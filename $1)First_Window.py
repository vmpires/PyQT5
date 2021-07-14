import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela em PyQT5!"
        self.CarregarJanela()
    
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    

aplicacao = QApplication(sys.argv)
janela = Janela()
sys.exit(aplicacao.exec_())


