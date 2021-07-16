from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
valor = 0

def Advance():
    global valor
    valor += 10
    window.progressBar.setValue(valor)

def Erase():
    global valor 
    valor = 0
    window.progressBar.setValue(valor)


app = QtWidgets.QApplication([])
window = uic.loadUi("$8ProgressBar.ui")
window.pushButton.clicked.connect(Advance)
window.pushButton_2.clicked.connect(Erase)

window.show()
app.exec()