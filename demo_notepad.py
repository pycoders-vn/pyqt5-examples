import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
                            QPushButton, QLabel, QPlainTextEdit, QStatusBar, QToolBar, \
                            QVBoxLayout, QAction, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QSize                          
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('./Icons/notepad.ico'))
        self.screen_width, self.screen_height = self.geometry().width(), self.geometry().height()
        self.resize(self.screen_width * 2, self.screen_height * 2) 

        self.filterTypes = 'Text Document (*.txt);; Python (*.py);; Markdown (*.md)'

        self.path = None

        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(12)

        mainLayout = QVBoxLayout()

        # editor
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)
        mainLayout.addWidget(self.editor)

        # stautsBar
        self.statusBar = self.statusBar()

        # app container
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        #----------------------------------
        # File Menu
        #----------------------------------
        file_menu = self.menuBar().addMenu('&File')

        #----------------------------------
        # File ToolBar
        #----------------------------------
        file_toolbar = QToolBar('File')
        file_toolbar.setIconSize(QSize(60, 60))
        self.addToolBar(Qt.BottomToolBarArea, file_toolbar)

        """
        open, save, saveAs
        """
        open_file_action = QAction(QIcon('./Icons/file_open.ico'), 'Open File...', self)
        open_file_action.setStatusTip('Open file')
        open_file_action.setShortcut(QKeySequence.Open)
        open_file_action.triggered.connect(self.file_open) #TODO

        save_file_action = self.create_action(self, './Icons/save_file.ico', 'Save File', 'Save file', self.file_save)
        save_file_action.setShortcut(QKeySequence.Save)

        save_fileAs_action = self.create_action(self, './Icons/save_as_file.ico', 'Save File As...', 'Save file as', self.file_saveAs)
        save_fileAs_action.setShortcut(QKeySequence('Ctrl+Shift+S'))

        file_menu.addActions([open_file_action, save_file_action, save_fileAs_action])
        file_toolbar.addActions([open_file_action, save_file_action, save_fileAs_action])

        # Print Action (Print Document)
        print_action = self.create_action(self, './Icons/printer.ico', 'Print File', 'Print file', self.print_file)
        print_action.setShortcut(QKeySequence.Print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        #----------------------------------
        # Edit Menu
        #----------------------------------
        edit_menu = self.menuBar().addMenu('&Edit')

        #----------------------------------
        # Edit ToolBar
        #----------------------------------
        edit_toolbar =QToolBar('Edit')
        edit_toolbar.setIconSize(QSize(60, 60))
        self.addToolBar(Qt.BottomToolBarArea, edit_toolbar)

        # Undo, Redo Actions
        undo_action = self.create_action(self, './Icons/undo.ico', 'Undo', 'Undo', self.editor.undo)
        undo_action.setShortcut(QKeySequence.Undo)

        redo_action = self.create_action(self, './Icons/redo.ico', 'Redo', 'Redo', self.editor.redo)
        redo_action.setShortcut(QKeySequence.Redo)

        edit_menu.addActions([undo_action, redo_action])
        edit_toolbar.addActions([undo_action, redo_action])

        # Clear action
        clear_action = self.create_action(self, './Icons/clear.ico', 'Clear', 'Clear', self.clear_content)
        edit_menu.addAction(clear_action)
        edit_toolbar.addAction(clear_action)

        # add separator
        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        # cut, copy, paste, select all
        cut_action = self.create_action(self, './Icons/cut.ico', 'Cut', 'Cut', self.editor.cut)
        copy_action = self.create_action(self, './Icons/copy.ico', 'Copy', 'Copy', self.editor.copy)
        paste_action = self.create_action(self, './Icons/paste.ico', 'Paste', 'Paste', self.editor.paste)
        select_all_action = self.create_action(self, './Icons/select_all.ico', 'Select All', 'Select all', self.editor.selectAll)

        cut_action.setShortcut(QKeySequence.Cut)
        copy_action.setShortcut(QKeySequence.Copy)
        paste_action.setShortcut(QKeySequence.Paste)
        select_all_action.setShortcut(QKeySequence.SelectAll)

        edit_menu.addActions([cut_action, copy_action, paste_action, select_all_action])
        edit_toolbar.addActions([cut_action, copy_action, paste_action, select_all_action])

        # add separator
        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        # wrap text
        wrap_text_action = self.create_action(self, './Icons/wrap_text.ico', 'Wrap Text', 'Wrap text', self.toggle_wrap_text)
        wrap_text_action.setShortcut('Ctrl+Shift+W')
        edit_menu.addAction(wrap_text_action)
        edit_toolbar.addAction(wrap_text_action)

        self.update_title()

    def toggle_wrap_text(self):
        self.editor.setLineWrapMode(not self.editor.lineWrapMode())

    def clear_content(self):
        self.editor.setPlainText('')

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Open file',
            directory='',
            filter=self.filterTypes
        )

        if path:
            try:    
                with open(path, 'r') as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            self.file_saveAs()
        else:
            try:
                text = self.editor.toPlainText()
                with open(self.path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:  
                self.dialog_message(str(e))

    def file_saveAs(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            'Save file as',
            '',
            self.filterTypes
        )                               

        text = self.editor.toPlainText()

        if not path:
            return
        else:
            try:
                with open(path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.update_title()

    def print_file(self):
        printDialog = QPrintDialog()
        if printDialog.exec_():
            self.editor.print_(printDialog.printer())

    def update_title(self):
        self.setWindowTitle('{0} - NotepadX'.format(os.path.basename(self.path) if self.path else 'Unittled'))

    def dialog_message(self, message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def create_action(self, parent, icon_path, action_name, set_status_tip, triggered_method)   :
        action = QAction(QIcon(icon_path), action_name, parent)
        action.setStatusTip(set_status_tip)
        action.triggered.connect(triggered_method)
        return action



app = QApplication(sys.argv)
notePade = AppDemo()
notePade.show()
sys.exit(app.exec_())