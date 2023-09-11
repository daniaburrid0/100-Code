import secrets
import hashlib
import sqlite3
from typing import List, Tuple
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QMessageBox,
)


class PasswordManager:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                website TEXT,
                email TEXT,
                password TEXT
            )
            """
        )
        self.conn.commit()

    def add_password(self, website: str, email: str, password: str):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT INTO passwords (website, email, password)
            VALUES (?, ?, ?)
            """,
            (website, email, self.hash_password(password)),
        )
        self.conn.commit()

    def get_passwords(self) -> List[Tuple[int, str, str, str]]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM passwords")
        return cursor.fetchall()

    def hash_password(self, password: str) -> str:
        salt = secrets.token_hex(16)
        hashed_password = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000
        )
        return f"{salt}:{hashed_password.hex()}"

    def verify_password(self, password: str, hashed_password: str) -> bool:
        salt, hashed = hashed_password.split(":")
        return hashed == hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000
        ).hex()


class PasswordManagerWindow(QMainWindow):
    def __init__(self, password_manager: PasswordManager):
        super().__init__()
        self.password_manager = password_manager
        self.setWindowTitle("Password Manager")
        self.setFixedSize(500, 300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.website_label = QLabel("Website:")
        self.website_entry = QLineEdit()
        self.email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.generate_password_button = QPushButton("Generate Password")
        self.generate_password_button.clicked.connect(self.generate_password)
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_password)
        self.passwords_button = QPushButton("View Passwords")
        self.passwords_button.clicked.connect(self.view_passwords)
        self.layout.addWidget(self.website_label)
        self.layout.addWidget(self.website_entry)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_entry)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_entry)
        self.layout.addWidget(self.generate_password_button)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.passwords_button)
        self.layout.addLayout(button_layout)

    def generate_password(self):
        password = secrets.token_hex(8)
        self.password_entry.setText(password)

    def add_password(self):
        website = self.website_entry.text()
        email = self.email_entry.text()
        password = self.password_entry.text()
        if not website or not email or not password:
            QMessageBox.warning(
                self, "Error", "Please fill in all fields.", QMessageBox.Ok
            )
            return
        self.password_manager.add_password(website, email, password)
        self.website_entry.setText("")
        self.email_entry.setText("")
        self.password_entry.setText("")
        QMessageBox.information(
            self, "Success", "Password added successfully.", QMessageBox.Ok
        )

    def view_passwords(self):
        passwords = self.password_manager.get_passwords()
        if not passwords:
            QMessageBox.information(
                self, "No Passwords", "No passwords found.", QMessageBox.Ok
            )
            return
        password_dialog = PasswordDialog(passwords)
        password_dialog.exec_()


class PasswordDialog(QMessageBox):
    def __init__(self, passwords: List[Tuple[int, str, str, str]]):
        super().__init__()
        self.setWindowTitle("Passwords")
        self.setText("Here are your saved passwords:")
        self.setDetailedText("\n".join(f"{p[1]} | {p[2]} | {p[3]}" for p in passwords))


if __name__ == "__main__":
    app = QApplication([])
    password_manager = PasswordManager("passwords.db")
    window = PasswordManagerWindow(password_manager)
    window.show()
    app.exec_()