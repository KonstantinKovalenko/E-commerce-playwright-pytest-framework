import allure

@allure.feature("Navigation")
@allure.story("Test Cases page")
@allure.title("Navigate to Test Cases page")
@allure.description("Verify user can navigate to Test Cases page via header button.")

def test_navigate_to_test_cases_page(app):
    app.home.open()
    app.home.verify_loaded()

    app.header.click_test_cases()

    app.test_cases.verify_loaded()
    app.test_cases.verify_test_cases_visible()