import sys

from PyQt6.QtWidgets import QApplication
from src.Interface.MainWindow import MainWindow
'''from src.Interface.OldInterface import MainWindow'''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    interface = MainWindow()
    interface.show()
    sys.exit(app.exec())

'''app = QApplication([])
window = MainWindow()
window.show()
app.exec()'''
