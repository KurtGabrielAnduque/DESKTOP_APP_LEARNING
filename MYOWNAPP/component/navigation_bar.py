from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout
from PySide6.QtCore import Qt, Slot, Signal

# import components
from PySide6.QtWidgets import QLabel, QPushButton, QButtonGroup

from pathlib import Path

BASEPATH = Path(__file__).resolve().parent.parent

class NavigationBar(QFrame):
    page_changed = Signal(int)

    def __init__(self, navigation_page_lists: list[str]):
        super().__init__()
        self.setFixedWidth(220)
        navigation_bar_layout = QVBoxLayout(self)
        self.setObjectName("DashBoardContainer")

        self.nav_label = QLabel('MAIN MENU')
        self.nav_label.setObjectName('MainLabel')
        navigation_bar_layout.addWidget(self.nav_label)
        navigation_bar_layout.setContentsMargins(0, 0, 0, 0)
        navigation_bar_layout.setSpacing(0)
        
        self.button_group = QButtonGroup(self) # get the lists send from the main
        self.button_group.setExclusive(True)
        self.button_group.idClicked.connect(self.page_changed.emit)

        for index, label in enumerate(navigation_page_lists):

            if label == "Settings":
                navigation_bar_layout.addStretch()
                # Create a separate horizontal divider
                separator = QFrame()
                separator.setObjectName("SettingsSeparator")
                separator.setFixedHeight(1)

                navigation_bar_layout.addWidget(separator)

            button = QPushButton(label)
            button.setCheckable(True) # turn it into on and off state

            if label == "Settings":
                button.setObjectName('SettingsButton')

            if index == 0:
                button.setChecked(True)

            navigation_bar_layout.addWidget(button)

            self.button_group.addButton(button, index)


        qss_path = BASEPATH / "component" / "styles" / "nav_style.qss"

        if qss_path.exists():
            self.setStyleSheet(qss_path.read_text(encoding="utf-8"))