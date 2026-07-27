import allure

@allure.feature("Test Cases")
@allure.story("Test Cases page")
@allure.title("Test Cases page navigation")
@allure.description("Verify Test Cases page navigation.")

def test_navigate_to_test_cases_page(home_page, test_cases_page):
    home_page.open()
    home_page.verify_loaded()

    home_page.header.click_test_cases()

    test_cases_page.verify_loaded()
    test_cases_page.verify_test_cases_visible()