from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, Signal
# import a BUTTON group so we can manage how multiple button behave
from PySide6.QtWidgets import QButtonGroup, QPushButton


class SideNavigationBar(QWidget):
    # this is a signal or a index value that navigation bar must send when user
    # chnge a specific page index 
    page_changed = Signal(int)

    # now this consturctor must excpect a list of navigation pages 
    # therefore: variable: list[str]
    def __init__(self, navigation_page_lists: list[str]):
        super().__init__()

        # set the side nagivation bar size
        self.setFixedWidth(220)

        # ofcourse creating side navigation bar is vertical
        navigation_container = QVBoxLayout(self)

        self.nav_label = QLabel('MAIN MENU')
        navigation_container.addWidget(self.nav_label)

        # manage the group behaviour
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True) # turn the group of button to act like radio buttons
        self.button_group.idClicked.connect(self.page_changed.emit) #send the signal value of the page index

        # now prepare 
        for index, label in enumerate(navigation_page_lists):
            button = QPushButton(label)
            button.setCheckable(True) # this will make the button have on and off state

            # set the default open page which is first index in the navigation bar
            if index == 0:
                button.setChecked(True)

            navigation_container.addWidget(button) # add it to the container
            self.button_group.addButton(button, index) # add the button and their corresponding index so we can emit a correct index

        navigation_container.addStretch() 
            


        
        



