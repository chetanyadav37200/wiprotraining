import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(scope='module')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    yield driver
    driver.quit()


def test_open_amazon(driver):
    assert "amazon" in driver.current_url, "URL for Amazon is not correct"
    time.sleep(4)
    assert "amazon" in driver.title.lower(), "Title for Amazon is not correct"
    print("\nOpened Amazon Home - Title and URL verified")

def test_search_product(driver):
    wait = WebDriverWait(driver, 10)  # corrected class name

    # Wait until search box is visible
    search_box = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys('wireless mouse')

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    # Wait until results page title contains 'wireless'
    wait.until(EC.title_contains("wireless"))

    assert 'wireless' in driver.current_url.lower(), 'Search result page did not load'
    assert 'wireless' in driver.title.lower(), 'Search result page did not load'
    print("\nSearch results page loaded successfully")


def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # Wait for at least the first product to be visible
    first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a h2 span')))
    print("\nFirst Product:", first_product.text)

    # Get all product titles (returns a list)
    product_titles = driver.find_elements(By.CSS_SELECTOR, 'a h2 span')
    print(f"\nFound {len(product_titles)} products")

    # Print first 5 product titles
    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")