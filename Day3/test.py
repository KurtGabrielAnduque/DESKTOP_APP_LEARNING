import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
)


class FixedScrollWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fixed Window with Scrollable Widget")

        # 1. Lock the window to a fixed size
        self.setFixedSize(400, 300)

        # 2. Create the scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Essential for dynamic layouts

        # 3. Create a container widget and layout for the scrollable content
        container = QWidget()
        layout = QVBoxLayout(container)

        for i in range(1, 21):
            layout.addWidget(QPushButton(f"Item {i}"))

        # 4. Put the container inside the scroll area and set as central widget
        scroll_area.setWidget(container)
        self.setCentralWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FixedScrollWindow()
    window.show()
    sys.exit(app.exec())
