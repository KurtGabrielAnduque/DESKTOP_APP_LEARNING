from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class TreatmentVerification(QWidget):
    def __init__(self):
        super().__init__()

        treatment_verification_layout = QVBoxLayout(self)

        self.main_label = QLabel('Treatment Verification')
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        treatment_verification_layout.addWidget(self.main_label)

