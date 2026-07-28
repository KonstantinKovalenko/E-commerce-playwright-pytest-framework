from utils.test_data.products import BRANDS

class BrandProductsLocators:
    PATH = "/brand_products"

    PRODUCTS_LIST = ".features_items .col-sm-4"
    TITLE_FILTERED_PRODUCTS = '.features_items > h2'

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