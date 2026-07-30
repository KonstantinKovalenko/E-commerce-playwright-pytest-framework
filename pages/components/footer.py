from playwright.sync_api import Page
from pages.base_page import BasePage

class Footer(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.site_footer = page.locator('#footer')
        self.title_subscription = page.locator('.single-widget').get_by_role("heading", level=2, name="Subscription")
        self.input_email = page.locator('#susbscribe_email')
        self.button_subscribe = page.locator('#subscribe')
        self.subscribe_success = page.locator('#success-subscribe')
      
    def verify_subscription_visible(self):
        self.verify_text(
            self.title_subscription,
            "Subscription"
        )

    def scroll_down_to_footer(self):
        self.scroll_to(
            self.site_footer,
            "Site footer"
        )

    def subscribe(self, email: str):
        self.fill(self.input_email, email, "Email")

        self.click(
            self.button_subscribe,
            "Subscribe button"
        )        