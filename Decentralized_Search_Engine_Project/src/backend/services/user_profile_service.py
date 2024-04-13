import os
import json

class UserProfileService:
    def __init__(self, user_data_dir):
        self.user_data_dir = user_data_dir
        self.users = {}

    def register_user(self, username, email, password):
        """
        Register a new user.
        """
        user_id = self.generate_user_id()
        self.users[user_id] = {'username': username, 'email': email, 'password': password}
        self.save_user_data()
        return user_id

    def login_user(self, email, password):
        """
        Log in a user and return their user ID.
        """
        for user_id, user_data in self.users.items():
            if user_data['email'] == email and user_data['password'] == password:
                return user_id
        return None

    def get_user_info(self, user_id):
        """
        Get user information by user ID.
        """
        return self.users.get(user_id, None)

    def generate_user_id(self):
        """
        Generate a unique user ID.
        """
        return str(uuid.uuid4())

    def save_user_data(self):
        """
        Save user data to a JSON file.
        """
        with open(os.path.join(self.user_data_dir, 'users.json'), 'w') as f:
            json.dump(self.users, f)

    def load_user_data(self):
        """
        Load user data from a JSON file.
        """
        user_data_file = os.path.join(self.user_data_dir, 'users.json')
        if os.path.exists(user_data_file):
            with open(user_data_file, 'r') as f:
                self.users = json.load(f)

# Example usage:
if __name__ == "__main__":
    # Initialize the user profile service with the directory to store user data
    user_profile_service = UserProfileService("user_data")

    # Register a new user
    user_id = user_profile_service.register_user("user1", "user1@example.com", "password123")
    print("Registered User ID:", user_id)

    # Log in a user
    logged_in_user_id = user_profile_service.login_user("user1@example.com", "password123")
    print("Logged In User ID:", logged_in_user_id)

    # Get user information
    user_info = user_profile_service.get_user_info(logged_in_user_id)
    print("User Information:", user_info)
