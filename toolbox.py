from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QToolBox, QLabel
import sys

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # Add toolbar and items
        toolbox = QToolBox()
        layout.addWidget(toolbox, 0, 0)
        label = QLabel()
        toolbox.addItem(label, "Students")
        label = QLabel()
        toolbox.addItem(label, "Teachers")
        label = QLabel()
        toolbox.addItem(label, "Directors")

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())