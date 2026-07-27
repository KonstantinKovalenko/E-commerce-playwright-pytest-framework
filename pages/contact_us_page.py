import allure

from pages.base_page import BasePage
from utils.test_data import CONTACT_US

class ContactUsPage(BasePage):
    PATH = "/contact_us"

    GET_IN_TOUCH_TITLE = ".contact-form h2"
    SUCCESS_MESSAGE = '.contact-form div.status'

    NAME_INPUT = '[data-qa="name"]'
    EMAIL_INPUT = '[data-qa="email"]'
    SUBJECT_INPUT = '[data-qa="subject"]'
    MESSAGE_INPUT = "#message"

    UPLOAD_FILE_BUTTON = '[name="upload_file"]'
    SUBMIT_BUTTON = '[data-qa="submit-button"]'
    HOME_BUTTON = '#form-section a'

    def verify_get_in_touch_visible(self):
        self.verify_visible(
            self.page.locator(self.GET_IN_TOUCH_TITLE),
            "Get in touch title"
        )

    def verify_success_message_visible(self):
        self.verify_text(
            self.page.locator(self.SUCCESS_MESSAGE),
            "Success! Your details have been submitted successfully."
        )

    def fill_contact_us_form(self, email: str):
        self.fill(self.page.locator(self.NAME_INPUT), CONTACT_US["name"], "Name")
        self.fill(self.page.locator(self.EMAIL_INPUT), email, "Email")
        self.fill(self.page.locator(self.SUBJECT_INPUT), CONTACT_US["subject"], "Subject")
        self.fill(self.page.locator(self.MESSAGE_INPUT), CONTACT_US["message"], "Message")

    def upload_file(self, file_path: str):
        with allure.step(f'Upload file from "{file_path}"'):
            self.page.locator(self.UPLOAD_FILE_BUTTON).set_input_files(file_path)

    def click_home(self):
        self.click(
            self.page.locator(self.HOME_BUTTON),
            "Home button"
        )

    def submit_form(self):
        with allure.step("Submit contact form"):
            with allure.step("Prepare to click 'OK' in pup-up dialog"):
                self.page.once("dialog", lambda dialog: dialog.accept())
                self.click(self.page.locator(self.SUBMIT_BUTTON), "Submit button")