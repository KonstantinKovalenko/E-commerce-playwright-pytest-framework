import allure

@allure.feature("Products")
@allure.story("Products and product details")
@allure.title("All products and product details pages content")
@allure.description("Verify all products and product details pages contain expected content.")

def test_all_products_and_product_detail_content(home_page, products_page, product_details_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_products()

    products_page.verify_loaded()
    
    products_page.click_first_view_product()

    product_details_page.verify_loaded()
    product_details_page.verify_product_details_visible()