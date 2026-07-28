class CartLocators:
    PATH = "/view_cart"

    CART_EMPTY = "#empty_cart b"
    CART_ITEMS = "tbody tr"
    ITEM_NAME = ".cart_description a"
    ITEM_PRICE = ".cart_price p"
    ITEM_QUANTITY = ".cart_quantity button"
    ITEM_TOTAL_PRICE = ".cart_total p"

    BUTTON_PROCEED_TO_CHECKOUT = "#do_action .check_out"
    BUTTON_MODAL_REGISTER_LOGIN = '.modal-body a[href="/login"]'
    BUTTON_REMOVE_PRODUCT = ".cart_quantity_delete"