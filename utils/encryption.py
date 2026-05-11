from cryptography.fernet import Fernet
from utils.config import ENCRYPTION_KEY

cipher = Fernet(ENCRYPTION_KEY.encode())


def encrypt_text(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()


def decrypt_text(text: str) -> str:
    return cipher.decrypt(text.encode()).decode()
