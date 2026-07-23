from components.header import Header
from pages.base_page import BasePage


class HomePage(BasePage):

    PATH = "/"

    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)

    def verify_loaded(self):
        self.verify_title("Automation Exercise")