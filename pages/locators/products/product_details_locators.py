class ProductDetailsLocators:
    PRODUCT_INFORMATION = ".product-information"
    TITLE_REVIEW = 'a[href="#reviews"]'

    PRODUCT_NAME = ".product-information h2"
    CATEGORY = '.product-information p:has-text("Category:")'
    PRICE = ".product-information span > span"
    AVAILABILITY = '.product-information p:has-text("Availability:")'
    CONDITION = '.product-information p:has-text("Condition:")'
    BRAND = '.product-information p:has-text("Brand:")'

    INPUT_QUANTITY = "#quantity"

    BUTTON_ADD_TO_CART = '[type="button"]'
    BUTTON_MODAL_VIEW_CART = '.modal-body a[href="/view_cart"]'

    INPUT_NAME = "#name"
    INPUT_EMAIL = "#email"
    INPUT_REVIEW = "#review"

    BUTTON_SUBMIT_REVIEW = "#button-review"

    REVIEW_SUCCESS_MESSAGE = ".alert-success span"