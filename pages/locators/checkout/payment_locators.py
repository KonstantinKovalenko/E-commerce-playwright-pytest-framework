class PaymentLocators:
    PATH = "/payment"

    INPUT_NAME = '[data-qa="name-on-card"]'
    INPUT_CARD_NUMBER = '[data-qa="card-number"]'
    INPUT_CVC = '[data-qa="cvc"]'
    INPUT_EXPIRE_MONTH = '[data-qa="expiry-month"]'
    INPUT_EXPIRE_YEAR = '[data-qa="expiry-year"]'

    BUTTON_PAY_CONFIRM_ORDER = '[data-qa="pay-button"]'

    SUCCESS_MESSAGE = "#success_message"