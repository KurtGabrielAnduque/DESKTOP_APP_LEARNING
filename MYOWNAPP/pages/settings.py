from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, Slot, Signal

from pathlib import Path

#import components
from PySide6.QtWidgets import QLabel

BASEPATH = Path(__file__).resolve().parent.parent

class SettingsPage(QFrame):
    def __init__(self):
        super().__init__()

        samplepage_layout = QVBoxLayout(self)
        samplepage_layout.setObjectName('SettingsPage')

        self.sample_label = QLabel('Settings page')
        self.sample_label.setObjectName('SettingsPageLabel')


        samplepage_layout.addWidget(self.sample_label)

        # import the styling
        qss_path = BASEPATH / "pages" / "styles" / "settings_style.qss"

        if qss_path.exists():
            self.setStyleSheet(qss_path.read_text(encoding="utf-8"))