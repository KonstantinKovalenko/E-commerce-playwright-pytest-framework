from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.locators.components.footer_locators import FooterLocators as L

class Footer(BasePage):
    def verify_subscription_visible(self):
        self.verify_text(
            self.page.locator(L.TITLE_SUBSCRIPTION),
            "Subscription"
        )

    def verify_subscribe_success_visible(self):
        self.verify_visible(
            self.page.locator(L.SUBSCRIBE_SUCCESS),
            "You have been successfully subscribed!"
        )

    def scroll_down_to_footer(self):
        self.scroll_to(
            self.page.locator(L.SITE_FOOTER),
            "Site footer"
        )

    def subscribe(self, email: str):
        self.fill(self.page.locator(L.INPUT_EMAIL), email, "Email")

        self.click(
            self.page.locator(L.BUTTON_SUBSCRIBE),
            "Subscribe button"
        )        