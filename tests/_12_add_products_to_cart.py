import allure

@allure.feature("Cart")
@allure.story("Add to cart")
@allure.title("Add products to cart")
@allure.description("Verify products can be added to cart and cart page will contain added products.")

def test_add_products_to_cart(home_page, products_page, cart_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()

    products_page.verify_loaded()
    
    product_1 = products_page.get_product_info(0)
    products_page.hover_over_product(0)
    products_page.add_product_to_cart(0)

    products_page.click_modal_continue_shopping()

    product_2 = products_page.get_product_info(1)
    products_page.hover_over_product(1)
    products_page.add_product_to_cart(1)

    products_page.click_modal_view_cart()

    cart_page.verify_loaded()

    cart_page.verify_product(0, product_1)
    cart_page.verify_product(1, product_2)