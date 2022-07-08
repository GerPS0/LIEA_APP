from operator import inv
import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QAbstractItemView, QApplication,
    QCheckBox, QComboBox, QFileDialog, QDialog, QDialogButtonBox, QGridLayout,
    QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,
    QMainWindow, QMessageBox, QStyle, QSpinBox, QStyleOptionViewItem,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,QPushButton)
from pip import main


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.new_dialog = None

        self.create_actions()
        self.create_menus()

        self.setWindowTitle("Fractional design controller")
        self.resize(640, 480)

    def NewDesign(self):
        if self.new_dialog is None:
            self.new_dialog = DesignDialog(self)
        
        self.new_dialog.exec()
    
    def create_actions(self):
        self.new_fraccional_controller = QAction("&New fraccional controller",
                self, shortcut = "Ctrl+N",triggered=self.NewDesign)
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
    
    

class DesignDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.Convert_combo = QComboBox()
        self.Convert_combo.addItem("Buck")
        self.Convert_combo.addItem("Boost")
        convert_label = QLabel("&Conveter Type:")
        convert_label.setBuddy(self.Convert_combo)
        
        self.InputVoltage_combo = QComboBox()
        self.InputVoltage_combo.addItem("0")
        self.InputVoltage_combo.setEditable(True)
        InV_label = QLabel("&Input voltage:")
        InV_label.setBuddy(self.InputVoltage_combo)

        self.OutputVoltage_combo = QComboBox()
        self.OutputVoltage_combo.addItem("0")
        self.OutputVoltage_combo.setEditable(True)
        OuTV_label = QLabel("&Output voltage Type:")
        OuTV_label.setBuddy(self.OutputVoltage_combo)

        self.Apply_button = QPushButton("&Apply")
        self.Exit_button = QPushButton("&Exit")

        main_layout = QGridLayout(self)
        main_layout.addWidget(convert_label, 0,0)
        main_layout.addWidget(self.Convert_combo, 0,1)
        main_layout.addWidget(InV_label,1,0)
        main_layout.addWidget(OuTV_label,2,0)
        main_layout.addWidget(self.InputVoltage_combo,1,1)
        main_layout.addWidget(self.OutputVoltage_combo,2,1)

        main_layout.addWidget(self.Apply_button,5,0)
        main_layout.addWidget(self.Exit_button,5,1)

        self.setWindowTitle("Controller design")
        self.resize(640,480)

    








if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()

    mainWin.show()
    sys.exit(app.exec())
