import allure

from pages.base_page import BasePage
from utils.test_data.contact import CONTACT_US
from pages.locators.contact_us_locators import ContactUsLocators as L

class ContactUsPage(BasePage):
    def verify_get_in_touch_visible(self):
        self.verify_visible(
            self.page.locator(L.TITLE_GET_IN_TOUCH),
            "Get in touch title"
        )

    def verify_success_message_visible(self):
        self.verify_text(
            self.page.locator(L.SUCCESS_MESSAGE),
            "Success! Your details have been submitted successfully."
        )

    def click_home(self):
        self.click(
            self.page.locator(L.BUTTON_HOME),
            "Home button"
        )

    def fill_contact_us_form(self, email: str):
        self.fill(self.page.locator(L.INPUT_NAME), CONTACT_US["name"], "Name")
        self.fill(self.page.locator(L.INPUT_EMAIL), email, "Email")
        self.fill(self.page.locator(L.INPUT_SUBJECT), CONTACT_US["subject"], "Subject")
        self.fill(self.page.locator(L.INPUT_MESSAGE), CONTACT_US["message"], "Message")

    def upload_file(self, file_path: str):
        with allure.step(f'Upload file from "{file_path}"'):
            self.page.locator(L.BUTTON_UPLOAD_FILE).set_input_files(file_path)

    def submit_form(self):
        with allure.step("Submit contact form"):
            self.page.evaluate("window.confirm = () => true;")

            self.click(self.page.locator(L.BUTTON_SUBMIT), "Submit button")

            self.page.wait_for_selector(L.SUCCESS_MESSAGE, timeout=15000)