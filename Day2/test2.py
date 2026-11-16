import sys
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from pages.page_one import PageOne
from pages.page_two import PageTwo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practice Multi Page")
        self.resize(700, 450)

        # Root container splits screen horizontally: [ Sidebar | Page Stack ]
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)

        # 1. Left Sidebar Navigation
        sidebar = QWidget()
        sidebar.setFixedWidth(160)
        sidebar_layout = QVBoxLayout(sidebar)

        self.btn_page_one = QPushButton("Page One")
        self.btn_page_two = QPushButton("Page Two")

        # Make buttons act like mutually exclusive tabs
        for btn in (self.btn_page_one, self.btn_page_two):
            btn.setCheckable(True)
            btn.setAutoExclusive(True)
        self.btn_page_one.setChecked(True)  # Highlight default page

        sidebar_layout.addWidget(self.btn_page_one)
        sidebar_layout.addWidget(self.btn_page_two)
        sidebar_layout.addStretch()  # Pushes nav buttons to the top of the sidebar

        # 2. Right Content Area (QStackedWidget)
        self.stack = QStackedWidget()
        self.page_one = PageOne()
        self.page_two = PageTwo()

        self.stack.addWidget(self.page_one)  # Index 0
        self.stack.addWidget(self.page_two)  # Index 1

        # 3. Connect Sidebar Buttons to Stack Indices
        self.btn_page_one.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_page_two.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        # 4. Assemble Main Layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()