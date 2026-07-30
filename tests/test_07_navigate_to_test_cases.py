import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES

@allure.feature("Navigation")
@allure.story("Test Cases page")
@allure.title("Navigate to Test Cases page")
@allure.description("Verify user can navigate to Test Cases page via header button.")

def test_navigate_to_test_cases_page(app):
    app.home.open()
    
    with allure.step(f'Verify page title "{TITLES['home']}"'):
        expect(app.home.page).to_have_title(TITLES["home"])

    app.header.click_test_cases()

    with allure.step(f'Verify page title "{TITLES['test_cases']}"'):
        expect(app.test_cases.page).to_have_title(TITLES["test_cases"])

    with allure.step(f'Verify "Test Cases" section is visible'):
        expect(app.test_cases.title_test_cases).to_be_visible()