from pathlib import Path
import sys
from PySide6.QtCore import QFileSystemWatcher, Qt, Slot
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def enable_live_qss(app: QApplication, qss_path: Path) -> QFileSystemWatcher:
    """Loads style.qss and automatically re-applies it whenever the file is saved."""
    resolved_path = str(qss_path.resolve())
    watcher = QFileSystemWatcher([resolved_path], app)

    def apply_stylesheet(path: str):
        file = Path(path)
        if file.exists():
            app.setStyleSheet(file.read_text(encoding="utf-8"))
        # Re-watch the path because VS Code replaces files atomically on save
        if path not in watcher.files():
            watcher.addPath(path)

    watcher.fileChanged.connect(apply_stylesheet)
    apply_stylesheet(resolved_path)
    return watcher


class QSSPlayground(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS Styling Sandbox")
        self.setFixedSize(520, 400)

        root = QWidget()
        self.setCentralWidget(root)
        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(24, 24, 24, 24)

        # 1. Card Container (QFrame supports QSS background & borders out of the box)
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)

        # 2. Typography Labels (#titleLabel, #subtitleLabel)
        title = QLabel("Water Sample Calibration")
        title.setObjectName("titleLabel")

        subtitle = QLabel("Edit styles/style.qss and press Ctrl+S to see changes live.")
        subtitle.setObjectName("subtitleLabel")

        # 3. Text Input (:focus pseudo-state)
        self.sample_input = QLineEdit()
        self.sample_input.setPlaceholderText("Enter Sample ID (e.g. SMPL-001)")

        # 4. Checkbox (::indicator sub-control)
        self.confirm_check = QCheckBox("Chamber lid locked and sensor submerged")

        # 5. Dynamic Property Banner ([status="ok"] vs [status="warning"])
        self.status_banner = QFrame()
        self.status_banner.setObjectName("statusBanner")
        self.status_banner.setProperty("status", "ok")
        banner_layout = QHBoxLayout(self.status_banner)
        self.status_text = QLabel("Status: OK — Ready for measurement")
        banner_layout.addWidget(self.status_text)

        # 6. Action Buttons (Default, #dangerBtn, and :disabled)
        btn_row = QHBoxLayout()
        self.toggle_status_btn = QPushButton("Toggle Status")
        self.toggle_status_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.toggle_status_btn.clicked.connect(self.toggle_banner_state)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setObjectName("dangerBtn")
        self.reset_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.disabled_btn = QPushButton("Locked")
        self.disabled_btn.setEnabled(False)

        btn_row.addWidget(self.toggle_status_btn)
        btn_row.addWidget(self.reset_btn)
        btn_row.addWidget(self.disabled_btn)

        # Assemble Card
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addWidget(self.sample_input)
        card_layout.addWidget(self.confirm_check)
        card_layout.addWidget(self.status_banner)
        card_layout.addLayout(btn_row)

        root_layout.addWidget(card)
        root_layout.addStretch()

    @Slot()
    def toggle_banner_state(self):
        current = self.status_banner.property("status")
        next_state = "warning" if current == "ok" else "ok"

        self.status_banner.setProperty("status", next_state)
        if next_state == "ok":
            self.status_text.setText("Status: OK — Ready for measurement")
        else:
            self.status_text.setText("Status: WARNING — Recalibration required")

        # Required so Qt re-evaluates dynamic property selectors immediately
        self.status_banner.style().unpolish(self.status_banner)
        self.status_banner.style().polish(self.status_banner)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qss_file = Path(__file__).resolve().parent / "styles" / "styles.qss"
    watcher = enable_live_qss(app, qss_file)

    window = QSSPlayground()
    window.show()
    app.exec()