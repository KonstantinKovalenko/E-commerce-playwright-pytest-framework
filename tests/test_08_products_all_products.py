import allure

@allure.feature("Products")
@allure.story("Browsing")
@allure.title("All products and product details pages content")
@allure.description("Verify all products and product details pages contain expected content.")

def test_all_products_and_product_detail_content(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_products()

    app.products.verify_loaded()
    
    app.products.click_first_view_product()

    app.product_details.verify_loaded()
    app.product_details.verify_product_details_visible()