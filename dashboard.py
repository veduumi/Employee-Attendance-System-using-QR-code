import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt

class DashboardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dashboard')
        self.setMinimumWidth(1000)
        self.setMinimumHeight(300)

        # Create widgets
        title_label = QLabel("Dashboard")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding:30px")

        button2 = QPushButton("Check Employees Details")

        button3 = QPushButton("Check Attention Detail")
        button4 = QPushButton("Add New Employee Detail")
        button2.setStyleSheet(
            "font-size: 13px; color: white; background-color: blue; padding: 15px 10px; border: none; border-radius: 5px;")
        button3.setStyleSheet(
            "font-size: 13px; color: white; background-color: blue; padding: 15px 10px; border: none; border-radius: 5px;")
        button4.setStyleSheet(
            "font-size: 13px; color: white; background-color: blue; padding: 15px 10px; border: none; border-radius: 5px;")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(button4)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        cp = QDesktopWidget().availableGeometry().center()
        self.move(cp - self.rect().center())

        # button1.clicked.connect(self.openNewAdminWindow)
        button2.clicked.connect(self.openEmployeeDetail)
        button3.clicked.connect(self.openEmployeeAttendance)
        button4.clicked.connect(self.openAddEmployee)

    def openNewAdminWindow(self):
        subprocess.Popen(['python', 'addingAdmin.py'])
    def openEmployeeAttendance(self):
        subprocess.Popen(['python', 'employeeAttendance.py'])
    def openEmployeeDetail(self):
        subprocess.Popen(['python', 'employeeDetail.py'])
    def openAddEmployee(self):
        subprocess.Popen(['python', 'addEmployee.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DashboardApp()
    ex.show()
    sys.exit(app.exec_())
