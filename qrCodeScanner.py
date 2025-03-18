import cv2
import sqlite3
import datetime

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table to store entry and exit times
cursor.execute('''CREATE TABLE IF NOT EXISTS employee_logs (
                    id INTEGER PRIMARY KEY,
                    unique_id TEXT,
                    name TEXT,
                    entry_time TIMESTAMP,
                    exit_time TIMESTAMP
                    )''')
conn.commit()

def decode_qr_code(image):
    # Load the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_code_detector = cv2.QRCodeDetector()
    data, bbox, _ = qr_code_detector.detectAndDecode(gray)

    # If QR code detected, return the data
    if bbox is not None:
        print("QR Code detected!")
        return data
    else:
        print("No QR Code detected.")
        return None

def toggle_status(unique_id, status):
    cursor.execute("SELECT status FROM employees WHERE unique_id=?", (unique_id,))
    cursor.fetchone()

    cursor.execute("UPDATE employees SET status=? WHERE unique_id=?", (status, unique_id))
    conn.commit()

def record_entry_exit(unique_id):
    cursor.execute("SELECT * FROM employees WHERE unique_id=?", (unique_id,))
    employee = cursor.fetchone()
    if employee:
        name = employee[1]
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("SELECT * FROM employee_logs WHERE unique_id=? AND exit_time IS NULL", (unique_id,))
        existing_entry = cursor.fetchone()
        if existing_entry:
            # Employee is exiting
            exit_time = current_time
            cursor.execute("UPDATE employee_logs SET exit_time=? WHERE unique_id=? AND exit_time IS NULL", (exit_time, unique_id))
            print("Exit recorded for employee:", name)
        else:
            # Employee is entering
            entry_time = current_time
            cursor.execute("INSERT INTO employee_logs (unique_id, name, entry_time) VALUES (?, ?, ?)", (unique_id, name, entry_time))
            print("Entry recorded for employee:", name)
        conn.commit()
    else:
        print("Employee data not found for ID:", unique_id)

def main():
    # Capture video from default camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture video.")
            break

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Check for QR code
        qr_data = decode_qr_code(frame)
        if qr_data:
            print("QR Code Data:", qr_data)
            record_entry_exit(qr_data)
            break

        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
