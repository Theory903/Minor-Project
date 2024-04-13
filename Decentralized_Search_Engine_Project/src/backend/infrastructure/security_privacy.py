import bcrypt
from cryptography.fernet import Fernet

class SecurityPrivacy:
    @staticmethod
    def hash_password(password):
        """
        Hash the user's password for storage.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password

    @staticmethod
    def verify_password(password, hashed_password):
        """
        Verify the user's password against the hashed password.
        """
        return bcrypt.checkpw(password.encode(), hashed_password)

    @staticmethod
    def generate_key():
        """
        Generate a symmetric encryption key.
        """
        return Fernet.generate_key()

    @staticmethod
    def encrypt_data(data, key):
        """
        Encrypt sensitive data using symmetric encryption.
        """
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data

    @staticmethod
    def decrypt_data(encrypted_data, key):
        """
        Decrypt encrypted data using symmetric encryption.
        """
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
        return decrypted_data

# Example usage:
if __name__ == "__main__":
    # Hash a user's password
    password = "password123"
    hashed_password = SecurityPrivacy.hash_password(password)
    print("Hashed Password:", hashed_password)

    # Verify a user's password
    entered_password = "password123"
    is_verified = SecurityPrivacy.verify_password(entered_password, hashed_password)
    print("Password Verified:", is_verified)

    # Generate a symmetric encryption key
    key = SecurityPrivacy.generate_key()
    print("Symmetric Encryption Key:", key)

    # Encrypt sensitive data
    data = "Sensitive information"
    encrypted_data = SecurityPrivacy.encrypt_data(data, key)
    print("Encrypted Data:", encrypted_data)

    # Decrypt encrypted data
    decrypted_data = SecurityPrivacy.decrypt_data(encrypted_data, key)
    print("Decrypted Data:", decrypted_data)
