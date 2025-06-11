import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)
        
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.exec_()
        
    def call_api_encrypt(self):
        # Check if server is running
        try:
            requests.get("http://127.0.0.1:5000/N")
        except requests.exceptions.ConnectionError:
            self.show_error("Cannot connect to server. Please make sure the server is running.")
            return
            
        # Get input values
        plain_text = self.ui.textEdit.toPlainText()
        key = self.ui.textEdit_2.toPlainText()
        
        # Validate input
        if not plain_text:
            self.show_error("Please enter plain text")
            return
        if not key:
            self.show_error("Please enter key")
            return
        try:
            key = int(key)
        except ValueError:
            self.show_error("Key must be a number")
            return
            
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": plain_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_3.setPlainText(data["cipher_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                self.show_error(f"Server error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Error: {str(e)}")
            
    def call_api_decrypt(self):
        # Check if server is running
        try:
            requests.get("http://127.0.0.1:5000")
        except requests.exceptions.ConnectionError:
            self.show_error("Cannot connect to server. Please make sure the server is running.")
            return
            
        # Get input values
        cipher_text = self.ui.textEdit_3.toPlainText()
        key = self.ui.textEdit_2.toPlainText()
        
        # Validate input
        if not cipher_text:
            self.show_error("Please enter cipher text")
            return
        if not key:
            self.show_error("Please enter key")
            return
        try:
            key = int(key)
        except ValueError:
            self.show_error("Key must be a number")
            return
            
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": cipher_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setPlainText(data["plain_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                self.show_error(f"Server error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())