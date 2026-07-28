import allure
import pytest

from utils.data_generator import generate_email
from utils.test_data.contact import UPLOAD_FILE_PATH

@pytest.mark.no_ads_block
@allure.feature("Submit form")
@allure.story("Contact us form")
@allure.title("Contact us form submission")
@allure.description("Verify contact us form can be filled and successfully submit.")

def test_contact_us_form_submission(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_contact_us()

    app.contact_us.verify_get_in_touch_visible()

    email = generate_email()

    app.contact_us.fill_contact_us_form(email)
    app.contact_us.upload_file(UPLOAD_FILE_PATH["path"])
    app.contact_us.submit_form()
    
    app.contact_us.verify_success_message_visible()

    app.contact_us.click_home()
    app.home.verify_loaded()