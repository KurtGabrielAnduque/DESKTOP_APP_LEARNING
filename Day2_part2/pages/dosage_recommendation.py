from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class DosageRecommendation(QWidget):
    def __init__(self):
        super().__init__()

        dosage_recommedation_layout = QVBoxLayout(self)

        self.main_label = QLabel('Dosage Recommendation')
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        dosage_recommedation_layout.addWidget(self.main_label)

