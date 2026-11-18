import sys
from PySide6.QtCore import Signal, Slot
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


class SensorInputCard(QFrame):
    # TODO 1 (DECLARE): Define two signals here:
    # - reading_sent carrying a dict
    # - clear_requested carrying nothing
    reading_sent = Signal(dict)
    clear_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        # Input row
        inputs_row = QHBoxLayout()

        self.ph_input = QDoubleSpinBox()
        self.ph_input.setRange(0.0, 14.0)
        self.ph_input.setValue(7.0)
        self.ph_input.setPrefix("pH: ")

        self.turbidity_input = QDoubleSpinBox()
        self.turbidity_input.setRange(0.0, 500.0)
        self.turbidity_input.setValue(12.5)
        self.turbidity_input.setPrefix("Turbidity: ")
        self.turbidity_input.setSuffix(" NTU")

        inputs_row.addWidget(self.ph_input)
        inputs_row.addWidget(self.turbidity_input)

        # Button row
        btn_row = QHBoxLayout()
        self.send_btn = QPushButton("Send Reading")
        self.clear_btn = QPushButton("Clear Display")


        # connect buttons to corresponding signals
        self.send_btn.clicked.connect(lambda: self._handle_send())
        self.clear_btn.clicked.connect(lambda: self.clear_requested.emit())


        btn_row.addWidget(self.send_btn)
        btn_row.addWidget(self.clear_btn)

        layout.addLayout(inputs_row)
        layout.addLayout(btn_row)

    @Slot()
    def _handle_send(self):
        payload = {
            "ph": self.ph_input.value(),
            "turbidity": self.turbidity_input.value(),
        }
        # TODO 2B (EMIT): Emit self.reading_sent with payload
        self.reading_sent.emit(payload)


class MonitorPage(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Signal Cycle Practice")
        self.resize(460, 240)

        layout = QVBoxLayout(self)

        # Child widget
        self.sensor_card = SensorInputCard()

        # Parent readout labels
        self.readout_label = QLabel("Latest Reading: None")
        self.alert_label = QLabel("Water Status: Waiting for data...")

        # TODO 3 (CONNECT):
        # 1. Connect self.sensor_card.reading_sent to self.update_readout
        # 2. Connect self.sensor_card.reading_sent to self.check_water_quality
        # 3. Connect self.sensor_card.clear_requested to self.clear_monitor
        
        self.sensor_card.reading_sent.connect(self.update_readout)
        self.sensor_card.reading_sent.connect(self.check_water_quality)
        self.sensor_card.clear_requested.connect(self.clear_monitor)



        layout.addWidget(self.sensor_card)
        layout.addWidget(self.readout_label)
        layout.addWidget(self.alert_label)
        layout.addStretch()

    @Slot(dict)
    def update_readout(self, data: dict):
        self.readout_label.setText(
            f"Latest Reading -> pH: {data['ph']:.2f} | Turbidity: {data['turbidity']:.1f} NTU"
        )

    @Slot(dict)
    def check_water_quality(self, data: dict):
        if data["turbidity"] > 50.0 or not (6.5 <= data["ph"] <= 8.5):
            self.alert_label.setText("Water Status: WARNING — Out of normal range!")
        else:
            self.alert_label.setText("Water Status: NORMAL — Parameters within range.")

    @Slot()
    def clear_monitor(self):
        self.readout_label.setText("Latest Reading: None")
        self.alert_label.setText("Water Status: Waiting for data...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonitorPage()
    window.show()
    app.exec()