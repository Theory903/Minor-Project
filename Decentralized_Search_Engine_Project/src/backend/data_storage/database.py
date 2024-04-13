import sqlite3
import uuid

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """
        Create necessary tables if they do not exist.
        """
        # Create table to store user information
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               user_id TEXT PRIMARY KEY,
                               username TEXT,
                               email TEXT,
                               age INTEGER,
                               gender TEXT
                               )''')
        self.connection.commit()

        # Create table to store search history
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS search_history (
                               search_id INTEGER PRIMARY KEY AUTOINCREMENT,
                               user_id TEXT,
                               query TEXT,
                               timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                               FOREIGN KEY (user_id) REFERENCES users(user_id)
                               )''')
        self.connection.commit()

    def add_user(self, username, email, age, gender):
        """
        Add a new user to the database.
        """
        user_id = str(uuid.uuid4())
        self.cursor.execute("INSERT INTO users (user_id, username, email, age, gender) VALUES (?, ?, ?, ?, ?)",
                            (user_id, username, email, age, gender))
        self.connection.commit()
        return user_id

    def record_search(self, user_id, query):
        """
        Record a user's search query.
        """
        self.cursor.execute("INSERT INTO search_history (user_id, query) VALUES (?, ?)", (user_id, query))
        self.connection.commit()

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()

# Example usage:
if __name__ == "__main__":
    # Initialize database
    db = Database("search_engine.db")

    # Create necessary tables
    db.create_tables()

    # Add a new user
    user_id = db.add_user("Alice", "alice@example.com", 30, "Female")
    print("User ID:", user_id)

    # Record a user's search
    db.record_search(user_id, "Decentralized search engine")

    # Close database connection
    db.close()
