from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtWidgets import QLabel, QPushButton
from PySide6.QtCore import Qt, Slot


class PageOne(QWidget):
    def __init__(self):
        super().__init__()

        page_one_container = QVBoxLayout(self)

        self.label1 = QLabel('PageOne CLass')
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)


        page_one_container.addWidget(self.label1)

        