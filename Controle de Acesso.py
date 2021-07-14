# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Controle de Acesso.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControleDeAcesso(object):
    def setupUi(self, ControleDeAcesso):
        ControleDeAcesso.setObjectName("ControleDeAcesso")
        ControleDeAcesso.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ControleDeAcesso)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 227, 29))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 251, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(556, 2, 241, 51))
        self.label_3.setObjectName("label_3")
        ControleDeAcesso.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ControleDeAcesso)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuControle_de_Acesso_RFID = QtWidgets.QMenu(self.menubar)
        self.menuControle_de_Acesso_RFID.setObjectName("menuControle_de_Acesso_RFID")
        ControleDeAcesso.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ControleDeAcesso)
        self.statusbar.setObjectName("statusbar")
        ControleDeAcesso.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuControle_de_Acesso_RFID.menuAction())

        self.retranslateUi(ControleDeAcesso)
        QtCore.QMetaObject.connectSlotsByName(ControleDeAcesso)

    def retranslateUi(self, ControleDeAcesso):
        _translate = QtCore.QCoreApplication.translate
        ControleDeAcesso.setWindowTitle(_translate("ControleDeAcesso", "MainWindow"))
        self.label.setText(_translate("ControleDeAcesso", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color: black\">Controle de Acesso</span></p></body></html>"))
        self.label_2.setText(_translate("ControleDeAcesso", "TextLabel"))
        self.label_3.setText(_translate("ControleDeAcesso", "TextLabel"))
        self.menuControle_de_Acesso_RFID.setTitle(_translate("ControleDeAcesso", "Controle de Acesso - RFID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ControleDeAcesso = QtWidgets.QMainWindow()
    ui = Ui_ControleDeAcesso()
    ui.setupUi(ControleDeAcesso)
    ControleDeAcesso.show()
    sys.exit(app.exec_())

