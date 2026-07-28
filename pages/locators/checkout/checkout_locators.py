class CheckoutLocators:
    PATH = "/checkout"

    CART_ITEMS = "tbody tr"
    ITEM_NAME = ".cart_description a"
    ITEM_PRICE = ".cart_price p"
    ITEM_QUANTITY = ".cart_quantity button"
    ITEM_TOTAL_PRICE = ".cart_total p"

    DELIVERY_ADDRESS = "#address_delivery"
    BILLING_ADDRESS = "#address_invoice"
    TOTAL_PRICES = ".cart_total_price"

    TEXT_AREA_COMMENT = ".form-control"
    BUTTON_PLACE_ORDER = 'a[href="/payment"]'