import allure
import re

from pathlib import Path
from playwright.sync_api import expect

def expect_url(page, expected: str):
    with allure.step(f'Verify URL "{expected}"'):
        expect(page).to_have_url(expected)

def expect_url_contains(page, expected: str):
    with allure.step(f'Verify URL contains "{expected}"'):
        expect(page).to_have_url(re.compile(f".*{re.escape(expected)}.*"))

def expect_title(page, expected: str):
    with allure.step(f'Verify page title "{expected}"'):
        expect(page).to_have_title(expected)

def expect_visible(locator, name: str):
    with allure.step(f'Verify "{name}" is visible'):
        expect(locator).to_be_visible()

def expect_text(locator, expected: str):
    with allure.step(f'Verify text "{expected}"'):
        expect(locator).to_have_text(expected)

def expect_contains(locator, expected: str):
    with allure.step(f'Verify text contains "{expected}"'):
        expect(locator).to_contain_text(expected)

def expect_product(product: dict, expected: dict):
    with allure.step("Verify product"):
        expect_text(product["name"], expected["name"])
        expect_text(product["price"], f'Rs. {expected["price"]}')

        total = expected["price"] * product["quantity"]
        expect_text(product["total"], f"Rs. {total}")

def expect_greater_than(actual: int, expected: int, description: str):
    with allure.step(f'Verify {description}: {actual} > {expected}'):
        assert actual > expected

def expect_file_exists(file: Path):
    with allure.step(f'Verify "{file.name}" exists'):
        assert file.exists(), f"{file} does not exist"

def expect_equal(actual, expected, description: str):
    with allure.step(f'Verify {description}'):
        assert actual == expected, (
            f"\nExpected: {expected}\n"
            f"Actual: {actual}"
        )