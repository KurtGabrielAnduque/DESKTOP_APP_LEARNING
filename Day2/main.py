from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys

from pages.page_one import PageOne
from pages.page_two import PageTwo

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setup the main widget
        # 1. start with title
        self.setWindowTitle('Practice Multi Page')

        # 2. make a center widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_container = QVBoxLayout(main_widget)

        self.pageOne = PageOne()
        self.pageTwo = PageTwo()

        main_container.addWidget(self.pageOne)
        main_container.addWidget(self.pageTwo)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
