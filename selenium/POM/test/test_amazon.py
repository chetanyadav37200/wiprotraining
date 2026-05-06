from pages.home_page import HomePage

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for Amazon is not correct'
    print("\nOpened Amazon")

def test_search_product(driver):
    homepage = HomePage(driver)
    homepage.type_search_input()
    homepage.click_search_input()

    assert homepage.is_amazon_page_loaded()
    print("\nSearch result page loaded successfully")
