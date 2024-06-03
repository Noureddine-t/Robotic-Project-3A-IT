from PyQt6.QtWidgets import QApplication
from src.Interface.MainWindow import MainWindow

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
