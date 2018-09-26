import sys
from PyQt5.QtWidgets import QApplication, QDisplayWindow
from interface import Ui_Display

class DataWindow(QDisplayWindow)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Display()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DataWindow(sys.argv)
    w.show()
    sys.exit(app.exec_())