from cryptography.fernet import Fernet

from utils.config import ENCRYPTION_KEY


if not ENCRYPTION_KEY:
    raise ValueError(
        "ENCRYPTION_KEY missing from environment variables"
    )

try:
    cipher = Fernet(
        ENCRYPTION_KEY.encode()
    )

except Exception as e:
    raise ValueError(
        f"Invalid Fernet key: {e}"
    )


def encrypt_text(text: str) -> str:
    return cipher.encrypt(
        text.encode()
    ).decode()


def decrypt_text(text: str) -> str:
    return cipher.decrypt(
        text.encode()
    ).decode()
