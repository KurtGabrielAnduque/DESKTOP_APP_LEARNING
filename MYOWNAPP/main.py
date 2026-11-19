from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget

# import design components
from PySide6.QtWidgets import QLabel, QPushButton, QComboBox

# import the core components
from PySide6.QtCore import Qt, Slot, Signal

import sys
from pathlib import Path


#import the navigation bar component
from component.navigation_bar import NavigationBar

# import the pages
from pages.dashboard import DashBoard
from pages.sample_page import SamplePage
from pages.settings import SettingsPage


# Project directory
BASE_DIR = Path(__file__).resolve().parent


# Function to load QSS
def load_stylesheet(path: Path):
    if path.exists():
        return path.read_text(encoding="utf-8")

    print(f"Warning: Stylesheet not found: {path}")
    return ""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setup the main application container
        self.setWindowTitle('QSS lesso Application')
        self.setFixedSize(1024,600)
        main_container = QWidget()
        self.setCentralWidget(main_container)
        self.setObjectName('MainContainer')

        # setup of the main container
        main_layout = QHBoxLayout(main_container)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # setup the names of pages
        self.dashboard = DashBoard()
        self.samplepage = SamplePage()
        self.settingspage = SettingsPage()

        # setup the route

        nav_routes = [
            ("Dash Board", self.dashboard),
            ("Sample Page", self.samplepage),
            ("Settings", self.settingspage)
        ]

        # setup the navigation bar now
        self.navigatino_bar = NavigationBar([label for label, _ in nav_routes])


        #setup the stackedWidget
        self.pages = QStackedWidget()
        for _, page in nav_routes:
            self.pages.addWidget(page)

        
        self.navigatino_bar.page_changed.connect(self.pages.setCurrentIndex)

        main_layout.addWidget(self.navigatino_bar)
        main_layout.addWidget(self.pages)

        

        # Import the global QSS
        # Load global stylesheet
        global_qss = load_stylesheet(BASE_DIR / "styles" / "style.qss")
        QApplication.instance().setStyleSheet(global_qss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()