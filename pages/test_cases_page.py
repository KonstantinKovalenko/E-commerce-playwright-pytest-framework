from pages.base_page import BasePage

class TestCasesPage(BasePage):
    PATH = "/test_cases"

    TEST_CASES_TITLE = "#form h2"

    def verify_loaded(self):
        self.verify_title("Automation Practice Website for UI Testing - Test Cases")

    def verify_test_cases_visible(self):
        self.verify_visible(
            self.page.locator(self.TEST_CASES_TITLE),
            "Test Cases section"
        )