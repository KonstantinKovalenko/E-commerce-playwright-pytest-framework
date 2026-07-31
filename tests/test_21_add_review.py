import allure

from playwright.sync_api import expect
from utils.data_generator import generate_email
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible, expect_text

@allure.feature("Products")
@allure.story("Review")
@allure.title("Add review on product")
@allure.description("Verify user can add review on product.")

def test_add_review(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_products()
    expect_title(app.products.page, TITLES["products"])

    app.products.click_first_view_product()
    expect_title(app.product_details.page, TITLES["product_details"])
    expect_visible(app.product_details.title_review, "Write Your Review")

    email = generate_email()
    app.product_details.fill_review_form(email)
    app.product_details.click_submit_review()
    expect_text(app.product_details.review_success_message, "Thank you for your review.")