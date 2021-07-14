import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.topo = 100
        self.esquerda = 100
        self.largura = 700
        self.altura = 500
        self.titulo = "Quinta Janela em PyQT5!"

        # Criação da Caixa de texto
        self.textbox = QLineEdit(self)
        self.textbox.move(25,20)
        self.textbox.resize(200,30)

        # Criação do Botão 1
        botao1 = QPushButton('Botão 1', self)
        botao1.move(210,70)
        botao1.resize(85,50)
        botao1.setStyleSheet('QPushButton {background-color: green; font: bold; font-size:15px}')
        botao1.clicked.connect(self.botao1_click)
       
        # Criação do Botão 2       
        botao2 = QPushButton('Botão 2', self)
        botao2.move(350,70)
        botao2.resize(85,50)
        botao2.setStyleSheet('QPushButton {background-color: red; font: bold; font-size:15px}')
        botao2.clicked.connect(self.botao2_click)
        
        # Criação do Botão 3       
        botao3 = QPushButton('Enviar', self)
        botao3.move(250,20)
        botao3.resize(60,30)
        botao3.setStyleSheet('QPushButton {font: bold; font-size:10px}')
        botao3.clicked.connect(self.botao3_click)
        
        # Criação do Label 1       
        self.label_1 = QLabel(self)
        self.label_1.setText("Olá mundo!")
        self.label_1.move(25,80)
        self.label_1.resize(200,25)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 15px; color: black}')

        # Criação do Label 2     
        self.label_2 = QLabel(self)
        self.label_2.setText("Mensagem enviada: ")
        self.label_2.move(330,10)
        self.label_2.resize(500,40)
        self.label_2.setStyleSheet('QLabel {font: bold; font-size: 15px; color: black}')
        
        # Criação da Imagem 1
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
        '''Altera o label 1, sua cor e setta a Porsche para a imagem'''
        self.label_1.setText("O botão 1 foi clicado!")
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 15px; color: green}')
        self.carro.setPixmap(QtGui.QPixmap('porsche.png'))
    
    def botao2_click(self):
        '''Altera o label 1, sua cor e setta a Ferrari para a imagem'''
        self.label_1.setText("O botão 2 foi clicado!")
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 15px; color: red}')
        self.carro.setPixmap(QtGui.QPixmap('ferrari.png'))

    def botao3_click(self):
        conteudo = self.textbox.text()
        self.label_2.setText("Mensagem enviada: " + conteudo)

aplicacao = QApplication(sys.argv)
janela = Janela()
sys.exit(aplicacao.exec_())