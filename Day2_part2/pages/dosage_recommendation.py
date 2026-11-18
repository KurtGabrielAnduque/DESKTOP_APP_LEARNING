from PySide6.QtCore import Signal, Slot, QTimer
from PySide6.QtWidgets import (
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnalysisStatusPanel(QFrame):
    """Handles all post-click states: validation warning, loading, and post-analysis actions."""

    confirm_dosage_clicked = Signal()
    retest_clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("analysisStatusPanel")

        layout = QVBoxLayout(self)

        # State 1: Missing sample warning banner
        self.warning_box = QFrame()
        self.warning_box.setObjectName("warningBanner")
        warning_layout = QVBoxLayout(self.warning_box)
        warning_layout.addWidget(QLabel("Sample Not Detected"))
        warning_layout.addWidget(
            QLabel("Please place the 1L sample in the analysis chamber before starting.")
        )
        warning_layout.addWidget(
            QLabel("Note: If the jar is already placed, check the box above and start.")
        )

        # State 2: Loading / processing banner
        self.loading_box = QFrame()
        self.loading_box.setObjectName("loadingBanner")
        loading_layout = QVBoxLayout(self.loading_box)
        loading_layout.addWidget(QLabel("Analyzing Raw Water Sample, please wait..."))

        # State 3: Completed actions (your upcoming 2 post-analysis buttons)
        self.completed_box = QFrame()
        self.completed_box.setObjectName("completedBanner")
        completed_layout = QVBoxLayout(self.completed_box)
        completed_layout.addWidget(QLabel("Analysis Complete. Select next step:"))

        btn_row = QHBoxLayout()
        self.proceed_btn = QPushButton("Proceed to Dosage")
        self.retest_btn = QPushButton("Re-run Sample")
        self.proceed_btn.clicked.connect(self.confirm_dosage_clicked.emit)
        self.retest_btn.clicked.connect(self.retest_clicked.emit)
        btn_row.addWidget(self.proceed_btn)
        btn_row.addWidget(self.retest_btn)
        completed_layout.addLayout(btn_row)

        layout.addWidget(self.warning_box)
        layout.addWidget(self.loading_box)
        layout.addWidget(self.completed_box)

        self.hide_all()

    def hide_all(self):
        self.warning_box.hide()
        self.loading_box.hide()
        self.completed_box.hide()

    def show_warning(self):
        self.hide_all()
        self.warning_box.show()

    def show_loading(self):
        self.hide_all()
        self.loading_box.show()

    def show_completed(self):
        self.hide_all()
        self.completed_box.show()


class StartAnalysis(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("startAnalysisCard")
        self.is_jar_secured = False

        main_container_layout = QVBoxLayout(self)

        # Pre-check controls
        self.controls_box = QFrame()
        controls_layout = QVBoxLayout(self.controls_box)

        self.jar_secured_check = QCheckBox(
            "Check only if the 1L raw water sample is placed in the chamber"
        )
        self.start_analysis_button = QPushButton("Start Raw Water Analysis")

        self.jar_secured_check.toggled.connect(self.container_checker)
        self.start_analysis_button.clicked.connect(self.perform_analysis)

        controls_layout.addWidget(self.jar_secured_check)
        controls_layout.addWidget(self.start_analysis_button)

        # Separated status banner component
        self.status_panel = AnalysisStatusPanel()
        self.status_panel.retest_clicked.connect(self.reset_controls)

        main_container_layout.addWidget(self.controls_box)
        main_container_layout.addWidget(self.status_panel)

    @Slot(bool)
    def container_checker(self, checked: bool):
        self.is_jar_secured = checked

    @Slot()
    def perform_analysis(self):
        if not self.is_jar_secured:
            self.status_panel.show_warning()
            return

        # Lock controls so operator cannot double-trigger while analyzing
        self.start_analysis_button.setEnabled(False)
        self.start_analysis_button.setText("Analyzing...")
        self.jar_secured_check.setEnabled(False)
        self.status_panel.show_loading()
        # add waiting time then
        QTimer.singleShot(3000, self.finish_analysis)

    @Slot()
    def finish_analysis(self):
        self.start_analysis_button.hide()
        self.status_panel.show_completed()

    @Slot()
    def reset_controls(self):
        self.start_analysis_button.show()
        self.start_analysis_button.setEnabled(True)
        self.start_analysis_button.setText("Start Raw Water Analysis")
        self.jar_secured_check.setEnabled(True)
        self.status_panel.hide_all()


class DosageRecommendation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        self.page_label = QLabel("Raw Water Quality Analyzer")
        self.start_the_analysis = StartAnalysis()

        layout.addWidget(self.page_label)
        layout.addWidget(self.start_the_analysis)
        layout.addStretch()  # Placed at the bottom so header + card stay pinned to the top