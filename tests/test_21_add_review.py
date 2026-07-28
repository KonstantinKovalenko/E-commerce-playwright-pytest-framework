import allure

from utils.data_generator import generate_email

@allure.feature("Products")
@allure.story("Review")
@allure.title("Add review on product")
@allure.description("Verify user can add review on product.")

def test_add_review(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()
    app.products.verify_loaded()

    app.products.click_first_view_product()
    app.product_details.verify_loaded()

    app.product_details.verify_review_title_visible()

    email = generate_email()
    app.product_details.fill_review_form(email)
    app.product_details.click_submit_review()

    app.product_details.verify_submit_success()