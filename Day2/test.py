import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


# 1. Modular Page Component
class PageWidget(QWidget):
    def __init__(self, title: str, description: str):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        header = QLabel(title)
        header.setStyleSheet("font-size: 24px; font-weight: bold;")

        body = QLabel(description)
        body.setStyleSheet("font-size: 14px; color: #555;")

        layout.addWidget(header)
        layout.addWidget(body)


# 2. Reusable Navigation Component
class SidebarNav(QFrame):
    # Custom signal emitting the selected page index
    page_changed = Signal(int)

    def __init__(self, nav_items: list[str]):
        super().__init__()
        self.setFixedWidth(200)
        self.setStyleSheet("""
            SidebarNav { background-color: #1e1e2e; }
            QPushButton {
                color: #cdd6f4;
                background: transparent;
                border: none;
                padding: 12px 16px;
                text-align: left;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #313244; }
            QPushButton:checked {
                background-color: #89b4fa;
                color: #11111b;
                font-weight: bold;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 20, 0, 20)
        layout.setSpacing(4)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        self.button_group.idClicked.connect(self.page_changed.emit)

        for index, label in enumerate(nav_items):
            btn = QPushButton(label)
            btn.setCheckable(True)
            if index == 0:
                btn.setChecked(True)
            layout.addWidget(btn)
            self.button_group.addButton(btn, index)

        layout.addStretch()


# 3. Main Window Combining Both
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Page & Navigation Demo")
        self.resize(800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Setup Navigation and Pages
        nav_labels = ["Dashboard", "Analytics", "Settings"]
        self.sidebar = SidebarNav(nav_labels)

        self.pages = QStackedWidget()
        self.pages.addWidget(PageWidget("Dashboard", "Welcome to your main overview."))
        self.pages.addWidget(PageWidget("Analytics", "Charts and metrics go here."))
        self.pages.addWidget(PageWidget("Settings", "Manage your preferences here."))

        # Connect Navigation Signal to StackedWidget Slot
        self.sidebar.page_changed.connect(self.pages.setCurrentIndex)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.pages)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
