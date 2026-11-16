from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class Settings(QWidget):
    def __init__(self):
        super().__init__()

        settings_layout = QVBoxLayout(self)

        self.main_label = QLabel('Settings')
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        settings_layout.addWidget(self.main_label)

