from pages.base_page import BasePage

class HomePage(BasePage):

    PATH = "/"

    def verify_loaded(self):
        self.verify_title("Automation Exercise")