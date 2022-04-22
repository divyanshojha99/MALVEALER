#MALVEALER MAIN FILE
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget
from PyQt5.QtCore import Qt
from scan import ScanWidget
from update import UpdateWidget
from PyQt5 import QtGui


class MalvealerMainWidget(QTabWidget):

    def __init__(self):
        super().__init__()
        self.addTab(ScanWidget(), "Scan")
        self.addTab(UpdateWidget(), "Update")


class MalvealerMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle("MALVEALER")
        self.setGeometry(300, 300, 900, 600)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setCentralWidget(MalvealerMainWidget())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    malvealer = MalvealerMainWindow()
    malvealer.show()
    sys.exit(app.exec())