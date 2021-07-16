from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def SendName():
    name = window.lineEdit.text()
    window.listWidget.addItem(name)
    window.lineEdit.setText("")

def DeleteAll():
    window.listWidget.clear()

app = QtWidgets.QApplication([])
window = uic.loadUi("$6List_Widget.ui")
window.pushButton.clicked.connect(SendName)
window.pushButton_2.clicked.connect(DeleteAll)

window.show()
app.exec()