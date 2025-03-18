import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton

class EmployeeAttention(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Employee Attention')
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Unique ID', '  Name  ', 'Entry Time', 'Exit Time'])
        self.table.setStyleSheet(
            """
            QTableWidget {
                background-color: #333333;
                border: 2px solid #666666;
                border-radius: 5px;
                padding:10px;
                color: #ffffff;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #666666;
            }

            QTableWidget::item:selected {
                background-color: #555555;
                color: #ffffff;
            }

            QHeaderView::section {
                margin: 5px;
                background-color: #121212;
                border: none;
                padding: 5px 15px;
                border-radius:5px;
                font-weight: bold;
                color: #fff;
            }
            """
        )

        self.table.verticalHeader().setVisible(False)

        layout.addWidget(self.table)

        self.loadEmployeeDetails()

        self.refresh_button = QPushButton('Refresh')
        self.refresh_button.clicked.connect(self.loadEmployeeDetails)

        self.refresh_button.setStyleSheet(
            "font-size: 13px; color: white; background-color: blue; padding: 15px 10px; border: none; border-radius: 5px;")

        layout.addWidget(self.refresh_button)

        self.setLayout(layout)

    def loadEmployeeDetails(self):
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("SELECT  unique_id, name, entry_time, exit_time  FROM employee_logs")
            employees = cursor.fetchall()

            self.table.setRowCount(0)

            for row_num, employee in enumerate(employees):
                self.table.insertRow(row_num)
                for col_num, data in enumerate(employee):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(0x84)
                    self.table.setItem(row_num, col_num, item)

            conn.close()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    employee_attention_widget = EmployeeAttention()
    employee_attention_widget.show()
    sys.exit(app.exec_())
