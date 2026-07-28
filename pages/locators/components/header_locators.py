class HeaderLocators:
    SITE_HEADER = "#header"

    BUTTON_PRODUCTS = 'a[href="/products"]'
    BUTTON_CART = '.shop-menu a[href="/view_cart"]'
    BUTTON_SIGNUP_LOGIN = '.shop-menu a[href="/login"]'
    BUTTON_LOGOUT = 'a[href="/logout"]'
    BUTTON_DELETE_ACCOUNT = 'a[href="/delete_account"]'
    BUTTON_TEST_CASES = '.shop-menu a[href="/test_cases"]'
    BUTTON_CONTACT_US = 'a[href="/contact_us"]'
    
    LOGGED_IN_USER = 'a:has-text("Logged in as")'