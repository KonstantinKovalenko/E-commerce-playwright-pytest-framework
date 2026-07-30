from pages.base_page import BasePage

class TestCasesPage(BasePage):
    PATH = "/test_cases"

    def __init__(self, page: Page):
        super().__init__(page)
        self.title_test_cases = page.get_by_role("heading", level=2, name="Test Cases")

    def verify_loaded(self):
        self.verify_title("Automation Practice Website for UI Testing - Test Cases")

    def verify_test_cases_visible(self):
        self.verify_visible(
            self.title_test_cases,
            "Test Cases section"
        )