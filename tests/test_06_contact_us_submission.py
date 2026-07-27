import allure
import pytest

from utils.data_generator import generate_email
from utils.test_data import UPLOAD_FILE_PATH

@pytest.mark.no_ads_block
@allure.feature("Contact us form")
@allure.story("Contact us form")
@allure.title("Contact us form submission")
@allure.description("Verify contact us form can be filled and successfully submit.")

def test_contact_us_form_submission(home_page, contact_us_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_contact_us()

    contact_us_page.verify_get_in_touch_visible()

    email = generate_email()

    contact_us_page.fill_contact_us_form(email)
    contact_us_page.upload_file(UPLOAD_FILE_PATH["path"])
    contact_us_page.submit_form()
    
    contact_us_page.verify_success_message_visible()

    contact_us_page.click_home()
    home_page.verify_loaded()