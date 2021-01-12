from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        button = QPushButton("Button")
        button.setToolTip("This is a text")
        layout.addWidget(button, 0, 0)

        button = QPushButton("Button")
        button.setToolTip("<b>HTML</b> <i>can</i> be shown too..")
        layout.addWidget(button, 1, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
