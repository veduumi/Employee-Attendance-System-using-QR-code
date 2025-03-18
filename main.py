import subprocess
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Employee Attendance Management System')
        self.setMinimumWidth(600)
        self.setMaximumWidth(600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        title_label = QLabel("Employee Attendance Management System")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding:30px")
        layout.addWidget(title_label)
        button1 = QPushButton("Admin Access")
        button2 = QPushButton("Attendance")
        button1.setStyleSheet(
            "font-size: 13px; color: white; background-color: orangered; padding: 15px 10px; border: none; border-radius: 5px;")
        button2.setStyleSheet(
            "font-size: 13px; color: white; background-color: blue; padding: 15px 10px; border: none; border-radius: 5px;")
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)
        self.center()
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)

    def center(self):
        screen_geometry = QApplication.desktop().screenGeometry()
        center_point = screen_geometry.center()
        window_top_left = center_point - self.rect().center()
        self.move(window_top_left)

    def button1_clicked(self):
        subprocess.Popen(['python', 'adminAccess.py'])

    def button2_clicked(self):
        subprocess.Popen(['python', 'takingAttention.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
