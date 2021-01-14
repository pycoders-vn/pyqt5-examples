from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        button1 = QPushButton()
        button1.setText("Show dialog!")
        button1.move(50,50)
        button1.clicked.connect(self.showDialog)
        layout.addWidget(button1)
        # Set fixed window size
        self.setFixedSize(500, 550)
        #  Set the central widget and the general layout
        self.setLayout(layout)

        
    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Message box pop up window")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def msgButtonClick(self, i):
        print("Button clicked is:",i.text())

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())