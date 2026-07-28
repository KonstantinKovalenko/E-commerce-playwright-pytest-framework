import allure

@allure.feature("Cart")
@allure.story("Add products")
@allure.title("Add products to cart")
@allure.description("Verify products can be added to cart and cart page will contain added products.")

def test_add_products_to_cart(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()
    app.products.verify_loaded()
    
    product_1 = app.products.get_product_info(0)
    app.products.hover_over_product(0)
    app.products.add_product_to_cart(0)

    app.products.click_modal_continue_shopping()

    product_2 = app.products.get_product_info(1)
    app.products.hover_over_product(1)
    app.products.add_product_to_cart(1)

    app.products.click_modal_view_cart()
    app.cart.verify_loaded()

    app.cart.verify_product(0, product_1)
    app.cart.verify_product(1, product_2)

    app.cart.remove_all_products()
    app.cart.verify_cart_empty()