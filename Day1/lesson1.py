from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout
# other compotnents for widgets
from PySide6.QtWidgets import QPushButton, QLineEdit, QTextEdit, QSlider, QProgressBar, QComboBox, QRadioButton, QListWidget
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a window title
        # similiar to page title in web desing
        self.setWindowTitle('Hellow World Application')

        # QWidget works like a div in HTML
        # However if we want to create multiple div
        # there must be a parent div
        parent_container = QWidget()
        self.setCentralWidget(parent_container)

        # vertically stack every sub container
        main_layout = QVBoxLayout(parent_container)

        # now create a sub container Container1
        container1 = QWidget()
        cont1_layout = QHBoxLayout(container1)
        labels = ['ONE','TWO','THREE','FOUR']
        for text in labels:
            label = QLabel(text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cont1_layout.addWidget(label)

        # add pushbutton for container1
        button1 = QPushButton('Click me')
        cont1_layout.addWidget(button1)

        button2 = QPushButton('Click me')
        cont1_layout.addWidget(button2)

# ===========================================================================

        # CONTAINER2
        container2 = QWidget()
        cont2_layout = QVBoxLayout(container2)
        labels2= ['FIVE','SIX','SEVEN','EIGHT']
        for text in labels2:
            label = QLabel(text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cont2_layout.addWidget(label)

        # adding line edit in container 2
        line_edit = QLineEdit() # 1 line comment
        text_edit = QTextEdit() # text box

        listWid = QListWidget()
        listWid.addItems(['item1','item2','item3'])


        cont2_layout.addWidget(line_edit)
        cont2_layout.addWidget(text_edit)
        cont2_layout.addWidget(listWid)


# ===========================================================================
        container3 = QWidget()
        cont3_layout = QVBoxLayout(container3)
        
        # child container inside container3
        contianer31 = QWidget()
        cont31_layout = QHBoxLayout(contianer31)

        labels3 = ['NINE','TEN','ELEVEN','TWELVE']
        for text in labels3:
            label = QLabel(text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cont31_layout.addWidget(label)


        # creting combo box
        combobox = QComboBox()
        combobox.addItems(['item1','item2','item3'])
        
        cont3_layout.addWidget(contianer31)
        cont3_layout.addWidget(combobox)




# ===========================================================================
        # add both sub conainter in main container
        main_layout.addWidget(container1)
        main_layout.addWidget(container2)
        main_layout.addWidget(container3)





app = QApplication()

window = MainWindow()
window.show()

app.exec()
