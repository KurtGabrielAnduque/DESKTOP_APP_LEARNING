from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class DashBoard(QWidget):
    def __init__(self):
        super().__init__()

        dash_board_layout = QVBoxLayout(self)

        self.main_label = QLabel('Dashboard')
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        dash_board_layout.addWidget(self.main_label)

