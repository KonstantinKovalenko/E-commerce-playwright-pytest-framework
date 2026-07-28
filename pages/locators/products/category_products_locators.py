from utils.test_data.products import CATEGORIES

class CategoryProductsLocators:
    PATH = "/category_products"

    PRODUCTS_LIST = ".features_items"
    TITLE_FILTERED_PRODUCTS = '.features_items > h2'

    CATEGORY_BUTTONS = {
        CATEGORIES["women"]: ('a[href="#Women"]', "#Women li"),
        CATEGORIES["men"]: ('a[href="#Men"]', "#Men li"),
        CATEGORIES["kids"]: ('a[href="#Kids"]', "#Kids li"),
    }