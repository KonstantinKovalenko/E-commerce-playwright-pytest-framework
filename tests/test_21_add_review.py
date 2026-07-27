import allure

from utils.data_generator import generate_email

@allure.feature("Products")
@allure.story("Products review")
@allure.title("Add review on product")
@allure.description("Verify user can add review on product.")

def test_add_review(home_page, products_page, product_details_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()
    products_page.verify_loaded()

    products_page.click_first_view_product()

    product_details_page.verify_loaded()

    product_details_page.verify_review_title_visible()

    email = generate_email()

    product_details_page.fill_review_form(email)
    product_details_page.click_submit_review()

    product_details_page.verify_submit_success()