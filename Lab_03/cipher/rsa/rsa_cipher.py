import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from cipher.rsa.rsa_cipher import RSACipher

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RSA CIPHER")

        # Khởi tạo giao diện
        self.init_ui()

        # Khởi tạo đối tượng mã hóa RSA
        self.rsa_cipher = RSACipher()

    def init_ui(self):
        # Các nhãn và ô nhập
        self.plain_text = QTextEdit()
        self.cipher_text = QTextEdit()
        self.info_text = QTextEdit()
        self.signature_text = QTextEdit()

        # Các nút
        self.btn_generate = QPushButton("Generate Keys")
        self.btn_encrypt = QPushButton("Encryption")
        self.btn_decrypt = QPushButton("Decryption")
        self.btn_sign = QPushButton("Sign")
        self.btn_verify = QPushButton("Verify")

        # Gắn sự kiện cho nút
        self.btn_generate.clicked.connect(self.generate_keys)
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.btn_decrypt.clicked.connect(self.decrypt)
        self.btn_sign.clicked.connect(self.sign)
        self.btn_verify.clicked.connect(self.verify)

        # Layout giao diện
        layout = QVBoxLayout()

        # Tiêu đề
        title = QLabel("<h2 style='text-align:center;'>RSA CIPHER</h2>")
        layout.addWidget(title)
        layout.addWidget(self.btn_generate)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Plain Text"))
        row1.addWidget(QLabel("Information"))
        layout.addLayout(row1)

        row2 = QHBoxLayout()
        row2.addWidget(self.plain_text)
        row2.addWidget(self.info_text)
        layout.addLayout(row2)

        row3 = QHBoxLayout()
        row3.addWidget(QLabel("Cipher Text"))
        row3.addWidget(QLabel("Signature"))
        layout.addLayout(row3)

        row4 = QHBoxLayout()
        row4.addWidget(self.cipher_text)
        row4.addWidget(self.signature_text)
        layout.addLayout(row4)

        row5 = QHBoxLayout()
        row5.addWidget(self.btn_encrypt)
        row5.addWidget(self.btn_decrypt)
        row5.addWidget(self.btn_sign)
        row5.addWidget(self.btn_verify)
        layout.addLayout(row5)

        self.setLayout(layout)

    # Chức năng xử lý
    def generate_keys(self):
        try:
            self.rsa_cipher.generate_keys()
            QMessageBox.information(self, "Thông báo", "Đã tạo khóa RSA thành công!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tạo khóa: {str(e)}")

    def encrypt(self):
        try:
            _, pub_key = self.rsa_cipher.load_keys()
            plaintext = self.plain_text.toPlainText()
            cipher = self.rsa_cipher.encrypt(plaintext, pub_key)
            self.cipher_text.setPlainText(cipher.hex())
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi mã hóa: {str(e)}")

    def decrypt(self):
        try:
            priv_key, _ = self.rsa_cipher.load_keys()
            ciphertext_hex = self.cipher_text.toPlainText()
            ciphertext = bytes.fromhex(ciphertext_hex)
            decrypted = self.rsa_cipher.decrypt(ciphertext, priv_key)
            self.plain_text.setPlainText(decrypted if decrypted else "Giải mã thất bại")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi giải mã: {str(e)}")

    def sign(self):
        try:
            priv_key, _ = self.rsa_cipher.load_keys()
            message = self.info_text.toPlainText()
            signature = self.rsa_cipher.sign(message, priv_key)
            self.signature_text.setPlainText(signature.hex())
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi ký: {str(e)}")

    def verify(self):
        try:
            _, pub_key = self.rsa_cipher.load_keys()
            message = self.info_text.toPlainText()
            signature = bytes.fromhex(self.signature_text.toPlainText())
            result = self.rsa_cipher.verify(message, signature, pub_key)
            if result:
                QMessageBox.information(self, "Thông báo", "Chữ ký hợp lệ!")
            else:
                QMessageBox.warning(self, "Thông báo", "Chữ ký KHÔNG hợp lệ!")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi xác minh: {str(e)}")

# Khởi chạy chương trình
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())
