import allure

from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.test_data.contact import CONTACT_US

class ContactUsPage(BasePage):
    PATH = "/contact_us"

    def __init__(self, page: Page):
        super().__init__(page)

        self.title_get_in_touch = page.get_by_role("heading", name="Get In Touch")
        self.success_message = page.locator(".contact-form").get_by_text("Success! Your details have been submitted successfully.")

        self.input_name = page.locator('[data-qa="name"]')
        self.input_email = page.locator('[data-qa="email"]')
        self.input_subject = page.locator('[data-qa="subject"]')
        self.input_message = page.locator('#message')

        self.button_upload_file = page.locator('[name="upload_file"]')
        self.button_submit = page.locator('[data-qa="submit-button"]')
        self.button_home = page.locator("#form-section").get_by_role("link", name="Home")

    def verify_success_message_visible(self):
        self.verify_text(
            self.success_message,
            "Success! Your details have been submitted successfully."
        )

    def click_home(self):
        self.click(
            self.button_home,
            "Home button"
        )

    def fill_contact_us_form(self, email: str):
        self.fill(self.input_name, CONTACT_US["name"], "Name")
        self.fill(self.input_email, email, "Email")
        self.fill(self.input_subject, CONTACT_US["subject"], "Subject")
        self.fill(self.input_message, CONTACT_US["message"], "Message")

    def upload_file(self, file_path: str):
        with allure.step(f'Upload file from "{file_path}"'):
            self.button_upload_file.set_input_files(file_path)

    def submit_form(self):
        with allure.step("Submit contact form"):
            self.page.once("dialog", lambda dialog: dialog.accept())
            self.click(self.button_submit, "Submit button")