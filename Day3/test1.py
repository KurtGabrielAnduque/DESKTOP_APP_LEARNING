import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QDoubleSpinBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AlertBanner(QFrame):
    """Reusable conditional container (equivalent to an inline React alert component)."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("alertBanner")

        layout = QHBoxLayout(self)
        self.message_label = QLabel()
        self.dismiss_btn = QPushButton("Dismiss")
        self.dismiss_btn.clicked.connect(self.hide)

        layout.addWidget(self.message_label)
        layout.addStretch()
        layout.addWidget(self.dismiss_btn)

        # Hidden on initial render (just like initial state: showAlert = false)
        self.hide()

    def show_warning(self, text: str):
        self.message_label.setText(text)
        self.show()  # Layout automatically expands to make room for this container


class DosageCheckDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inline Conditional Container")
        self.resize(460, 220)

        main_layout = QVBoxLayout(self)

        

        # 2. Condition trigger controls
        self.turbidity_input = QDoubleSpinBox()
        self.turbidity_input.setRange(0.0, 5000.0)
        self.turbidity_input.setSuffix(" NTU")
        self.turbidity_input.valueChanged.connect(self.on_turbidity_changed)

        main_layout.addWidget(QLabel("Adjust turbidity above 50 NTU to trigger container:"))
        main_layout.addWidget(self.turbidity_input)
        # 1. Mount the conditional container where you want it to appear
        self.alert_banner = AlertBanner()
        main_layout.addWidget(self.alert_banner)
        main_layout.addStretch()


    @Slot(float)
    def on_turbidity_changed(self, value: float):
        if value > 50.0:
            self.alert_banner.show_warning(
                f"High Turbidity ({value:.1f} NTU): Manual jar verification required."
            )
        else:
            self.alert_banner.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = DosageCheckDemo()
    demo.show()
    app.exec()