import allure

from playwright.sync_api import expect
from utils.test_data.titles import TITLES
from utils.assertions import expect_title, expect_visible

@allure.feature("Navigation")
@allure.story("Test Cases page")
@allure.title("Navigate to Test Cases page")
@allure.description("Verify user can navigate to Test Cases page via header button.")

def test_navigate_to_test_cases_page(app):
    app.home.open()
    expect_title(app.home.page, TITLES["home"])

    app.header.click_test_cases()
    expect_title(app.test_cases.page, TITLES["test_cases"])
    expect_visible(app.test_cases.title_test_cases, "Test Cases section")