from playwright.sync_api import Page
from pages.base_page import BasePage

class Footer(BasePage):
    SITE_FOOTER = '#footer'
    SUBSCRIPTION_TITLE = ".single-widget h2"
    EMAIL_INPUT = "#susbscribe_email"
    SUBSCRIBE_BUTTON = '#subscribe'
    SUBSCRIBE_SUCCESS = "#success-subscribe"

    def __init__(self, page: Page):
        super().__init__(page)

    def verify_subscribe_success_visible(self):
        self.verify_visible(
            self.page.locator(self.SUBSCRIBE_SUCCESS),
            "You have been successfully subscribed!"
        )

    def scroll_down_to_footer(self):
        self.scroll_to(
            self.page.locator(self.SITE_FOOTER),
            "Site footer"
        )

    def verify_subscription_visible(self):
        self.verify_text(
            self.page.locator(self.SUBSCRIPTION_TITLE),
            "Subscription"
        )

    def subscribe(self, email: str):
        self.fill(self.page.locator(self.EMAIL_INPUT), email, "Email")

        self.click(
            self.page.locator(self.SUBSCRIBE_BUTTON),
            "Subscribe button"
        )        