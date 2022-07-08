import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QDialog,
    QMainWindow, QMessageBox, QToolBar, QMessageBox)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        self.new_fraccional_controller = QAction("&New fraccional controller",
                self, shortcut = "Ctrl+N")
        self.load_fraccional_controller = QAction("&Load controller",self,
                shortcut = "Ctrl+P")
        self.exit_action = self.exit_action = QAction("E&xit", self, shortcut="Ctrl+Q",
                triggered=self.close)

        self.about_action = QAction("&About", self)
    
    def create_menus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.new_fraccional_controller)
        self.fileMenu.addAction(self.load_fraccional_controller)
        self.fileMenu.addAction(self.exit_action)

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.about_action)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()
    sys.exit(app.exec())
