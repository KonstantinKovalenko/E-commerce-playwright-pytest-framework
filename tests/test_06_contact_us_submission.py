import allure
import pytest

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.contact import UPLOAD_FILE_PATH
from utils.test_data.titles import TITLES

@pytest.mark.no_ads_block
@allure.feature("Submit form")
@allure.story("Contact us form")
@allure.title("Contact us form submission")
@allure.description("Verify contact us form can be filled and successfully submit.")

def test_contact_us_form_submission(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_contact_us()

    with allure.step(f'Verify "Get in touch" title is visible'):
        expect(app.contact_us.title_get_in_touch).to_be_visible()

    email = generate_email()

    app.contact_us.fill_contact_us_form(email)
    app.contact_us.upload_file(UPLOAD_FILE_PATH["path"])
    app.contact_us.submit_form()
    
    app.contact_us.verify_success_message_visible()

    app.contact_us.click_home()

    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])