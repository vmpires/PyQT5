from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox

def SendMessage():
    msg = window.lineEdit.text()
    if msg == '':
        QMessageBox.about(window, "Alerta!", f"Nada foi digitado.")
    else:
        QMessageBox.about(window, "Mensagem", f"Aqui está sua mensagem: {msg}")
    window.lineEdit.setText("")

app = QtWidgets.QApplication([])
window = uic.loadUi("$7MessageBox.ui")
window.pushButton.clicked.connect(SendMessage)

window.show()
app.exec()