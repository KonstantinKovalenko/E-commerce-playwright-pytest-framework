from utils.test_data.products import CATEGORIES

class HomeLocators:
    PATH = "/"

    VIEW_PRODUCT = ".features_items .choose a"
    PRODUCT_CARDS = ".features_items .col-sm-4 .productinfo"

    BUTTON_MODAL_CONTINUE_SHOPPING = ".modal-footer button"
    BUTTON_MODAL_VIEW_CART = '.modal-body a[href="/view_cart"]'
    BUTTON_ADD_TO_CART = ".features_items .productinfo a"
    BUTTON_SCROLL_UP = "#scrollUp"

    CATEGORIES_SECTION = "#accordian"
    CATEGORY_BUTTONS = {
        CATEGORIES["women"]: ('a[href="#Women"]', "#Women li"),
        CATEGORIES["men"]: ('a[href="#Men"]', "#Men li"),
        CATEGORIES["kids"]: ('a[href="#Kids"]', "#Kids li"),
    }

    RECOMMENDED_SECTION = ".recommended_items"
    RECOMMENDED_ITEMS = ".recommended_items .productinfo"
    BUTTON_RECOMMENDED_ADD_TO_CART = ".recommended_items .productinfo a"

    SLIDE_CAROUSEL_TITLES = "#slider-carousel .carousel-inner h2"