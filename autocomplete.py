from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # auto complete options                                                 
        names = ["apple", "alps", "iphone 6", "iphone 7", "berry", "cherry" ]
        completer = QCompleter(names)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())