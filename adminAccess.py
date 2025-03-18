import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
import sqlite3
import subprocess

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setMinimumWidth(300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.username_input.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding: 5px; text-align: center;");

        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.password_input.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff; padding: 5px; text-align: center;");

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)
        self.login_button.setStyleSheet(
            "font-size: 15px; color: white; background-color: orangered; padding: 15px 10px; border: none; border-radius: 5px;margin-top:20px")

        self.setLayout(layout)
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                            id INTEGER PRIMARY KEY,
                            username TEXT UNIQUE,
                            password TEXT,
                            email TEXT
                          )''')
        conn.commit()
        conn.close()

    def login(self):
        username = self.username_input.text() 
        password = self.password_input.text()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            subprocess.Popen(['python', 'dashboard.py'])
            self.close()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Invalid username or password')

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
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec_())
