import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtWidgets import QPushButton, QRadioButton, QCheckBox, QComboBox, QTextEdit, QLineEdit
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt, Slot



class PAGE1(QWidget):
   

    def __init__(self):
        self.internal_value = 0

        super().__init__()

        # create the main container
        main_layout = QVBoxLayout(self)

        # CONTAINER1 ================================
        # container for the list of buttons
        self.container1 = QWidget()
        cont1_layout = QHBoxLayout(self.container1)

        # add the buttons
        self.button1 = QPushButton('ADD 1')
        self.button2 = QPushButton('ADD 2')
        self.button3 = QPushButton('ADD 3')

        # add functionalities to each button
        self.button1.clicked.connect(lambda: self.on_button_click(1))
        self.button2.clicked.connect(lambda: self.on_button_click(2))
        self.button3.clicked.connect(lambda: self.on_button_click(3))

        # add it to container 1
        cont1_layout.addWidget(self.button1)
        cont1_layout.addWidget(self.button2)
        cont1_layout.addWidget(self.button3)

        # CONTAINER2 ===================================
        self.container2 = QWidget()
        cont2_layout = QVBoxLayout(self.container2)

        self.checkbox1 = QCheckBox('TASK 1')
        self.checkbox2 = QCheckBox('TASK 2')
        self.checkbox3 = QCheckBox('TASK 3')
        self.checkbox4 = QCheckBox('TASK 4')

        # add functionalities to each checked checkbox
        checkboxes = [self.checkbox1, self.checkbox2, self.checkbox3, self.checkbox4]

        for cb in checkboxes:
            cb.toggled.connect(lambda checked, box = cb: self.checked_task(checked, box))

        cont2_layout.addWidget(self.checkbox1)
        cont2_layout.addWidget(self.checkbox2)
        cont2_layout.addWidget(self.checkbox3)
        cont2_layout.addWidget(self.checkbox4)

        # CONTAINER3 ============================================
        self.container3 = QWidget()
        cont3_layout = QHBoxLayout(self.container3)

        self.radio1 = QRadioButton('choice A')
        self.radio2 = QRadioButton('choice B')
        self.radio3 = QRadioButton('choice C')
        self.radio4 = QRadioButton('choice D')

        cont3_layout.addWidget(self.radio1)
        cont3_layout.addWidget(self.radio2)
        cont3_layout.addWidget(self.radio3)
        cont3_layout.addWidget(self.radio4)

        for r in (self.radio1, self.radio2, self.radio3, self.radio4):
            r.toggled.connect(self.radio_select)

        # add it to main container
        main_layout.addWidget(self.container1)
        main_layout.addWidget(self.container2)
        main_layout.addWidget(self.container3)


    # functionalities for the button
    @Slot()
    def on_button_click(self,value):
        self.internal_value += value
        print(f'internal value: {self.internal_value}')

    # functionalities for the radio button
    @Slot()
    def radio_select(self):
        r = self.sender()
        if r.isChecked():
            print(f'{r.text()} is selected')

    # functionalities for the checkbox
    @Slot()
    def checked_task(self, checked: bool, checkbox: QCheckBox):
        task_name = checkbox.text()
        if checked:
            print(f'{task_name} is Done')
        else:
            print(f'{task_name} is reverted')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # setup the window title
        self.setWindowTitle('WIDGET EVENTS')

        # get the mywidgets class to present first page
        self.page1 = PAGE1()
        self.setCentralWidget(self.page1)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()