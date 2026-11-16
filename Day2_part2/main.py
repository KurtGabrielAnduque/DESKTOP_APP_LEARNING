# import intialization of the main window
from PySide6.QtWidgets import QMainWindow, QApplication
# import intialization of needed tools
from PySide6.QtWidgets import QWidget, QHBoxLayout, QStackedWidget
# import other core components
from PySide6.QtCore import Qt, Slot
import sys
# import the side bar
from components.navigation_bar import SideNavigationBar


# add list of pages in stacked widget
from pages.dash_board import DashBoard
from pages.dosage_recommendation import DosageRecommendation
from pages.settings import Settings
from pages.treatment_history import TreatmentHistory
from pages.treatment_verification import TreatmentVerification

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sample Application')
        self.resize(1024, 600)

        main_container = QWidget()
        self.setCentralWidget(main_container)

        # intialize the container of the main container
        main_container_layout = QHBoxLayout(main_container)
        main_container_layout.setContentsMargins(0, 0, 0, 0)
        main_container_layout.setSpacing(0)

        # list here the name of pages
        self.dashboard = DashBoard()
        self.dosage_recommendation = DosageRecommendation()
        self.dosage_verification = TreatmentVerification()
        self.treatment_history = TreatmentHistory()
        self.settings = Settings()

        # setup the navigation routes
        # this method is better in order to avoid page index mismatch
        nav_routes = [
            ("Dash Board", self.dashboard),
            ("Dosage Recommendation", self.dosage_recommendation),
            ("Treatment Verification", self.dosage_verification),
            ("Treament History", self.treatment_history),
            ("Settings", self.settings)
        ]


        # setup the navigation bar and page
        self.navigation_bar = SideNavigationBar([label for label, _ in nav_routes])

        self.pages = QStackedWidget()
        # automate the creation of page routing
        for _, routes in nav_routes:
            self.pages.addWidget(routes)



        # connect the navigation bar to the signal emitter
        self.navigation_bar.page_changed.connect(self.pages.setCurrentIndex)

        main_container_layout.addWidget(self.navigation_bar)
        main_container_layout.addWidget(self.pages)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()