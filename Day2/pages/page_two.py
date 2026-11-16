from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Slot


class PageTwo(QWidget):
    def __init__(self):
        super().__init__()

        self.main_number = 0

        container2 = QVBoxLayout(self)

        self.main_label = QLabel('Page Two Container')

        # Container 1.1
        self.container_sub1 = QWidget()
        subcon1 = QHBoxLayout(self.container_sub1)

        self.button_one = QPushButton('Page two part 1')
        self.button_two = QPushButton('Page two part 2')

        # add functionalities to the buttons
        self.button_one.clicked.connect(lambda: self.Increment_function(1))
        self.button_two.clicked.connect(lambda: self.Increment_function(2))


        subcon1.addWidget(self.button_one)
        subcon1.addWidget(self.button_two)

        container2.addWidget(self.main_label)
        container2.addWidget(self.container_sub1)

        

    @Slot()
    def Increment_function(self, number):
        self.main_number += number
        print(f'Sum: {self.main_number}')
