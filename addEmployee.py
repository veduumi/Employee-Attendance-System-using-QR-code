import sys
import random
import string
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget

class AddEmployeeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Add Employee Detail')
        self.setMinimumWidth(400)
        self.setMinimumHeight(300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        self.name_input.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding: 5px; text-align: center;");

        self.address_label = QLabel('Address:')
        self.address_input = QLineEdit()
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        self.address_input.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding: 5px; text-align: center;");


        self.mobile_label = QLabel('Mobile Number:')
        self.mobile_input = QLineEdit()
        layout.addWidget(self.mobile_label)
        layout.addWidget(self.mobile_input)
        self.mobile_input.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding: 5px; text-align: center;");

        self.generateUniqueID()

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.submitDetails)
        layout.addWidget(self.submit_button)
        self.submit_button.setStyleSheet(
            "font-size: 13px; color: white; background-color: blue; padding: 15px 10px; border: none; border-radius: 5px;")

        self.setLayout(layout)

        self.centerOnScreen()

    def generateUniqueID(self):
        unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.unique_id = unique_id

    def submitDetails(self):
        name = self.name_input.text()
        address = self.address_input.text()
        mobile = self.mobile_input.text()

        if not name or not address or not mobile:
            QMessageBox.warning(self, 'Missing Information', 'All fields are required.')
            return

        self.addToDatabase(name, address, mobile)

        msg = f'Name: {name}\nAddress: {address}\nMobile Number: {mobile}\nUnique ID: {self.unique_id}'
        QMessageBox.information(self, 'Employee Details', msg)

    def addToDatabase(self, name, address, mobile):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            address TEXT,
                            mobile TEXT,
                            status INTEGER,
                            unique_id TEXT
                          )''')

        # Insert data into table
        cursor.execute("INSERT INTO employees (name, address, mobile, status, unique_id) VALUES (?, ?, ?, ?, ?)",
                       (name, address, mobile, 1, self.unique_id))
        conn.commit()

        # Close database connection
        conn.close()

    def centerOnScreen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    add_employee_widget = AddEmployeeWidget()
    add_employee_widget.show()
    sys.exit(app.exec_())
