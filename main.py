import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

class JanelaTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomo - Test")
        self.resize(300, 150)

        # Txt centralizado na janela
        label = QLabel("25:00", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 40px; font-weight: bold;")

        self.setCentralWidget(label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaTest()
    janela.show()
    sys.exit(app.exec())
