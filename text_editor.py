import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtGui import QTextCursor

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        mainLayout = QVBoxLayout()

        self.textEditor = QTextEdit()
        mainLayout.addWidget(self.textEditor)

        document = self.textEditor.document()
        cursor = QTextCursor(document)

        p1 = cursor.position() # returns int
        cursor.insertImage('vision_icon.png')

        self.setLayout(mainLayout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())