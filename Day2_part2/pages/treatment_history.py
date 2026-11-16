from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class TreatmentHistory(QWidget):
    def __init__(self):
        super().__init__()

        treatment_history_layout = QVBoxLayout(self)

        self.main_label = QLabel('Treatment History')
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        treatment_history_layout.addWidget(self.main_label)

