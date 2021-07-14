import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui
class Janela(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.topo = 100
        self.esquerda = 100
        self.largura = 700
        self.altura = 500
        self.titulo = "Quarta Janela em PyQT5!"

        botao1 = QPushButton('Botão 1', self)
        botao1.move(210,70)
        botao1.resize(100,80)
        botao1.setStyleSheet('QPushButton {background-color: green; font: bold; font-size:15px}')
        botao1.clicked.connect(self.botao1_click)
        
        botao2 = QPushButton('Botão 2', self)
        botao2.move(350,70)
        botao2.resize(100,80)
        botao2.setStyleSheet('QPushButton {background-color: red; font: bold; font-size:15px}')
        botao2.clicked.connect(self.botao2_click)
        
        self.label_1 = QLabel(self)
        self.label_1.setText("Olá mundo!")
        self.label_1.move(250,20)
        self.label_1.resize(200,25)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 15px; color: black}')

        self.carro = QLabel(self)
        self.carro.move(100, 200)
        self.carro.setPixmap(QtGui.QPixmap('porsche.png'))
        self.carro.resize(500,375)
        
        self.CarregarJanela()
    
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
    
    def botao1_click(self):
        self.label_1.setText("O botão 1 foi clicado!")
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 15px; color: green}')
        self.carro.setPixmap(QtGui.QPixmap('porsche.png'))
    
    def botao2_click(self):
        self.label_1.setText("O botão 2 foi clicado!")
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 15px; color: red}')
        self.carro.setPixmap(QtGui.QPixmap('ferrari.png'))

aplicacao = QApplication(sys.argv)
janela = Janela()
sys.exit(aplicacao.exec_())