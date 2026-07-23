def test_home_page(home_page):
    home_page.open()
    home_page.verify_loaded()