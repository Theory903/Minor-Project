# Main frontend application

from .pages.home_page import HomePage
from .pages.user_profile_page import UserProfilePage
from .components.search_bar import SearchBar
from .components.search_results import SearchResults
from .components.user_profile import UserProfile

class App:
    def __init__(self):
        self.home_page = HomePage()
        self.user_profile_page = UserProfilePage()
        self.search_bar = SearchBar()
        self.search_results = SearchResults()
        self.user_profile = UserProfile()
    
    def run(self):
        # Run the main application logic here
        pass
