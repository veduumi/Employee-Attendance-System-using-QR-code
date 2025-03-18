import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QDesktopWidget

class Attention(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Attention')
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.button = QPushButton('Take Attention')
        layout.addWidget(self.button)
        self.button.setStyleSheet(
            "font-size: 15px; color: white; background-color: orangered; padding: 15px 10px; border: none; border-radius: 5px;margin-top:20px")
        self.setLayout(layout)

        self.button.clicked.connect(self.openQRCodeScanner)

    def openQRCodeScanner(self):
        subprocess.Popen(['python', 'qrCodeScanner.py'])


    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showEvent(self, event):
        self.centerWindow()
        super().showEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Attention_page = Attention()
    Attention_page.show()
    sys.exit(app.exec_())

