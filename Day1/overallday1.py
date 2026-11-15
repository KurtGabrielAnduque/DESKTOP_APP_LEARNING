# import main pyside6 modules
from PySide6.QtWidgets import QMainWindow, QApplication
# import components
from PySide6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QComboBox, QDoubleSpinBox, QTextEdit, QPushButton, QVBoxLayout
# import message boxes
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt, Slot
import sys


class PageTwo(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)

        self.container1 = QWidget()
        cont1_layout = QGridLayout(self.container1)

        # intialize the labels
        self.sample_id = QLabel('Sample ID: ')
        self.water_stage = QLabel('Water Stage: ') 
        self.turbidity = QLabel('Turbidity: ')
        self.notes = QLabel('Operator Notes: ')

        # intialize the components
        self.id_value = QLineEdit()
        self.id_value.setPlaceholderText('SMPL-00001')

        self.water_stages_values = QComboBox()
        self.water_stages_values.addItems(["Raw Inlet", "Coagulated", "Clarified"])

        self.turbidity_values = QDoubleSpinBox()
        self.turbidity_values.setRange(0.0, 1000.0)
        self.turbidity_values.setSuffix(' NTU')

        self.operator_notes_values = QTextEdit()

        # add to main container
        # labels alignment
        cont1_layout.addWidget(self.sample_id, 0, 0)
        cont1_layout.addWidget(self.water_stage, 1, 0)
        cont1_layout.addWidget(self.turbidity, 2, 0)
        cont1_layout.addWidget(self.notes, 3, 0)

        # components alignment
        cont1_layout.addWidget(self.id_value, 0, 1)
        cont1_layout.addWidget(self.water_stages_values, 1,1)
        cont1_layout.addWidget(self.turbidity_values, 2, 1)
        cont1_layout.addWidget(self.operator_notes_values, 3, 1)


        # Second container
        self.container2 = QWidget()
        cont2_layout = QVBoxLayout(self.container2)

        self.submit_btn = QPushButton("Submit Values")
        self.submit_btn.clicked.connect(lambda: self.submit_values())

        # to container2 layout
        cont2_layout.addWidget(self.submit_btn)

        # connect the overall components
        self.id_value.returnPressed.connect(self.submit_values)


        # add to main container
        main_layout.addWidget(self.container1)
        main_layout.addWidget(self.container2)

    @Slot()
    def submit_values(self):
        id = self.id_value.text()
        water_stage = self.water_stages_values.currentText()
        turbidity = self.turbidity_values.value()
        notes = self.operator_notes_values.toPlainText()

        if not id.strip():
            QMessageBox.warning(self, 'id value', "Id has no values pls add the sample ID")
            return

        if not notes.strip():
            QMessageBox.warning(self, 'ntoes', "Please leave a note")
            return

        QMessageBox.information(self, 'Water sample Information', f'ID: {id} \n water stage: {water_stage} \n water turbidity: {turbidity} \n Operator Notes: {notes}')








class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize the main window
        self.setWindowTitle('Overall learning')
        self.page_two = PageTwo()
        self.setCentralWidget(self.page_two)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()