import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class OverrideDoseModal(QDialog):
    """Custom modal dialog (equivalent to a React <Modal> with form state)."""

    def __init__(self, recommended_dose: float, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Manual Dosage Override")
        self.setModal(True)
        self.resize(340, 160)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(f"Model Recommended Dose: {recommended_dose:.2f} mg/L"))

        self.override_input = QDoubleSpinBox()
        self.override_input.setRange(0.0, 200.0)
        self.override_input.setValue(recommended_dose)
        self.override_input.setSuffix(" mg/L")
        layout.addWidget(self.override_input)

        # Action buttons
        btn_row = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        confirm_btn = QPushButton("Apply Override")

        cancel_btn.clicked.connect(self.reject)   # Closes dialog and returns Rejected
        confirm_btn.clicked.connect(self.accept)  # Closes dialog and returns Accepted

        btn_row.addStretch()
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(confirm_btn)
        layout.addLayout(btn_row)


class ParentPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modal Pop-Up Demo")
        self.resize(400, 200)

        layout = QVBoxLayout(self)
        self.status_label = QLabel("Active Dose: 18.50 mg/L (Auto)")
        self.open_modal_btn = QPushButton("Override Dosage...")
        self.open_modal_btn.clicked.connect(self.open_override_modal)

        layout.addWidget(self.status_label)
        layout.addWidget(self.open_modal_btn)

    @Slot()
    def open_override_modal(self):
        # Pass 'self' so the modal centers over this window
        modal = OverrideDoseModal(recommended_dose=18.50, parent=self)

        if modal.exec() == QDialog.DialogCode.Accepted:
            new_dose = modal.override_input.value()
            self.status_label.setText(f"Active Dose: {new_dose:.2f} mg/L (Manual Override)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    page = ParentPage()
    page.show()
    app.exec()