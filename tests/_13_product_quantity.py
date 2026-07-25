import allure

from utils.test_data import QUANTITY

@allure.feature("Cart")
@allure.story("Product quantity")
@allure.title("Product quantity in cart")
@allure.description("Verify product quantity in cart.")

def test_product_quantity(home_page, product_details_page, cart_page):
    home_page.open()
    home_page.verify_loaded()

    product = home_page.get_product_info(2)
    home_page.click_view_product(2)

    product_details_page.verify_loaded()

    product_details_page.set_quantity(QUANTITY["value"])

    product_details_page.click_add_to_cart()
    product_details_page.click_modal_view_cart()

    cart_page.verify_loaded()

    cart_page.verify_quantity(0, QUANTITY["value"])
    cart_page.verify_product(0, product)
