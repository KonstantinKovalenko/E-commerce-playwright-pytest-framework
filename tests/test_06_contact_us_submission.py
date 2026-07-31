import allure
import pytest

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.contact import UPLOAD_FILE_PATH
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible, expect_text

@pytest.mark.no_ads_block
@allure.feature("Submit form")
@allure.story("Contact us form")
@allure.title("Contact us form submission")
@allure.description("Verify contact us form can be filled and successfully submit.")

def test_contact_us_form_submission(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_contact_us()
    expect_visible(app.contact_us.title_get_in_touch, "Get in touch")

    email = generate_email()
    app.contact_us.fill_contact_us_form(email)
    app.contact_us.upload_file(UPLOAD_FILE_PATH["path"])
    app.contact_us.submit_form()
    expect_text(app.contact_us.success_message, "Success! Your details have been submitted successfully.")

    app.contact_us.click_home()
    expect_title(app.home.page, TITLES["home"])