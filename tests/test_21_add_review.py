import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.titles import TITLES

@allure.feature("Products")
@allure.story("Review")
@allure.title("Add review on product")
@allure.description("Verify user can add review on product.")

def test_add_review(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_products()

    with allure.step(f'Verify page title "{TITLES['products']}"'):
        expect(app.products.page).to_have_title(TITLES["products"])

    app.products.click_first_view_product()

    with allure.step(f'Verify page title "{TITLES['product_details']}"'):
        expect(app.product_details.page).to_have_title(TITLES["product_details"])

    with allure.step(f'Verify "Write Your Review" is visible'):
        expect(app.product_details.title_review).to_be_visible()

    email = generate_email()
    app.product_details.fill_review_form(email)
    app.product_details.click_submit_review()

    app.product_details.verify_submit_success()