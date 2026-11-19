from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, Slot, Signal

from pathlib import Path

# import components
from PySide6.QtWidgets import QLabel

BASEPATH = Path(__file__).resolve().parent.parent

class DashBoard(QFrame):
    def __init__(self):
        super().__init__()

        dashboard_layout = QVBoxLayout(self)
        dashboard_layout.setObjectName('DashBoard')

        self.main_label = QLabel('DASHBOARD')
        self.main_label.setObjectName('DashBoardLabel')

        dashboard_layout.addWidget(self.main_label)

        # import the styling
        qss_path = BASEPATH / "pages" / "styles" / "dashboard_style.qss"

        if qss_path.exists():
            self.setStyleSheet(qss_path.read_text(encoding="utf-8"))