from utils.test_data.products import BRANDS

class ProductsLocators:
    PATH = "/products"

    PRODUCTS_LIST = ".features_items"
    PRODUCTS_ARRAY = ".features_items .col-sm-4 .productinfo"
    BUTTON_MODAL_CONTINUE_SHOPPING = ".modal-footer button"
    BUTTON_MODAL_VIEW_CART = '.modal-body a[href="/view_cart"]'
    BUTTON_ADD_TO_CART = ".features_items .productinfo a"

    VIEW_PRODUCT = ".features_items .choose a"
    PRODUCT_FRAME = ".features_items .single-products"
    BUTTON_OVERLAY_ADD_TO_CART = ".features_items .product-overlay a"

    INPUT_SEARCH_PRODUCT = "#search_product"
    BUTTON_SEARCH_PRODUCT = "#submit_search"

    TITLE_SEARCHED_PRODUCTS = '.features_items > h2.title'
    PRODUCT_NAME = '.features_items .productinfo p'

    BRANDS_FILTERS = ".brands-name"
    BRANDS_BUTTONS = {
        BRANDS["polo"]: 'a[href="/brand_products/Polo"]',
        BRANDS["h_m"]: 'a[href="/brand_products/H&M"]',
        BRANDS["madame"]: 'a[href="/brand_products/Madame"]',
        BRANDS["mast_harbour"]: 'a[href="/brand_products/Mast & Harbour"]',
        BRANDS["babyhug"]: 'a[href="/brand_products/Babyhug"]',
        BRANDS["allen_solly_junior"]: 'a[href="/brand_products/Allen Solly Junior"]',
        BRANDS["kookie_kids"]: 'a[href="/brand_products/Kookie Kids"]',
        BRANDS["biba"]: 'a[href="/brand_products/Biba"]'
    }