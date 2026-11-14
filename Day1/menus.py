from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QCheckBox
from PySide6.QtCore import Qt, Slot
import sys

class pageOne(QWidget):
    def __init__(self):
        # default to indicate the jar is not placed
        self.container_secured = False


        super().__init__()

        main_layout = QVBoxLayout(self)

        self. container1 = QWidget()
        cont1_layout = QVBoxLayout(self.container1)

        self.is_container_placed = QCheckBox('Press check here if you already secure the raw water sample')
        self.start_analysis = QPushButton('Start Analysis')

        #add the functionalities
        # checkbox function
        self.is_container_placed.toggled.connect(lambda checked, box = self.is_container_placed: self.container_checker(checked, box))

        # button function
        self.start_analysis.clicked.connect(lambda: self.perform_analysis())
        
        cont1_layout.addWidget(self.is_container_placed)
        cont1_layout.addWidget(self.start_analysis)

        main_layout.addWidget(self.container1)

    @Slot()
    def container_checker(self, checked:bool, checkbox: QCheckBox):
        if checked:
            self.container_secured = True
            print('jar secured')
            print(self.container_secured)
        else:
            self.container_secured = False
            print('jar unsecured')
            print(self.container_secured)

    @Slot()
    def perform_analysis(self):
        if self.container_secured:
            print('Start analysis')
        else:
            QMessageBox.information(self, 'container checker', "Please secure a container in the chamber")
        

        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Message Dialog Box Lesson')
        self.page1 = pageOne()
        self.setCentralWidget(self.page1)





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()