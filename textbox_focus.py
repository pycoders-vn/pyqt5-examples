import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout

# Use setBuddy method to quickly assign shortcut key to set focus on the buddy widget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('setBuddy tutorial')
        layout = QFormLayout()
        self.setLayout(layout)

        labelUsername = QLabel('&Username: ')
        editUsername = QLineEdit('')
        layout.addRow(labelUsername, editUsername)

        labelPassword = QLabel('&Password: ')
        editPassword = QLineEdit()
        layout.addRow(labelPassword, editPassword)

        btn = QPushButton('&Enter')
        btn.setMinimumWidth(400)
        btn.clicked.connect(lambda: print('Hello World'))
        layout.addRow(btn, QLabel())

        labelUsername.setBuddy(editUsername)
        labelPassword.setBuddy(editPassword)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')