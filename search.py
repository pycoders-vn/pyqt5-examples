import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 1000)
        mainLayout = QVBoxLayout()

        companies = ('Apple', 'Facebook', 'Google', 'Amazon', 'Walmart', 'Dropbox', 'Starbucks', 'eBay', 'Canon')
        model = QStandardItemModel(len(companies), 1)
        model.setHorizontalHeaderLabels(['Company'])

        for row, company in enumerate(companies):
            item = QStandardItem(company)
            model.setItem(row, 0, item)

        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)

        search_field = QLineEdit()          
        search_field.setStyleSheet('font-size: 20px; height: 30px;')
        search_field.textChanged.connect(filter_proxy_model.setFilterRegExp)
        mainLayout.addWidget(search_field)

        table = QTableView()
        table.setStyleSheet('font-size: 16px;')
        table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setModel(filter_proxy_model)
        mainLayout.addWidget(table)

        self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())  